.. title: Push the button
.. slug: push-the-button
.. date: 2016-11-02 23:56:07 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Buttons und Labels**

Glade
-----

Ausgehend vom `letzten Beispiel <link://slug/fenster-mit-aussicht>`_ werden nun ein paar Elemente hinzugefügt, ein Label, ein Button und ein Togglebutton. Jedes Anzeigen- oder Steuerungselement benötigt je ein Container. In diesem Beispiel werden vertikale Boxen angelegt, diese lassen sich jederzeit erweitern, es ist auch möglich, Container ineinander zu verschachteln.

Den Elementen Button und Togglebutton wird auf *clicked* bzw. *toggled* ein Signal zugewiesen. Label dient nur der Anzeige von Text, hier wird kein Signal benötigt.

In der Vorschauansicht kann man testen, ob die korrekte Reaktion ausgelöst wird.

.. thumbnail:: /images/02_gladepreview.png

Python
------

Ein Klick auf den Button soll in der Labelanzeige einen anderen Text anzeigen, hier wird zufällig ein Element aus einer Liste ausgewählt.

Alle *Gtk.Builder*-Objekte können über die Funktion ``get_object`` angesprochen werden:

.. code-block:: python

    Gtk.Builder.get_object("name").funktion(options)

    #Beispiel GtkLabel
    Gtk.Builder.get_object("label_name").set_text("neuer Text")

Der Togglebutton soll die Labelanzeige leeren und Button inaktivieren und bei erneutem Klick wieder freigeben.

Der Zustand des Togglebuttons kann mit der Funktion ``get_active()`` abgerufen werden (gibt True/False zurück).

Abhängig vom verwendeten Widget erfordert die Signal-Funktion mindestens einen Parameter.

.. code-block:: python

    def on_t_button_toggled(self,widget):
        if widget.get_active():
            #do something
        else:
            #do something different

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 02_labelbutton.glade xml

Python
******

.. listing:: 02_labelbutton.py python


