#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_switch_state_set(self,widget,state):
        if state is True:
            print("switch is on")
        else:
            print("switch is off")

    def on_cbutton_toggled(self,widget):
        if widget.get_active():
            print("checkbox checked")
        else:
            print("checkbox unchecked")

    def on_rbutton1_toggled(self,widget):
        if widget.get_active():
            print("radiobutton selection changed to 1")

    def on_rbutton2_toggled(self,widget):
        if widget.get_active():
            print("radiobutton selection changed to 2")

    def on_rbutton3_toggled(self,widget):
        if widget.get_active():
            print("radiobutton selection changed to 3")

class Example:
    
    def __init__(self):
        
        self.gladefile = "04_clickableelements.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(Handler())

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()

x = Example()
x.main()
