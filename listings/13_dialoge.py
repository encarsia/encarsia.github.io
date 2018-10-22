#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_dialog_delete_event(self,widget,event):
        widget.hide_on_delete()
        return True

    def on_aboutbutton_clicked(self,widget):
        x.obj("aboutdialog").run()

    def on_messagebutton_clicked(self,widget):
        x.obj("messdialog").format_secondary_text("")
        x.obj("messdialog").run()
        
    def on_dialog_response(self,widget,response):
        if response == -8:
            widget.hide_on_delete()
        elif response == -9:
            widget.format_secondary_text("Doch!")

class Example:
    
    def __init__(self):
        
        builder = Gtk.Builder()
        builder.add_from_file("13_dialoge.glade")
        builder.connect_signals(Handler())
        
        self.obj = builder.get_object
        self.obj("window").show_all()
        
    def main(self):
        Gtk.main()

x = Example()
x.main()
