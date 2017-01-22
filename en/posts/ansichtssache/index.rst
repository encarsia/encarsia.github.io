.. title: Data view
.. slug: ansichtssache
.. date: 2016-12-22 00:02:20 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Display TreeStore data**

(Continuation of the `ListStore article <link://slug/uberlistet>`_)

.. thumbnail:: /images/12_treestore.png
    :width: 480

TreeStore vs. ListStore
-----------------------

In contrast to ListStores TreeStore rows can possess child rows. That's why the ``append`` function requires another parameter that specifies the parent row reference:

.. code-block:: python

    #append row to liststore
    store.append([value1,value2,value3])
    
    #append row to treestore
    store.append(parent,[value1,value2,value3])

The *parent* value is either

* **None** if the current row is not a child row of another, or
* **TreeIter** pointing to the superordinate row.

The *TreeIter* value is generated when creating a row, subordinate rows are created by

.. code-block:: python

    row1 = store.append(None,[value1,value2,value3])
    row2 = store.append(row1,[value1,value2,value3])

The TreeIter of a cell is obtained by calling the ``get_selection`` function of the automatically generated *GtkTreeSelection* widget.

Glade
-----

In the example there are two TreeStores with some columns and the coresponding TreeView widgets to display the data columns.

TreeModelSort
*************

Sorting a column is set by calling ``set_sort_column_id``. If this is applied to the TreeStore all TreeView widgets using this store are equally sorted.

If this behaviour is not diesired *TreeModelSort* elements come into play and which are "interposed" between store and view widgets. First the TreeModelSort is created via *"Miscellaneous > Tree Model Sort"* from the widget sidebar. Then you choose a source TreeView to use data from. After that the model in the TreeView widget is replaced by the newly created TreeModelSort.

The sort function is now simply applied to the TreeModelSort object instead to the TreeView object.

TreeModelFilter
***************

*TreeModelFilter* allows to only show data that matches the specified filter criteria. Handling this object is analogue to TreeModelSort.

In the example the varieties can be filtered according to fruit colour so there is a *GtkButtonBox* required to put the corresponding buttons into.

Load formatting values from the model
*************************************

Besides the columns containing displayed data there is a "weight" column in the first TreeStore. This value is used to show the cell in bold text. It is realized by setting the CellRenderer's property of *"Font weight"* to the column containing the corresponding value (normal font is 400). In this way the appearance of cells can be defined, for example colours or font formating.

Python
------

TreeModelSort
*************

Requesting a position by calling ``GtkTreeSelection.get_selected()`` returns a tuple (model, pos), *pos* of *model* points to TreeModelSort (or TreeModelFilter) and requires conversion to the TreeStore position:

.. code-block:: python

    model,pos = selection.get_selected()
    converted_iter = treesort.convert_iter_to_child_iter(pos)
    store.set_value(converted_iter,column,value)

TreeModelFilter
***************

First of all a filter function is required defining the visibility of cells, in the example it's the variable *self.color*:

.. code-block:: python

    def color_filter_func(self,model,iter,data):
        if model[iter][2] == self.color:
            return True
        else:
            return False

This function has to be assigned to TreeFilter

.. code-block:: python

    treefilter.set_visible_func(filter_func)

A filter process is then executed by calling the ``refilter()`` function on the TreeFilter object:

.. code-block:: python

    def on_button_clicked(self,widget):
        x.color = widget.get_label()
        x.obj("treefilter").refilter()

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 12_treestore.glade xml

Python
******

.. listing:: 12_treestore.py python

