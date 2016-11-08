#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import gi
gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_go_clicked(self,widget):
        for i in range(101):
            x.progbar1.set_fraction(i/100)
            x.progbar2.pulse()
            x.progbar2.set_text("%d %%" % i)
            x.levbar1.set_value(i/100)
            x.levbar2.set_value((i/100)*5)
            time.sleep(.05)
            #interrupt main loop to update GUI
            while Gtk.events_pending(): Gtk.main_iteration()
        x.progbar2.set_fraction(1)

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("06_progresslevel.glade")
        self.builder.connect_signals(Handler())

        self.progbar1 = self.builder.get_object("prog1")
        self.progbar2 = self.builder.get_object("prog2")
        self.levbar1 = self.builder.get_object("lev1")
        self.levbar2 = self.builder.get_object("lev2")

        self.levbar2.add_offset_value("high",4)
        self.levbar2.add_offset_value("full",5)

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()

x = Example()
x.main()

