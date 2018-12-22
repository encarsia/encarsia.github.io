#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GLib, GdkPixbuf


class Handler:

    def on_window_destroy(self, window):
        window.close()

    def on_dialog_close(self,widget, *event):
        widget.hide_on_delete()
        return True

    def on_filechooser_dialog_response(self, widget, response):
        if response == 1:
            self.on_dialog_close(widget)
        elif response == 0:
            app.uri = widget.get_filename()
            app.draw_pixbuf(app.uri)
            app.handle_fav(app.uri)
            self.on_dialog_close(widget)

    def on_filechooser_dialog_file_activated(self, widget):
        self.on_filechooser_dialog_response(widget, 0)

    def on_open_button_clicked(self, widget):
        app.obj("filechooser_dialog").show_all()

    def on_setwp_button_clicked(self, widget):
        app.bg_setting.set_string("picture-uri", "file://{}".format(app.uri))

    def on_window_size_allocate(self, widget, size):
        app.draw_pixbuf(app.uri)
    
    def on_filechooser_dialog_update_preview(self, widget):
        if widget.get_filename() != None and os.path.isfile(widget.get_filename()):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(widget.get_filename(),200, 200, True)
            app.obj("preview").set_from_pixbuf(pixbuf)

    def on_fav_button_toggled(self,widget):
        if widget.get_active():
            #add file to fav_list if not in list
            if app.uri not in app.fav_list:
                app.fav_list.append(app.uri)
        else:
            #remove file from fav_list if in list
            if app.uri in app.fav_list:
                app.fav_list.remove(app.uri)
        #update GSettings entry for favourites
        app.app_setting.set_value("favourites", GLib.Variant("as", app.fav_list))
        #update fav list in popup menu
        popup = app.obj("menu")
        #remove all items
        for i in popup.get_children():
            popup.remove(i)
        #reload all items from fav_list
        for fav in app.fav_list:
            #only label menuitem with filename instead of path 
            item = Gtk.MenuItem(os.path.split(fav)[1])
            item.connect("activate", self.on_choose_fav_from_menu, fav)
            popup.append(item)
        popup.show_all()

    def on_choose_fav_from_menu(self, widget, filename):
        app.uri = filename
        app.draw_pixbuf(filename)
        app.handle_fav(filename)

class ExampleApp:

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("activate", self.on_app_activate)
        self.app.connect("shutdown", self.on_app_shutdown)

    def on_app_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("17_gsettings.glade")
        builder.connect_signals(Handler())
        self.obj = builder.get_object

        #load existing GSettings application config
        self.bg_setting = Gio.Settings.new("org.gnome.desktop.background")
        #get_value returns Gio formatted file path
        file = self.bg_setting.get_value("picture-uri")
        #convert path into string
        self.uri = file.get_string()[7:]
        #bind GSettings key to GTK+ object 
        self.bg_setting.bind("show-desktop-icons", self.obj("switch"), "active", Gio.SettingsBindFlags.DEFAULT)

        #add GSettings schema from compiled XML file located in current directory (only recommended for test use, standard location: /usr/share/glib-2.0/schemas/)
        schema_source = Gio.SettingsSchemaSource.new_from_directory(os.getcwd(), 
                Gio.SettingsSchemaSource.get_default(), False)
        schema = Gio.SettingsSchemaSource.lookup(schema_source,"org.example.wallpaper-changer", False)
        self.app_setting = Gio.Settings.new_full(schema, None, None)
        #convert value (GLib.Variant) into native list
        self.fav_list = self.app_setting.get_value("favourites").unpack()

        self.obj("window").set_application(app)
        self.obj("window").show_all()

        self.draw_pixbuf(self.uri)
        self.handle_fav(self.uri)

    def draw_pixbuf(self,file):
        size=self.obj("image_area").get_allocation()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(file, size.width, size.height, True)
        self.obj("image_area").set_from_pixbuf(pixbuf)

    def handle_fav(self,uri):
        #set toggle button to correct state
        if uri in self.fav_list:
            self.obj("fav_button").set_active(True)
        else:
            self.obj("fav_button").set_active(False)

    def on_app_shutdown(self, app):
        self.app.quit()

    def run(self, argv):
        self.app.run(argv)


app = ExampleApp()
app.run(sys.argv)
