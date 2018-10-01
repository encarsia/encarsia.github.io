.. title: Widget-Änderungen in GTK+ 2.20+
.. slug: gtk220neu
.. date: 2018-09-23 13:29:06 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text
.. status: draft

**Auch wenn die Entwicklung von GTK+ 4 weit fortgeschritten ist, gibt es immer noch Änderungen in der 3er Version**

Das GUI-Programm Glade_ wurde erst `kürzlich modernisiert <link://slug/glade-322>`_, in der Anwendung von Widgets sind mir einieg Neuerungen aufgefallen. Dies fällt in der Regel durch entsprechende *DeprecationWarnings* in der Konsole auf, die Programme selbst funktionieren noch wie gewünscht.

.. _Glade: https://glade.gnome.org/

Das heißt, die Artikel der `Tutorial-Reihe <link://slug/tutorial-reihe-glade>`_ bleiben vorerst unverändert (über eine gute Lösung muss ich noch nachdenken).

Es folgt eine nicht auf Vollständigkeit ausgelegte Liste der Änderungen:

set_wm_class
************

    **Alt:** ``Gtk.Window.set_wmclass(args)``

    **Neu:** keine, Funktion nicht mehr verwenden

new_from_stock
**************

    **Alt:** ``Gtk.Button.new_from_stock(Gtk.STOCK_OK)``

    **Neu:** ``Gtk.Button.new_with_label("OK")``

Labels bekommen nur noch eine Bezeichnung durch einen String, in der Dokumentation

Gtk.Image.new_from_stock(Gtk.STOCK_YES, 1)

gilt auch für ToggleButton



new_with_label
**************

Bei der Initialisierung von Labels enthaltene Widgets, z.B. *Gtk.MenuItem*

    **Alt:** ``Gtk.MenuItem("label")``
    
    **Neu:** ``Gtk.MenuItem.new_with_label("label")``

set_alignment
*************

    **Alt:** ``Gtk.Misc.set_alignment(x, y)``, z.B. bei Labels
    
    **Neu:** *Gtk.Widget*-Alignment* ``:halign`` und ``:valign`` verwenden

Vte-Terminal
************

    **Alt:** ``Vte.Terminal.spawn_sync(args)``

    **Neu:** GLib.spawn_async oder Vte.Pty.spawn_async (Details unbekannt)


