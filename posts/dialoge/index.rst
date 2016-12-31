.. title: Dialoge
.. slug: dialoge
.. date: 2016-12-31 17:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Anzeige von Dialogfenstern**

Dialoge sind ergänzende Fenster zur Anwendung und dienen der Interaktion mit dem Benutzer, in denen Informationen angezeigt werden oder Eingaben vom Benutzer abgefragt werden können. Die *Gtk.Dialog*-Klasse bietet einige Unterklassen für gebräuchliche Anzeigen und Abfragen, wie die im Beispiel verwendeten *About*- und *MessageDialog*.

.. thumbnail:: /images/13_dialoge.png

.. TEASER_END

Glade
-----

Dialog-Widgets findet man unter "Oberste Ebene" neben den Fenster-Widgets. 

AboutDialog
***********

Das "About"-Dialogfenster bietet in der Regel Informationen zum Projekt, darunter Version, Lizenz, beteiligte Programmierer, Übersetzer etc. Dies alles lässt sich sehr einfach direkt in Glade angeben.

MessageDialog
*************

Der MessageDialog ist ein Standarddialog zum Anzeigen oder Abfragen von Informationen. Er ist so konfiguriert, dass er keine eigene Fensterdekoration besitzt und nicht als Fenster in der Taskbar erscheint. Außerdem bietet er die Möglichkeit, Standardbuttons einzurichten.

Buttons und Responses
*********************

Dialoge besitzen bereits intern über eine *GtkButtonBox*, die mit beliebigen Buttons befüllt werden kann.

Im Gegensatz zu Buttons in normalen Fenstern müssen in Dialogen keine Signale auf *clicked* angelegt werden, sondern man legt in den Button-Eigenschaften unter "Allgemein" eine Antwortkennung (Response) fest (int) und belegt das Signal *response* des GtkDialog.

Standardbuttons wie im MessageDialog auswählbar besitzen eine vorgegebene Response:

 * **Ok** -5
 * **Abbrechen** -6
 * **Schließen** -7
 * **Ja** -8
 * **Nein** -9
 * **[X]** -4

Der große Vorteil der Responses besteht darin, dass sie sich direkt auf das Dialog-Objekt beziehen; man kann die Responses in einer Funktion verarbeiten und muss dies nicht für jeden einzelnen Button vornehmen.

Wiederherstellbare Dialoge
**************************

Das Problem von per *destroy*-Signal geschlossenen Fenstern besteht darin, dass sie sich nicht wieder aufrufen lassen. Deshalb wird stattdessen das Signal *delete-event* belegt.


Python
------

Responses
*********

Beim Auslösen des *response*-Signals wird die Antwortkennung als Parameter übergeben, so kann wie bereits erwähnt jede innerhalb einer einzelnen Funktion verarbeitet werden:

.. code-block:: python

    def on_dialog_response(self,widget,response):
        if response == 0:
            widget.hide_on_delete()
        elif response == 1:
            do.something()
        elif response == (2 or 3):
            do.something.different()

Delete-event
************

Mit der Funktion ``hide_on_delete()`` ausgeblendete Dialoge oder reguläre Fenster lassen sich mit ``show_all()`` wieder anzeigen:

.. code-block:: python

    def on_dialog_delete_event(self,widget,event):
        widget.hide_on_delete()
        return True

Listings
--------


Glade
*****

.. listing:: 13_dialoge.glade xml

Python
******

.. listing:: 13_dialoge.py python


