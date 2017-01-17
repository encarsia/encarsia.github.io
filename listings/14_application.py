#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gio

class Handler:

    def on_window_destroy(self,window):
        window.close()

    def on_dialog_delete_event(self,widget,event):
        widget.hide_on_delete()
        return True

    def on_aboutbutton_clicked(self,widget):
        app.obj("aboutdialog").show_all()

    def on_messagebutton_clicked(self,widget):
        app.obj("messdialog").format_secondary_text("")
        app.obj("messdialog").show_all()
        
    def on_dialog_response(self,widget,response):
        if response == -8:
            widget.hide_on_delete()
        elif response == -9:
            widget.format_secondary_text("Doch!")

class ExampleApp:

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("startup", self.on_app_startup)
        self.app.connect("activate", self.on_app_activate)
        self.app.connect("shutdown", self.on_app_shutdown)

    def on_app_startup(self, app):
        print("Gio.Application startup signal emitted")

    def on_app_activate(self, app):
        print("Gio.Application activate signal emitted")
        builder = Gtk.Builder()
        builder.add_from_file("13_dialoge.glade")
        builder.add_from_file("14_giomenu.ui")
        builder.connect_signals(Handler())

        app.set_app_menu(builder.get_object("appmenu"))
        self.obj = builder.get_object
        self.obj("window").set_application(app)
        
        #display application name in upper panel of the GNOME Shell
        self.obj("window").set_wmclass("Application test","Application test")
        self.obj("window").show_all()
        
        self.add_simple_action("about", self.on_action_about_activated)
        self.add_simple_action("message", self.on_action_message_activated)
        self.add_simple_action("quit", self.on_action_quit_activated)

    def on_app_shutdown(self, app):
        print("Gio.Application shutdown signal emitted")

    def add_simple_action(self, name, callback):
        action = Gio.SimpleAction.new(name)
        action.connect("activate", callback)
        self.app.add_action(action)

    def on_action_about_activated(self, action, user_data):
        self.obj("aboutdialog").show_all()

    def on_action_message_activated(self, action, user_data):
        Handler().on_messagebutton_clicked(self)

    def on_action_quit_activated(self, action, user_data):
        self.app.quit()

    def run(self, argv):
        self.app.run(argv)

app = ExampleApp()
app.run(sys.argv)
