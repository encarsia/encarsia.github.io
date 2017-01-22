.. title: Exterminate!
.. slug: exterminate
.. date: 2016-11-30 15:48:06 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**The VTE terminal widget**

.. thumbnail:: /images/11_terminal.png

Glade
-----

The widget can be found in the lower part of the widget side bar and provides a complete terminal emulator. To close the window on the ``exit`` command the *child-exited* signal has to be assigned.

A button click shall open a Python prompt within the terminal window, so we need the familiar *clicked* signal.

Python
------

Elements used in Glade that are not part of the *Gtk* module have to be registered as a *GObject* object (this is also required when using a *GtkSourceView* widget as the functionality is provided by the *GtkSource module):

.. code:: python

    GObject.type_register(Vte.Terminal)

The terminal emulator is initiated by calling ``spawn_sync`` expecting 7 parameters. Detailed information on the parameters are available in the `documentation <https://lazka.github.io/pgi-docs/#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync>`_ but for a common start a lot of defaults and Nones will do:

.. code-block:: python

    terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            None,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DEFAULT,
            None,
            None,
            )

The ``feed_child`` function must be called to send a command to the console. The expected parameters are the string including a newline and the length of the string:

.. code:: python

       command = "python\n"
       x.terminal.feed_child(command,len(command))

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 11_terminal.glade xml

Python
******

.. listing:: 11_terminal.py python
