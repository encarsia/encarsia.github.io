#!/usr/bin/python
# -*- coding: utf-8 -*-

import gettext
import locale
import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

_ = gettext.gettext


class Handler:

    def on_window_destroy(self, *args):
        Gtk.main_quit()


class Example:
    
    def __init__(self):

        #setting up localization
        locales_dir = os.path.join(os.getcwd(),
                                    "10_localization",
                                    "locale",
                                    )
        appname = "TUT"

        #required for showing Glade file translations
        locale.bindtextdomain(appname, locales_dir)
        locale.textdomain(locales_dir)
        #required for code translations
        gettext.bindtextdomain(appname, locales_dir)
        gettext.textdomain(appname)

        self.builder = Gtk.Builder()
        self.builder.set_translation_domain(appname)

        self.builder.add_from_file("10_lokalisation.glade")
        self.builder.connect_signals(Handler())

        #translatable strings
        print(_("It's a trap!"))
        print(_("""These aren't the droids you're looking for.\n"""))

        #not translatable
        nonono = """\"Jar Jar is the key to all of this.\""""
        george = "...ruined it."
        print(nonono, george)

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()


x = Example()
x.main()
