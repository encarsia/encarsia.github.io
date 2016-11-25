import datetime
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_spin_m_wrapped(self,widget):
        if widget.get_value() == 1:
            x.spin_y.set_value(x.spin_y.get_value()+1)
        else:
            x.spin_y.set_value(x.spin_y.get_value()-1)

    def on_comboboxtext1_changed(self,widget):
        print("Auswahl ComboBox 1:",widget.get_active_text())

    def on_comboboxtext2_changed(self,widget):
        print("Auswahl ComboBox 2:",widget.get_active_text())

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("08_combospin.glade")
        self.builder.connect_signals(Handler())

        #set current values for month/year
        self.builder.get_object("spin_m").set_value(datetime.datetime.now().month)
        self.spin_y = self.builder.get_object("spin_y")
        self.spin_y.set_value(datetime.datetime.now().year)

        #set combobox list values
        [self.builder.get_object("comboboxtext2").append(None,entry) for entry in ("bla","blubb","ja","nein")]

        window = self.builder.get_object("window")
        window.show_all()

    def main(self):
        Gtk.main()

x = Example()
x.main()
