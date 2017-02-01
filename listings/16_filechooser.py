#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GdkPixbuf

class Handler:

    def on_window_destroy(self,window):
        window.close()

    def on_dialog_close(self,widget,*event):
        widget.hide_on_delete()
        return True

    def on_filechooser_dialog_response(self,widget,response):
        if response == -6:
            print("Cancel")
        elif response == -5:
            print("File selection: %s" % widget.get_filename())
        self.on_dialog_close(widget)

    def on_filechooser_dialog_file_activated(self,widget):
        self.on_filechooser_dialog_response(widget,-5)

    def on_filechooser_dialog_update_preview(self,widget):
        if widget.get_filename() != None and os.path.isfile(widget.get_filename()):
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(widget.get_filename(),200,200,True)
            app.obj("preview").set_from_pixbuf(pixbuf)

    def on_file_button_clicked(self,widget):
        app.obj("filechooser_dialog").show_all()

    def on_dir_button_clicked(self,widget):

        dialog = Gtk.FileChooserDialog("Choose a folder",
                                    app.obj("window"),
                                    Gtk.FileChooserAction.SELECT_FOLDER,
                                    (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                    Gtk.STOCK_APPLY, Gtk.ResponseType.OK))
        dialog.set_default_size(600, 300)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Folder selection: %s" % dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

class ExampleApp:

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("activate", self.on_app_activate)
        self.app.connect("shutdown", self.on_app_shutdown)

    def on_app_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("16_filechooser.glade")
        builder.connect_signals(Handler())

        self.obj = builder.get_object
        self.obj("window").set_application(app)
        self.obj("window").set_wmclass("Filechooser example","Filechooser example")
        self.obj("window").show_all()

        #add filters to filechooser dialog
        self.obj("filefilter").set_name("Image files")
        self.obj("filechooser_dialog").add_filter(self.obj("filefilter"))
        self.obj("png_filter").set_name("PNG files")
        self.obj("filechooser_dialog").add_filter(self.obj("png_filter"))
        self.obj("jpg_filter").set_name("JPG files")
        self.obj("filechooser_dialog").add_filter(self.obj("jpg_filter"))

        #add buttons to headerbar of Glade generated dialog
        button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
        button.set_property("can-default",True)
        self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.CANCEL)
        button = Gtk.Button.new_from_stock(Gtk.STOCK_APPLY)
        button.set_property("can-default",True)
        self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.OK)

    def on_app_shutdown(self, app):
        self.app.quit()

    def run(self, argv):
        self.app.run(argv)

app = ExampleApp()
app.run(sys.argv)
