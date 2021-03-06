.. title: Exterminate!
.. slug: exterminate
.. date: 2016-11-30 15:48:06 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Das VTE-Terminal-Widget**

.. thumbnail:: /images/11_terminal.png

Glade
-----

Das Widget findet man in der Widget-Seitenleiste ganz unten und stellt ein fertiges Terminal bereit. Um das Terminal auf ``exit`` zu schließen, muss das Signal *child-exited* abgefangen werden.

Ein Klick auf den Button soll innerhalb dieses Terminals eine Python-Konsole starten, hier wird also das *clicked*-Signal belegt.

Python
------

Elemente außerhalb des *Gtk*-Moduls, die mit Glade verwendet werden, müssen als *GObject*-Typ registriert werden (dies betrifft beispielsweise auch das `GtkSource.View-Widget <link://slug/gtksv>`_ (Modul *GtkSource*):

.. code:: python

    GObject.type_register(Vte.Terminal)

Das Terminal wird mit der Funktion ``spawn_sync`` initiiert, die diverse Parameter erwartet. Die `Dokumentation <https://lazka.github.io/pgi-docs/#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync>`_ liefert Details, für eine einfache Bash kommt man mit viel Defaults und Nones aus:

.. code-block:: python

    terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            None,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DEFAULT,
            )

Um eine Eingabe an die Konsole zu schicken, bedarf es der Funktion ``feed_child``. Als Parameter muss der auszuführende Befehl als UTF-8-kodierter String inklusive *newline*, also dem "Enter" übergeben werden:

.. code:: python

       command = "python\n"
       x.terminal.feed_child(command.encode())

Die Ausgabe ins Terminal kann mit der Funktion ``get_text()`` abgefangen werden. Die Funktion gibt ein Tupel zurück, dessen erstes Element der Ausgabestring ist. Dieser enthält allerdings den gesamten Terminalinhalt, also auch viele Leerzeilen, die sich mit herkömmlichen String-Operationen beseitigen lassen.

.. code:: python

    widget.get_text()[0].rstrip()

.. TEASER_END

Listings
--------

Python
******

.. listing:: 11_terminal.py python

Glade
*****

.. listing:: 11_terminal.glade xml
