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

**Das VTE-Terminal-Widget**

.. thumbnail:: /images/11_terminal.png

.. TEASER_END

Glade
-----

Das Widget findet man in der Widget-Seitenleiste ganz unten und stellt ein fertiges Terminal bereit. Um das Terminal auf ``exit`` zu schließen, muss das Signal *child-exited* abgefangen werden.

Ein Klick auf den Button soll innerhalb dieses Terminals eine Python-Konsole starten, hier wird also das *clicked*-Signal belegt.

.. listing:: 11_terminal.glade xml

Python
------

Elemente außerhalb des Gtk-Moduls, die Glade verwendet werden, müssen als GObject-Typ registriert werden (dies betrifft beispielsweise auch das GtkSourceView-Widget (Modul GtkSource):

.. code:: python

    GObject.type_register(Vte.Terminal)

Das Terminal wird mit der Funktion ``spawn_sync`` initiiert, die ganze 7 Parameter erwartet. Die `Dokumentation <https://lazka.github.io/pgi-docs/#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync>`_ liefert Details, für eine einfache Bash kommt man mit viel Defaults und Nones aus:

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

Um eine Eingabe an die Konsole zu schicken, bedarf es der Funktion ``feed_child``. Als Parameter müssen übergeben werden zum einen der String (inklusive *newline*, um einen Befehl auszuführen) und die Länge des Strings:

.. code:: python

       command = "python\n"
       x.terminal.feed_child(command,len(command))

.. listing:: 11_terminal.py python


