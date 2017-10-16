#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib.request

import gi
gi.require_version('Gtk','3.0')
gi.require_version('Vte', '2.91')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, Gio, Vte, GObject, GLib, WebKit2

class Handler:
    
    def on_term_child_exited(self, widget, event):
        #reset and setup terminal on exit command
        widget.reset(True, True)
        app.stack_console()

    def on_home_button_clicked(self, widget):
        #reload given URL in current tab
        page = app.obj("notebook").get_current_page()
        app.nbtabs[page][2].load_uri(app.nbtabs[page][1])
        
class ExampleApp:

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.connect("activate", self.on_app_activate)

    def on_app_activate(self, app):
        GObject.type_register(Vte.Terminal)
        builder = Gtk.Builder()
        builder.add_from_file("21_stacknotebook.glade")
        builder.connect_signals(Handler())
        self.obj = builder.get_object
        self.obj("window").set_application(app)
        self.obj("window").set_wmclass("Tutorial application","Tutorial application")
        self.obj("window").show_all()
        
        #get window content
        self.stack_image()
        self.stack_console()
        self.stack_notebook()

    def run(self, argv):
        self.app.run(argv)

    def stack_image(self):
        #download and show NASA Astonomy Picture of the Day
        URL = "https://apod.nasa.gov"
        source = urllib.request.urlopen(URL).read().decode("utf-8")
        img_start = source.find("<IMG SRC=")
        img_end = source.find("alt=")
        img = source[img_start+10:img_end-2]
        IMGURL = "https://apod.nasa.gov/apod/"+img
        #urllib.request.urlretrieve(IMGURL, "apod.jpg")
        self.obj("image").set_from_file("apod.jpg")

    def stack_console(self):
        #setup terminal
        self.obj("term").spawn_sync(
            Vte.PtyFlags.DEFAULT,
            None,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DEFAULT,
            None,
            None,
            )

    def stack_notebook(self):
        
        self.nbtabs = [
                    ["gi_doc", "https://lazka.github.io/pgi-docs/"],
                    ["gtk_tut", "http://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html"],
                    ["glade_tut", "https://encarsia.github.io/posts/tutorial-reihe-glade/"]
                    ]
        
        for tab in self.nbtabs:
            webview = WebKit2.WebView()
            tab.append(webview)
            webview.load_uri(tab[1])
            self.obj(tab[0]).add(webview)
            webview.show()

app = ExampleApp()
app.run(sys.argv)
