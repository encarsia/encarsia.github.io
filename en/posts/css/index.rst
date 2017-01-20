.. title: Jumping off the greyscale
.. slug: css
.. date: 2016-11-08 16:22:40 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Pimp GUI using Cascading Style Sheets**

CSS
---

GTK+ objects' layouts can be altered by using CSS. In my humble opinion the usage should not be exaggerated and the main part of the layout should be left to be managed by the theme. Links:

* `GTK, Python and CSS are an awesome combo <http://wolfvollprecht.de/blog/gtk-python-and-css-are-an-awesome-combo/>`_ 
* `Overview of CSS in GTK+ <https://developer.gnome.org/gtk3/stable/chap-css-overview.html>`_ 
* `A GTK+ update <https://blogs.gnome.org/mclasen/2015/11/20/a-gtk-update/>`_ - Changes since GTK+ 3.20

Glade
-----

.. thumbnail:: /images/07_css.png

CSS layout instructions are set in the source code. This example shows the usage of CSS in levelbars so 4 of them are created with Glade.

Python
------

CSS
***

The pattern for layout instructions is

.. code-block::

    widget [element] {
      font...
      color...
      background...
      ...
    }

that are stored in a string variable loaded by the ``Gtk.CssProvider()`` class.

Levelbar
********

Levelbar values can be displayed in different colours depending on the defined value range (see article `"Bars" <link://slug/bars>`_), p.e. to visualize a critical battery status. The predefined offset markers are:

        * ``low`` (<=.25)
        * ``high`` (<=.75)
        * ``full`` (bis 1)

The values can be retrieved by the ``get_offset_value`` function or created/changed with the ``add_offset_value`` function.

In the example the 4th levelbar has an additional offset marker between ``high`` and ``full`` that's why a value of 0.8 is not visualized as ``full`` like it is in the 3rd levelbar.

.. code-block:: python

        self.bar.add_offset_value("alert",.9)

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 07_css.glade xml

Python
******

.. listing:: 07_css.py python
