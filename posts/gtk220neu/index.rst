.. title: Widget-Änderungen in GTK+ 2.20+
.. slug: gtk220neu
.. date: 2018-10-04 13:29:06 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Auch wenn die Entwicklung von GTK+ 4 weit fortgeschritten ist, gibt es immer noch Änderungen in der 3er Version**

Das GUI-Programm Glade_ wurde erst `kürzlich modernisiert <link://slug/glade-322>`_, in der Anwendung von Widgets sind mir einige Neuerungen aufgefallen. Dies fällt in der Regel durch entsprechende *DeprecationWarnings* in der Konsole auf, die Programme selbst funktionieren noch wie gewünscht.

.. _Glade: https://glade.gnome.org/

Das heißt, die Artikel der `Tutorial-Reihe <link://slug/tutorial-reihe-glade>`_ bleiben vorerst unverändert (über eine gute Lösung muss ich noch nachdenken).

Es folgt eine nicht auf Vollständigkeit ausgelegte und bei Bedarf ergänzte Liste der Änderungen:

set_wm_class
************

Programmname in Panel und Dock anzeigen

    **Alt:** ``Gtk.Window.set_wmclass(wmclass_name, wmclass_class)``

    **Neu:** ``GLib.set_prgname(wmclass_name)`` (in .desktop-Datei ``StartupWMClass=wmclass_name`` erforderlich)

widget.new_from_stock
*********************

    **Alt:** ``Gtk.Button.new_from_stock(Gtk.STOCK_OK)``

    **Neu:** ``Gtk.Button.new_with_label("OK")``

Labels bekommen nur noch eine Bezeichnung durch einen String.

Gilt auch für *ToggleButton* und *Image* (hier: image.new_from_icon_name() verwenden)


menuitem.new_with_label
***********************

Bei der Initialisierung von Labels enthaltene Widgets, z.B. *Gtk.MenuItem*

    **Alt:** ``Gtk.MenuItem("label")``
    
    **Neu:** ``Gtk.MenuItem.new_with_label("label")``

set_alignment
*************

    **Alt:** ``Gtk.Misc.set_alignment(x, y)``, z.B. bei Labels
    
    **Neu:** *Gtk.Widget*-Alignment ``:halign`` und ``:valign`` verwenden

Vte-Terminal
************

Befehl übergeben
================

    **Alt:** ``Vte.Terminal.feed_child(cmd, len(cmd))`` (cmd ist das zu übergebene Kommando)

    **Neu:** ``Vte.Terminal.feed_child(cmd.encode())`` (seit v2.91)


Start
=====

    **Alt:** ``Vte.Terminal.spawn_sync(args)``

    **Neu:** GLib.spawn_async oder Vte.Pty.spawn_async (Details unbekannt)

FileChooserDialog
*****************

    **Alt:**

.. code:: python

    dialog = Gtk.FileChooserDialog("Choose a folder",
                                    app.obj("window"),
                                    Gtk.FileChooserAction.SELECT_FOLDER,
                                    (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                    Gtk.STOCK_APPLY, Gtk.ResponseType.OK))

'

    **Neu:** Argumente werden namentlich übergeben, Buttons separat hinzugefügt:

.. code:: python

        dialog = Gtk.FileChooserDialog(title="Choose a folder",
                                       parent=app.obj("window"),
                                       action=Gtk.FileChooserAction.SELECT_FOLDER,
                                       )
        dialog.add_buttons("Cancel", Gtk.ResponseType.CANCEL,
                           "OK", Gtk.ResponseType.OK)
