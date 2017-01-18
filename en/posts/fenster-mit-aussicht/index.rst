.. title: View from the window
.. slug: fenster-mit-aussicht
.. date: 2016-11-02 17:14:04 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Minimal example**

Glade
-----

After launching Glade the application view is divided in 3 areas: window/widget selection on the left, the project view in the centre and a tree/property (including signal) view of project elements on the right.

Now a window is created and an ID assigned to be able to address the element in the source code.

.. thumbnail:: /images/01_glade.png

.. TEASER_END

To call functions from widgets they have to be connected to signals. Depending on the kind of graphical object signals can be emitted by clicking, marking, editing, switching etc.

If the example window should be able to be closed on clicking the [X] button the signal *destroy* is required. The entry field to specify the function provides a convenient suggestion function to reduce key input following the pattern ``on_id_signal``.

.. thumbnail:: /images/01_destroysignal.png

Glade does not generate GTK+ source code but a XML formatted file accessible to *GtkBuilder* (see listing below).

Python
------

First things first. *GtkBuilder* is provided by the *Gtk* module from the Python GObject Introspection bindings:

.. code-block:: python

    import gi
    gi.require_version('Gtk','3.0')
    from gi.repository import Gtk

After initing ``Gtk.Builder()`` the Glade file(s) are added.

.. code-block:: python

        builder.add_from_file(gladefile)

It may be convenient to work with multiple files in one project. In this case you have to bear in mind that if there are elements with the same identifier name only the element of the last loaded file can be addressed by ``get_object(id)``.

Second step is connecting the signals. It comes in handy to store these functions in an own class:

.. code-block:: python

    self.builder.connect_signals(Handler())

So this basic example script opens an empty window hat can be closed on clicking the close button.

Ohne Glade
----------

This example corresponds to the basic example of the `Python GTK+ 3 tutorial <http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html>`_:

.. code-block:: python

    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

The definded window does not contain any elements like boxes, buttons, bars, menus and other widgets.

Listings
--------

Glade
*****

.. listing:: 01_minimal.glade xml

Python
******

.. listing:: 01_minimal.py python






