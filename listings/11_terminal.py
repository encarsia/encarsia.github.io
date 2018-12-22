#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, Vte, GObject, GLib


class Handler:

    def on_window_destroy(self, *args):
        Gtk.main_quit()

    def on_button_clicked(self, widget):
        command = "python\n"
        x.terminal.feed_child(command.encode())


class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        GObject.type_register(Vte.Terminal)
        
        self.builder.add_from_file("11_terminal.glade")
        self.builder.connect_signals(Handler())
        
        self.terminal = self.builder.get_object("term")
        self.terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            None,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DEFAULT,
            )

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()


x = Example()
x.main()
