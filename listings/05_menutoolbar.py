import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_info_button_clicked(self,widget):
        x.sb_message("Öffne Info-Dialog")
        x.builder.get_object("about_dialog").show_all()

    def on_close_button_clicked(self,widget):
        x.sb_message("Schließe Info-Dialog")
        x.builder.get_object("about_dialog").hide_on_delete()

    def on_nothing_here(self,widget):
        x.sb_message("%s: Widget hat keine Funktion." % widget)

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("05_menutoolbar.glade")
        self.builder.connect_signals(Handler())

        window = self.builder.get_object("window")
        window.show_all()

    def sb_message(self,message):
        self.builder.get_object("statusbar").push(0,message)

    def main(self):
        Gtk.main()

x = Example()
x.main()
