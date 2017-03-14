#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gio, GdkPixbuf

class Handler:

    def on_window_destroy(self,window):
        window.close()

    def on_dialog_close(self,widget,*event):
        widget.hide_on_delete()
        return True

    def on_filechooser_dialog_delete_event(self,widget,event):
        widget.hide_on_delete()
        return True

    def on_filechooser_dialog_response(self,widget,response):
        if response == -6:
            self.on_dialog_close(widget)
        elif response == -5:
            app.uri = widget.get_filename()
            app.draw_pixbuf(app.uri)
            self.on_dialog_close(widget)
            #check if file is already fav
            app.obj("fav_button").set_active(False)
            for item in app.obj("fav_store"):
                if item[0] == app.uri:
                    app.obj("fav_button").set_active(True)
                    break
            #for item in app.obj("fav_store"):
                #if item[0] == app.uri:
                    #app.obj("fav_button").set_active(True)
                    #break
                #else:
                    #app.obj("fav_button").set_active(False)
                    #app.obj("fav_combo").set_active_iter(None)
            
    def on_filechooser_dialog_file_activated(self,widget):
        self.on_filechooser_dialog_response(widget,0)

    def on_open_button_clicked(self,widget):
        app.obj("filechooser_dialog").show_all()

    def on_setwp_button_clicked(self,widget):
        app.setting.set_string("picture-uri","file://%s" % app.uri)

    def on_window_size_allocate(self,widget,size):
        app.draw_pixbuf(app.uri)
    
    def on_filechooser_dialog_update_preview(self,widget):
        app.uri = widget.get_filename()
        if app.uri != None and os.path.isfile(app.uri):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(app.uri,200,200,True)
            app.obj("preview").set_from_pixbuf(pixbuf)

    def on_fav_button_toggled(self,widget):
        if widget.get_active():
            print("fav")
        else:
            print("unfav")
        #generate treestore from gsettings
        #if widget.get_active():
            ##add to combobox, avoid duplicate
            #for item in app.obj("fav_store"):
                #if item[0] != app.uri:
                    #row = app.obj("fav_store").append([app.uri,os.path.split(app.uri)[1]])
                    #app.obj("fav_combo").set_active_iter(row)
                    #break
        #else:
            ##remove from combobox
            #pass

    def on_fav_combo_changed(self,widget):
        if widget.get_active() > -1:
            app.uri = app.obj("fav_store").get_value(widget.get_active_iter(),0)
            app.obj("fav_button").set_active(True)

class ExampleApp:

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("activate", self.on_app_activate)
        self.app.connect("shutdown", self.on_app_shutdown)

    def on_app_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("17_gsettings.glade")
        builder.connect_signals(Handler())

        #read configuration from gsetting
        self.setting = Gio.Settings.new("org.gnome.desktop.background")
        file = self.setting.get_value("picture-uri")
        self.uri = file.get_string()[7:]

        self.obj = builder.get_object
        self.obj("window").set_application(app)
        self.obj("window").set_wmclass("Wallpaper changer","Wallpaper changer")
        self.obj("window").show_all()
        self.draw_pixbuf(self.uri)

        #add buttons to headerbar of Glade generated dialog
        button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
        button.set_property("can-default",True)
        self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.CANCEL)
        button = Gtk.Button.new_from_stock(Gtk.STOCK_APPLY)
        button.set_property("can-default",True)
        self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.OK)

    def draw_pixbuf(self,file):
        size=self.obj("image_area").get_allocation()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(file,size.width,size.height,True)
        self.obj("image_area").set_from_pixbuf(pixbuf)

    def on_app_shutdown(self, app):
        self.app.quit()

    def run(self, argv):
        self.app.run(argv)

app = ExampleApp()
app.run(sys.argv)
