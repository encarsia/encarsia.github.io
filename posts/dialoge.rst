.. title: Dialoge
.. slug: dialoge
.. date: 2016-12-31 17:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Anzeige von Dialogfenstern**

Dialoge sind ergänzende Fenster zur Anwendung und dienen der Interaktion mit dem Benutzer, in denen Informationen angezeigt werden oder Eingaben vom Benutzer abgefragt werden können. Die *GtkDialog*-Klasse bietet einige Unterklassen für gebräuchliche Anzeigen und Abfragen, wie die im Beispiel verwendeten *AboutDialog*- und *MessageDialog* (`Artikel zum FileChooserDialog <link://slug/fcdialog>`_).

.. thumbnail:: /images/13_dialoge.png

Glade
-----

Dialog-Widgets findet man unter *"Oberste Ebene"* neben den Fenster-Widgets.

Dialoge sind ergänzende Fenster, um den Fokus des Nutzers zu lenken. Sie können direkt an ein übergeordnetes Fenster angeheftet werden, mindestens aber müssen sie unter *"Allgemein > Fensterattribute > Vorübergehend für:"* einem Eltern-Fenster zugeordnet werden. Sie erscheinen dadurch nicht als separates Fenster in der Übersicht und erben ein vorhandenes Icon.

AboutDialog
***********

Das "About"-Dialogfenster bietet in der Regel Informationen zum Projekt, darunter Version, Lizenz, beteiligte Programmierer, Übersetzer etc. Dies alles lässt sich sehr einfach direkt in Glade angeben.

MessageDialog
*************

Der MessageDialog ist ein Standarddialog zum Anzeigen oder Abfragen von Informationen. Er ist so konfiguriert, dass er keine eigene Fensterdekoration besitzt und nicht als Fenster in der Taskbar erscheint. Außerdem bietet er die Möglichkeit, Standardbuttons einzurichten.

Buttons und Responses
*********************

Dialoge verfügen bereits intern über eine *GtkButtonBox*, die mit beliebigen Buttons befüllt werden kann. Dieser Bereich ist als "intern action_area" gekennzeichnet.

Im Gegensatz zu Buttons in normalen Fenstern müssen in Dialogen keine Signale auf *clicked* angelegt werden, sondern man legt in den Button-Eigenschaften unter *"Allgemein"* eine Antwortkennung (Response) fest (int) und belegt das Signal *response* des *GtkDialog*.

Standardbuttons wie im MessageDialog auswählbar besitzen vorgegebene Response-Kennungen (siehe `Python GI API Reference <https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.ResponseType>`_):

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

Dialog aufrufen
***************

Da Dialoge auch *Gtk.Windows* sind, lassen sie sich mit ``show_all()`` aufrufen. Die Funktion von Dialogen besteht allerdings in der Regel darin, Nutzereingaben zu erfassen oder Informationen zu vermitteln. Deshalb ruft man die Fenster am besten mit ``run()`` auf. Dies bewirkt, dass das Dialogfenster über dem Elternfenster fixiert wird und jenes nicht aktiv ist, bis ein Response-Signal ausgeführt wird.

Responses
*********

Beim Auslösen des *response*-Signals wird die Antwortkennung als Parameter übergeben, so kann, wie bereits erwähnt, jede Kennung innerhalb einer einzelnen Funktion verarbeitet werden:

.. code-block:: python

    def on_dialog_response(self, widget, response):
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

    def on_dialog_delete_event(self, widget, event):
        widget.hide_on_delete()
        return True

Mehrere Glade-Dateien
*********************

Wie `bereits erwähnt <link://slug/fenster-mit-aussicht>`_, können mehrere Dateien für Fenster und Dialoge innerhalb eines Projektes verwendet werden. Allerdings ist es nicht möglich, diese dateiübergreifend aneinanderzubinden. Hierzu wird die ``set_transient_for``-Funktion von *GtkWindow* benötigt:

.. code-block:: python

    dialog.set_transient_for(mainwindow)

Die Zugehörigkeit zum Elternwidget wird in Glade in den Eigenschaften unter *"Allgemein > Vorübergehend für:"* angegeben.

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 13_dialoge.glade xml

Python
******

.. listing:: 13_dialoge.py python
