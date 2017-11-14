#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

import gi
gi.require_version('Gtk','3.0')
gi.require_version('GtkSource','3.0')

from gi.repository import Gtk, GtkSource, Gio, GObject

class Handler:
    
    def on_stylechooserwidget_button_release_event(self, widget, event):
        x.buffer.set_style_scheme(widget.get_style_scheme())

    def on_button1_clicked(self, widget):
        x.load_file("22_editor_gtksv.py", "python")

    def on_button2_clicked(self, widget):
        x.load_file("22_editor_gtksv.glade", "xml")

    def on_save_clicked(self, widget):
        saver = GtkSource.FileSaver.new(x.buffer, x.sourcefile)
        saver.save_async(0, None, None, None, None, None)

    def on_saveas_clicked(self, widget):
        saver = GtkSource.FileSaver.new_with_target(x.buffer, x.sourcefile, Gio.File.new_for_path("{}.bak".format(x.file)))
        saver.save_async(0, None, None, None, None, None)

    def on_search_entry_search_changed(self, widget):
        x.find_text(0)

    def on_search_entry_activate(self, widget):
        x.find_text()

class Editor:
    
    def __init__(self):
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("activate", self.on_app_activate)
        
    def on_app_activate(self, app):
        self.builder = Gtk.Builder()
        GObject.type_register(GtkSource.View)
        self.builder.add_from_file("22_editor_gtksv.glade")
        self.builder.connect_signals(Handler())

        #setup SourceView        
        self.view = self.builder.get_object("sv")
        self.buffer = self.view.get_buffer()
        self.sourcefile = GtkSource.File()
        self.lang_manager = GtkSource.LanguageManager()

        #setup settings for SourceView
        self.settings = GtkSource.SearchSettings()
        self.builder.get_object("search_entry").bind_property('text', self.settings, 'search-text')
        self.settings.set_search_text("initial highlight")
        self.settings.set_wrap_around(True)
        self.search_context = GtkSource.SearchContext.new(self.buffer, self.settings)

        window = self.builder.get_object("app_window")
        window.set_application(app)
        window.set_wmclass("Tutorial application","Tutorial application")
        window.show_all()

    def run(self, argv):
        self.app.run(argv)

    def load_file(self, f, lang):
        self.file = f
        self.sourcefile.set_location(Gio.File.new_for_path(f))
        self.buffer.set_language(self.lang_manager.get_language(lang))
        loader = GtkSource.FileLoader.new(self.buffer,self.sourcefile)
        loader.load_async(0, None, None, None, None, None)

    def find_text(self, start_offset=1):
        buf = self.buffer
        insert = buf.get_iter_at_mark(buf.get_insert())
        start, end = buf.get_bounds()
        insert.forward_chars(start_offset)
        match, start_iter, end_iter, wrapped = self.search_context.forward2(insert)

        if match:
            buf.place_cursor(start_iter)
            buf.move_mark(buf.get_selection_bound(), end_iter)
            self.view.scroll_to_mark(buf.get_insert(), 0.25, True, 0.5, 0.5)
            return True
        else:
            buf.place_cursor(buf.get_iter_at_mark(buf.get_insert()))

    def main(self):
        Gtk.main()

x = Editor()
x.run(sys.argv)
