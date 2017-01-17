.. title: Push the button
.. slug: push-the-button
.. date: 2016-11-02 23:56:07 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Buttons and labels**

Glade
-----

Based on the `first example <link://slug/fenster-mit-aussicht>`_ some elements are added, a label, a button and a togglebutton. Any control or display widget requires a container. In this example a vertically arranged container box is created. Boxes can be extended, downsized, rearranged and contain further container widgets.

Now the *clicked* and *toggled* signal are assigned to the button and togglebutton element. The label widget's purpose ist to display text so there is no signal assignment required.

Glade provides a preview function to test if the correct reaction is triggered.

.. thumbnail:: /images/02_gladepreview.png

Python
------

On a button click the label widget should change the diplayed text randomly chosen from a given list.

All *GtkBuilder* elements can be addressed by the ``get_object`` function.

.. code-block:: python

    Gtk.Builder.get_object("name").function(options)

    #Beispiel GtkLabel
    Gtk.Builder.get_object("label_name").set_text("new text")

The task of the togglebutton is to clear the label widget display and deactivate the button which can be reactivated on the next click.

The status of togglebuttons can be retrieved by the ``get_active()`` function returning True or False.

Depending on the widget the corresponding signal function expects at least one parameter

.. code-block:: python

    def on_t_button_toggled(self,widget):
        if widget.get_active():
            #do something
        else:
            #do something different

Listings
--------

Glade
*****

.. listing:: 02_labelbutton.glade xml

Python
******

.. listing:: 02_labelbutton.py python
