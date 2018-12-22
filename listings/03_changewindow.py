#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:

    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_button1_clicked(self, widget):
        x.window.hide_on_delete()
        x.set_window("win2")

    def on_button2_clicked(self, widget):
        x.window.hide_on_delete()
        x.set_window("win1")
        
    def on_info_button_clicked(self, widget):
        x.about.show_all()

    def on_close_button_clicked(self, widget):
        x.about.hide_on_delete()


class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("03_changewindow.glade")
        self.builder.connect_signals(Handler())
        
        self.about = self.builder.get_object("about_dialog")

        self.set_window("win1")
        
    def set_window(self, win):
        self.window = self.builder.get_object(win)
        self.window.show_all()

    def main(self):
        Gtk.main()


x = Example()
x.main()
