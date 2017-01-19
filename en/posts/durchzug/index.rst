.. title: Open and close windows
.. slug: durchzug
.. date: 2016-11-03 23:40:03 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Open and close windows and dialogues**

Glade
-----

There can be created different types of windows and dialogs (which are subclasses of windows). In this example the main window has two buttons. The first one opens an info dialog, the second one closes the main window and opens another window instead.

.. thumbnail:: /images/03_changewindow.png

7 Signals are assigned:

- (per) window
    * "info" button (headerbar left): *clicked*
    * "ok" button (headerbar right): *clicked*
    * close/quit: *destroy*
- info dialog
    * close/quit: *destroy*

.. listing:: 03_changewindow.glade xml

Python
------

The most important functions needed for handling windows are

.. code-block:: python

    # open window
    Gtk.Builder.get_object("name").show_all()
    # close window temporarily, can be retrieved by show_all()
    Gtk.Builder.get_object("name").hide_on_delete()
    # close window, quit Gtk
    Gtk.main_quit()

Functions within the Handler() class of course can be assigned to multiple signals. So there are only 5 handler functions required in this example file.

The complete example code is:

.. listing:: 03_changewindow.py python

See also the `sequel article to dialogues <link://slug/dialoge>`_.