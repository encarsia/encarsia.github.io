.. title: Clickbaiting
.. slug: clickbaiting
.. date: 2016-11-05 16:01:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Switch, Checkbox, Radiobutton - mehr Elemente zum Anklicken**

In diesem Artikel wird exemplarisch die Verwendung von Switches, Checkboxen und Radiobuttons vorgestellt. Folgend werden weitere Steuerungs- und Anzeigenelemente verwendet, es wird aber kein Anspruch auf Vollständigkeit erhoben, da die Verwendungsprozedur praktisch nach folgendem Schema funktioniert:

1. Container (Box, Leiste etc.) für Element anlegen

2. Element hinzufügen

3. Element mit einer Bezeichnung versehen (bei Elementen ohne Interaktion wie Boxen oder Trennlinien kann darauf verzichtet werden)

4. gewünschtem Signal eine Funktion zuweisen

5. (optional) Signal-/Funktionsaufruf in der Vorschaufunktion testen

6. Funktion im Programmcode schreiben

Alle verfügbaren GTK+-Klassen und ihre Funktionen findet man unter `Python GI API Reference >> Gtk 3.0 >> Classes <http://lazka.github.io/pgi-docs/#Gtk-3.0/classes>`_.

.. thumbnail:: /images/04_clickableelements.png

Glade
-----

Switch oder Schalter
********************

Ein Switch ist ein einfacher Ein-/Aus-Schalter mit, Überraschung!, zwei Zuständen. Der Zustand lässt sich über das Signal *state_set* abrufen.

Checkbox
********

Checkboxen sind Togglebuttons in anderem Outfit, hier wird demnach das Signal *toggled* belegt.

Radiobutton
***********

Radiobuttons dienen der Auswahl _eines_ Listenpunktes aus einer gegebenen Liste. Das Element selbst funktioniert ebenfalls wie ein Togglebutton (das Signal *toggled* zuweisen).

Zusätzlich werden die zusammengehörigen Listenpunkte zu einer Gruppe zugeordet. Dies bewerkstelligt man einfach, indem man alle Radiobuttons unter "Allgemein > Knopfattribute > Gruppe" an einem "führenden Radiobutton" ausrichtet.


Python
------

Da Checkbox und Radiobutton Togglebuttons sind, wird hier der Status über die Funktion ``widget.get_active()`` abgerufen.

Beim Switch wird dem Signal *state_set* ein Parameter übergeben, der True/False ausgibt:

.. code-block:: python

    def on_switch_state_set(self,widget,state):
        if state is True:
            print("switch is on")
        else:
            print("switch is off")

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 04_clickableelements.glade xml

Python
******

.. listing:: 04_clickableelements.py python
