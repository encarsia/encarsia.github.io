#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("01_minimal.glade")
        self.builder.connect_signals(Handler())

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()

x = Example()
x.main()
