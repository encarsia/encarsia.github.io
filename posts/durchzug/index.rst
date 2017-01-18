.. title: Durchzug
.. slug: durchzug
.. date: 2016-11-03 23:40:03 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Fenster und Dialoge öffnen und schließen**

Glade
-----

Mit Glade lassen sich verschiedene Fensterarten und Dialoge erstellen. Im Beispiel hat das Hauptfenster zwei Buttons, ein Button öffnet ein Info-Fenster, der andere schließt das Hauptfenster und öffnet ein anderes Fenster, das jeweils das gleiche tut.

.. thumbnail:: /images/03_changewindow.png

.. TEASER_END

Es werden insgesamt 7 Signale angelegt:

- Fenster, jeweils
    * Info-Button (Headerbar links): *clicked*
    * Wechsel-/"Ok"-Button (Headerbar rechts): *clicked*
    * Schließen/Beenden: *destroy*
- Info-Dialog
    * Schließen-Button: *destroy*

.. listing:: 03_changewindow.glade xml

Python
------

Die entscheidenden Funktionen in der Handhabung von Fenstern sind

.. code-block:: python

    #Fenster anzeigen
    Gtk.Builder.get_object("name").show_all()
    #Fenster ausblenden, kann mit show_all() reaktiviert werden
    Gtk.Builder.get_object("name").hide_on_delete()
    #Fenster schließen, Gtk wird dabei beendet
    Gtk.main_quit()

Die Buttons zum Öffnen des Info-Dialogs und zum Beenden des Programms führen die jeweils identische Funktion aus; es werden demzufolge nur 5 Funktionen in der Handler-Klasse benötigt.

Das vollständige Beispiel ist dann:

.. listing:: 03_changewindow.py python

Siehe auch `Fortsetzung-Artikel zu Dialogen <link://slug/dialoge>`_.
