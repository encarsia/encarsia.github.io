import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_cbox_changed(self,widget):
        iter,model = widget.get_active_iter(),widget.get_model()
        row = model[iter]
        print("Selection:",row[0])
    
    def on_cellrenderer_descr_edited(self,widget,pos,edit):
        x.store[int(pos)][1] = edit
    
    def on_add_row_button_clicked(self,widget):
        x.store.append(list(x.more_rows[len(x.store)-3]))
        #set button inactive when all rows are appended
        if len(x.store) == 7:
            x.button.set_sensitive(False)

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("09_liststore.glade")
        self.builder.connect_signals(Handler())

        window = self.builder.get_object("window")
        window.show_all()

        self.button = self.builder.get_object("add_row_button")
        self.store = self.builder.get_object("liststore")
        
        #print all values
        [print(row[:]) for row in self.store]

        self.more_rows = [("four","",5739),
                            ("five","",120),
                            ("six","",4),
                            ("seven","lucky number",7)]

    def main(self):
        Gtk.main()

x = Example()
x.main()
