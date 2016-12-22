import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Handler:

    def on_window_destroy(self,*args):
        Gtk.main_quit()

    def on_button_clicked(self,widget):
        x.color = widget.get_label()
        x.obj("treefilter").refilter()

    def on_cellrenderer_note_edited(self,widget,row,edit):
        model,pos = x.obj("selection").get_selected()
        conv_iter = x.obj("treesort").convert_iter_to_child_iter(pos)
        x.obj("store").set_value(conv_iter,3,edit)

class Example:
    
    def __init__(self):
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("12_treestore.glade")
        self.builder.connect_signals(Handler())
        self.obj = self.builder.get_object

        #read data from text file
        with open("12_capsicum.txt") as f:
            data = [line.strip("\n") for line in f]

        colors = set()
        species = set()
        varieties = []
        for line in data:
            variety = line.split(";")
            colors.add(variety[2])
            species.add(variety[1])
            try:
                variety[3]
            except IndexError:
                variety.append("")
            varieties.append(variety)

        #append lines to 1st treestore
        for s in species:
            counter = 0
            row = self.obj("store").append(None,[None,None,None,None,800,None])
            for v in varieties:
                if v[1] == s:
                    self.obj("store").append(row,[v[0],v[1],v[2],v[3],400,None])
                    counter += 1
            self.obj("store").set_value(row,0,"%s (%d)" % (s,counter))
            self.obj("store").set_value(row,5,counter)

        #append lines to 2nd treestore
        [self.obj("filterstore").append(None,[v[0],v[1],v[2]]) for v in varieties]
        
        #create buttons in buttonbox
        for c in colors:
            button = Gtk.Button.new_with_label(c)
            button.connect("clicked",Handler().on_button_clicked)
            self.obj("buttonbox").add(button)

        self.obj("view").expand_all()
        self.obj("treesort").set_sort_column_id(5, Gtk.SortType.DESCENDING)
        self.obj("treefilter").set_visible_func(self.color_filter_func)
        self.obj("window").show_all()

    def color_filter_func(self,model,iter,data):
        if model[iter][2] == self.color:
            return True
        else:
            return False

    def main(self):
        Gtk.main()

x = Example()
x.main()
