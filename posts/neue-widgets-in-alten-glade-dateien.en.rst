.. title: New widgets in old Glade files
.. slug: neue-widgets-in-alten-glade-dateien
.. date: 2017-10-25 10:12:09 UTC+02:00
.. tags: glade
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Problem: disabled widgets in older Glade files**

It may occur that certain widgets in Glade are greyed out after opened in Glade.

.. thumbnail:: /images/glade_widgetsinactive.png

A hint is hown in tooltips like

.. thumbnail:: /images/glade_widgetsinactive_tooltip.png

The cause for this behaviour is the Gtk+ version given at the beginning of the file:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated with glade 3.20.1 -->
    <interface>
      <requires lib="gtk+" version="3.0"/>
      ...

This line will not be altered even if the file is saved by a more recent Glade version.
So you just manually replace ``"3.0"`` by a current version (``"3.20"`` at present).
