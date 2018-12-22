.. title: ListStore
.. slug: uberlistet
.. date: 2016-11-24 17:55:14 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Store data sets in ListStores and use ComboBox and TreeView to display the data**

There are a bunch of elements required to store and display tables of data in GTK+ applications:

1. The model to administrate data. There are two types:
    * *ListStore:* flat table, besides string and numerical values the rows also can be of GTK+ element type (like buttons or checkboxes), input of data sets in Glade possible
    * *TreeStore:* just like ListStore but rows can possess child rows, input of data sets in Glade is not possible (see also `TreeStore article <link://slug/ansichtssache>`_)

2. Widgets:
    * *TreeView:* show, sort and edit data; used by both store model types; a data store can be used my multiple TreeView widgets
    * *ComboBox:* comboboxes are used to limit input to given list items, this list can be stored in a List/TreeStore (see also `spinbutton and combobox article <link://slug/qual-der-wahl>`_)
    * *CellRenderers:* Subwidgets to specify source, layout and other properties (like being editable) of displayed data rows

.. thumbnail:: /images/09_treestore2.png

Glade
-----

ListStore
*********

In the example there is one ListStore created via *"Miscellaneous > List Store"* which will be later used by three Widgets.

First there are some rows created. ListStore data sets can be inserted in Glade but this in practise is only convenient for typing in few data sets.

Content changes in the ListStore are simultaneously updated in the Widgets using the ListStore. For individual sorting of the same List/TreeStore it is needed to create *Gtk.TreeModelSort* elements (this element is used in the example of the `TreeStore article <link://slug/ansichtssache>`_).

.. thumbnail:: /images/09_treestore1.png

Widgets
*******

ComboBox
    Creating the widget you are prompted to choose as "TreeView Model". In the edit mode accessible via *"Edit > Hierarchy"* there is created a CellRendererText. In the first field ("Text") the column to load the items of the dropdown menu from is set. To process the selection you will need the *changed* signal.

TreeView #1
    The first TreeView widget is placed within a *Gtk.ScrolledWindow* container. Like in a ComboBox there are created CellRenderers representing a column to show in the TreeView table. If the sort indicator is activated columns can be sorted on a column table click.
    Columns do not have to be sorted according to the columns they show.

TreeView #2
    The second TreeView widget is created within a *Gtk.ViewPort*.
    This container widget does not provide scroll bars but the automatically adapts the necessary size to display the whole content. So for larger tables you will need the *Gtk.ScrolledWindow*.
    The sort indicator is deactivated and the middle column ("Description") is made editible with the signal "edited" allocated.

Button
    The button's function is appending a row to the ListStore, so the *clicked* signal is required.

Python
------

TreeStore
*********

The ListStore's row can be iterated over via ``for row in store``. New rows are added by ``append``, other options are ``insert`` or ``remove`` to add or delete rows at specific positions.

ComboBox
********

For accessing a data row you need a *Gtk.TreeIter* object which points to the position in the model (this can also be achieved by a *Gtk.TreePath* object).

.. code-block:: python

    iter,model = widget.get_active_iter(),widget.get_model()
    row = model[iter]
    print("Selection:",row[0])

Edit cells
**********

The *edited* signal passes the position and content of the edited cell. The new content of the *CellRendererText* has to explicitly be committed to the data store otherwise the content will return to the pre edit state. This can be accomplished by using the passed *TreePath* position.

.. code-block:: python

    def on_cellrenderer_descr_edited(self,widget,pos,edit):
        x.store[int(pos)][1] = edit

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 09_liststore.glade xml

Python
******

.. listing:: 09_liststore.py python
