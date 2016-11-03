.. title: Durchzug oder Mehr als ein Fenster
.. slug: durchzug-oder-mehr-als-ein-fenster
.. date: 2016-11-03 13:40:03 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Fenster und Dialoge**

Glade
-----

Mit Glade lassen sich verschiedene Fensterarten und Dialoge erstellen. Im Beispiel hat das Hauptfenster zwei Buttons, ein Button öffnet ein Info-Fenster, der andere schließt es und öffnet ein anderes Fenster, das jeweils das gleiche tut.

.. thumbnail:: /images/03_changewindow.png

.. listing:: 03_changewindow.glade xml

Es werden insgesamt 7 Signale angelegt:

- Fenster, jeweils
    * Info-Button (Headerbar links)
    * Wechsel-/"Ok"-Button (Headerbar rechts)
    * Schließen/Beenden (*destroy*)
- Info-Dialog
    * Schließen-Button

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