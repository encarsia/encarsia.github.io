#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import setproctitle

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GLib


class ExampleApp:

    def __init__(self):
        
        setproctitle.setproctitle("Application test")
        GLib.set_prgname("Application test") 
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        
        self.app.add_main_option_entries([
            self.create_option_entry("--version",
                                     description="Show version numbers and exit",
                                    ),
            self.create_option_entry("--setlabel",
                                     description="Set label widget",
                                     arg=GLib.OptionArg.STRING,
                                    ),
            self.create_option_entry("--bollocks",
                                     description="Additional test option - exit",
                                    ),
        ])

        self.app.connect("handle-local-options", self.on_local_option)
        self.app.connect("activate", self.on_app_activate)

    def on_local_option(self, app, option):
        self.option_string = ""
        if option.contains("version"):
            var = GLib.VariantDict.end(option)
            print("Python: {}".format(sys.version[:5]))
            print("GTK+:   {}.{}.{}".format(Gtk.MAJOR_VERSION,
                                             Gtk.MINOR_VERSION,
                                             Gtk.MICRO_VERSION,
                                             ))
            return 0
        elif option.contains("bollocks"):
            return 1
        elif option.contains("setlabel"):
            var = GLib.VariantDict.end(option)
            self.option_string = var[var.keys()[0]]
        return -1

    def create_option_entry(self,
                            long_name,
                            short_name=None,
                            flags=0,
                            arg=GLib.OptionArg.NONE,
                            arg_data=None,
                            description=None,
                            arg_description=None,
                            ):
        option = GLib.OptionEntry()
        option.long_name = long_name.lstrip("-")
        option.short_name = 0 if not short_name else ord(short_name.lstrip("-"))
        option.flags = flags
        option.arg = arg
        option.arg_data = arg_data
        option.description = description
        option.arg_description = arg_description
        return option

    def on_app_activate(self, app):
        builder = Gtk.Builder()
        builder.add_from_file("15_application.glade")

        self.obj = builder.get_object
        self.obj("window").set_application(app)
        self.obj("label").set_text(self.option_string)

        # display application name in upper panel of the GNOME Shell
        # function is deprecated but still works as fallback
        self.obj("window").set_wmclass("Application test", "Application test")
        self.obj("window").show_all()

    def run(self, argv):
        self.app.run(argv)


app = ExampleApp()
app.run(sys.argv)
