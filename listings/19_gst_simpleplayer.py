#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")
gi.require_version("GstVideo", "1.0")
from gi.repository import Gst, Gtk, GLib, GstVideo


class GenericException(Exception):
    pass


class Handler:

    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_playpause_togglebutton_toggled(self, widget):
        if app.playpause_button.get_active():
            img = Gtk.Image.new_from_icon_name(Gtk.STOCK_MEDIA_PLAY,
                                               Gtk.IconSize.BUTTON)
            widget.set_property("image", img)
            app.pause()
        else:
            img = Gtk.Image.new_from_icon_name(Gtk.STOCK_MEDIA_PAUSE,
                                               Gtk.IconSize.BUTTON)
            widget.set_property("image", img)
            app.play()
       
    def on_forward_clicked(self, widget):
        app.skip_time()

    def on_backward_clicked(self, widget):
        app.skip_time(-1)
    
    def on_progress_value_changed(self, widget):
        app.on_slider_seek

    def on_vbutton_clicked(self, widget):
        app.clear_playbin()
        app.setup_player("mediaplayer.avi")
        if app.playpause_button.get_active() is True:
            app.playpause_button.set_active(False)
        else:
            app.play()
        
    def on_ibutton_clicked(self, widget):
        app.clear_playbin()
        app.setup_player("mediaplayer.jpg")
        app.pause()


class GstPlayer:

    def __init__(self):
        
        # init GStreamer
        Gst.init(None)
        
        # setting up builder
        builder = Gtk.Builder()
        builder.add_from_file("19_gst_player.glade")
        builder.connect_signals(Handler())

        self.movie_window = builder.get_object("play_here")
        self.playpause_button = builder.get_object("playpause_togglebutton")
        self.slider = builder.get_object("progress")
        self.slider_handler_id = self.slider.connect("value-changed", self.on_slider_seek)
        
        window = builder.get_object("window")
        window.show_all()

        # setting up videoplayer
        self.player = Gst.ElementFactory.make("playbin", "player")
        self.sink = Gst.ElementFactory.make("xvimagesink")
        self.sink.set_property("force-aspect-ratio", True)

    def setup_player(self,f):
        # file to play must be transmitted as uri
        uri = "file://" + os.path.abspath(f)
        self.player.set_property("uri", uri)
        
        # make playbin play in specified DrawingArea widget instead of
        # separate, GstVideo needed
        win_id = self.movie_window.get_property("window").get_xid()
        self.sink.set_window_handle(win_id)
        self.player.set_property("video-sink", self.sink)
        
    def play(self):
        self.is_playing = True
        self.player.set_state(Gst.State.PLAYING)
        #starting up a timer to check on the current playback value
        GLib.timeout_add(1000, self.update_slider)
        
    def pause(self):
        self.is_playing = False
        self.player.set_state(Gst.State.PAUSED)
        
    def current_position(self):
        status,position = self.player.query_position(Gst.Format.TIME)
        return position

    def skip_time(self,direction=1):
        #skip 20 seconds on forward/backward button
        app.player.seek_simple(Gst.Format.TIME,  Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT, self.current_position() + float(20) * Gst.SECOND * direction )

    def update_slider(self):
        if not self.is_playing:
            return False # cancel timeout
        else:
            success, self.duration = self.player.query_duration(Gst.Format.TIME)
            # adjust duration and position relative to absolute scale of 100
            self.mult = 100 / (self.duration / Gst.SECOND)
            if not success:
                raise GenericException("Couldn't fetch duration")
            # fetching the position, in nanosecs
            success, position = self.player.query_position(Gst.Format.TIME)
            if not success:
                raise GenericException("Couldn't fetch current position to update slider")
            
            # block seek handler so we don't seek when we set_value()
            self.slider.handler_block(self.slider_handler_id)
            self.slider.set_value(float(position) / Gst.SECOND * self.mult)
            self.slider.handler_unblock(self.slider_handler_id)
        return True # continue calling every x milliseconds

    def on_slider_seek(self, widget):
        seek_time = app.slider.get_value()
        self.player.seek_simple(Gst.Format.TIME,  Gst.SeekFlags.FLUSH | Gst.SeekFlags.KEY_UNIT, seek_time * Gst.SECOND / self.mult)
        
    def clear_playbin(self):
        try:
            self.player.set_state(Gst.State.NULL)
        except:
            pass

    def main(self):
        Gtk.main()


app = GstPlayer()
app.main()
