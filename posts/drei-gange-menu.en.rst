.. title: Serve the menu
.. slug: drei-gange-menu
.. date: 2016-11-07 22:10:09 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Menus, toolbars and statusbars**

Glade
-----

.. thumbnail:: /images/05_menutoolbar.png


Menu
****

The menu widget is part of the container widgets but itself needs an empty box to be placed in. There can be generated a standard menu that is easily edited after clicking on *"Edit..."* in a separate window.

Creating shortcuts is also simple. In the "Edit" window a click on *"Hierarchy > Properties > Accelerators"* opens a dialogue in which a shortcut is assigned to a signal (regarding menu items you want to assign *activate*).

Toolbar
*******

Toolbars contain different widgets like buttons, togglebuttons, radiobuttons oder (sub) menus. Generating and editing toolbars is analogue to menus.

Statusbar
*********

The purpose of statusbars is to show notifications or useful information. Messages are treated like a list, the statusbar widget provides the functions ``push`` and ``pop``.

Python
------

To send a message to the statusbar you will just need the function

.. code-block:: python

    widget.push(content_id,message)

If messages are exclusively shown "on top" the content_id can be a random number, like ``0``.

Listings
--------

Glade
*****
.. listing:: 05_menutoolbar.glade xml

Python
******

.. listing:: 05_menutoolbar.py python

