#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class Handler:

    def on_window_destroy(self, *args):
        Gtk.main_quit()


class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("07_css.glade")
        self.builder.connect_signals(Handler())

        css = b"""

levelbar trough block.filled.low {
    background-color: green;
}

levelbar trough block.filled.high {
    background-color: yellow;
}
   
levelbar trough block.filled.alert {
    background-color: orange;
}

levelbar trough block.filled.full {
    background-color: red;
}
"""
        #load css stylesheet
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.bar = self.builder.get_object("lev4")
        self.bar.add_offset_value("alert", .9)

        print("low:  ", self.bar.get_offset_value("low"))
        print("high: ", self.bar.get_offset_value("high"))
        print("alert:", self.bar.get_offset_value("alert"))
        print("full: ", self.bar.get_offset_value("full"))

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()


x = Example()
x.main()
