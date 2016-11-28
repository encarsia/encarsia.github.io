.. title: Alles so schön bunt hier
.. slug: css
.. date: 2016-11-08 16:22:40 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Schöner klicken mit Cascading Stylesheets**

CSS
---

GTK+-Objekte lassen sich mit Hilfe von CSS im Layout verändern. Meiner unmaßgeblichen Ansicht nach sollte man es damit allerdings nicht übertreiben und das grundlegende Erscheinungsbild dem eingestellten Theme überlassen. Links:

* `GTK, Python and CSS are an awesome combo <http://wolfvollprecht.de/blog/gtk-python-and-css-are-an-awesome-combo/>`_ - Grundlagen mit Beispiel
* `Overview of CSS in GTK+ <https://developer.gnome.org/gtk3/stable/chap-css-overview.html>`_ - ausführliche Übersicht mit vielen Beispielen
* `A GTK+ update <https://blogs.gnome.org/mclasen/2015/11/20/a-gtk-update/>`_ - Neuerungen seit GTK+ 3.20

Glade
-----

.. thumbnail:: /images/07_css.png

Mit Glade werden nur die Fenster/Widgets angelegt, in diesem Beispiel vier Levelbars mit Werten, die CSS-Layout-Anweisungen erfolgen dann im Code.

.. TEASER_END

.. listing:: 07_css.glade xml

Python
------

CSS
***

Layout-Anweisungen erfolgen nach dem Muster

.. code-block::

    widget [element] {
      font...
      color...
      background...
      ...
    }

innerhalb einer String-Variblen, die von der Klasse ``Gtk.CssProvider()`` geladen werden.

Levelbar
********

Levelbars können, wie bereits im Artikel `"Bars" <link://slug/bars>`_  angedeutet, in definierten Wertebereichen unterschiedliche Farben annehmen (um zum Beispiel einen kritischen Ladezustand zu visualisieren). Die vordefinierten Offset-Marker dafür sind:

        * ``low`` (<=.25)
        * ``high`` (<=.75)
        * ``full`` (bis 1)

Die Werte können mit den Funktionen ``get_offset_value`` abgefragt bzw. mit ``add_offset_value`` angelegt oder verändert werden.

Im Beispiel wird der unteren Levelbar ein zusätzlicher Offsetmarker zwischen ``high`` und ``full`` angelegt, deshalb wird beim Wert von 0.8 dort im Gegensatz zur dritten Levelbar nicht der Marker für ``full`` ereicht.

.. listing:: 07_css.py python
