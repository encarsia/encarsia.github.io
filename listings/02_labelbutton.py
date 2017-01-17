#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_button_clicked(self,widget):
        new_text = random.choice(x.label_texts)
        x.builder.get_object("label").set_text(new_text)

    def on_t_button_toggled(self,widget):
        if widget.get_active():
            x.builder.get_object("label").set_text("")
            x.builder.get_object("button").set_sensitive(False)
        else:
            x.builder.get_object("button").set_sensitive(True)

class Example:
    
    def __init__(self):
        
        self.gladefile = "02_labelbutton.glade"

        self.label_texts = ["The things you used to own, now they own you.",
                            "I am Jack's complete lack of surprise. I am Jack's Broken Heart.",
                            "On a long enough time line, the survival rate for everyone drops to zero.",
                            "Sticking feathers up your butt does not make you a chicken!",
                            "I am Jack's smirking revenge."]

        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(Handler())

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()

x = Example()
x.main()
