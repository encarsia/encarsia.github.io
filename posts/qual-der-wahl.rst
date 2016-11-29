.. title: Qual der Wahl
.. slug: qual-der-wahl
.. date: 2016-11-11 15:28:18 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Spinbutton und Combobox**

Die Widgets erleichtern die Eingabe bestimmer Werte, indem eine Listenauswahl oder ein Wertebereich und ggf. Standardwerte dazu vorgegeben werden. Die Eingabe ist normalerweise rein intuitiv über Mausklicks machbar, Tastatureingaben sind optional.

Glade
-----

.. thumbnail:: /images/08_combospin.png

.. TEASER_END

Spinbutton
**********

Spinbuttons haben zahlreiche, per Glade festlegbare Eigenschaften wie Mindest-/Höchst-/Standardwert. Zum Spinbutton gehört zwingend das Widget *adjustment*, das unter "Allgemein > Attribute des Einstellknopfs > Stellgröße" ausgewählt oder angelegt werden kann.

Im Beispiel repräsentieren die beiden Spinbuttons Monat und Jahr, wobei der Spinbutton für den Monat zyklisch angelegt wird, das heißt, nach dem Erreichen des Maximalwertes springt er auf den Mindestwert um. Dieses Verhalten löst das Signal *wrapped* aus und wird angelegt, um die Jahreszahl im zweiten Spinbutton passend umzuschalten.

Combobox
********

Es gibt in GTK+ zwei verschiedene Combobox-Widgets:

GtkComboboxText
    Die Auswahlliste des Dropdown-Menüs sind Strings und werden direkt im Widget erstellt.

GtkCombobox
    Die Daten für die Auswahlliste stammen aus einem Listen- oder Baumspeicher (ListStore oder TreeStore). In diesen können Datensätze mit verschiedenen Informationen gespeichert werden (siehe auch Artikel `"Überlistet" <link://slug/uberlistet>`_)

Beide Widgets können zusätzlich ein optionales Eingabefeld besitzen. In diesem Fall muss "Allgemein > Hat Eintrag" aktiviert sein. Dies legt das interne Widget *GtkEntry* an. Wichtig ist, dass dieses unter "Gemeinsam > Widget Flags" fokussierbar gemacht wird.

Im Beispiel gibt es zwei ComboboxText-Widgets. Das erste besitzt kein Eingabefeld, es ist also ausschließlich eine Auswahl unter den gegebenen Listenpunkten möglich, die Auswahlliste ist direkt in Glade eingegeben. Die zweite Combobox hat ein Eingabefeld, zu demonstrativen Zwecken werden die Listenpunkte direkt im Programm erstellt. Bei beiden wird das Signal *changed* abgefangen.

.. listing:: 08_combospin.glade xml

Python
------

Spinbutton
**********

Der Wert eines Spinbutton lässt sich einfach per ``get_value`` bzw. ``set_value`` ermitteln bzw. festlegen. So werden im Beispiel zu Beginn die aktuellen Monats- und Jahreszahlen eingetragen und in der Funktion ``on_spin_m_wrapped`` beim Umschalten von 12 auf 1 die Jahreszahl um 1 erhöht und umgekehrt.

Combobox
********

Listeneinträge einer Combobox können einfach mit der Funktion ``append`` angefügt werden, wie in diesem Beispiel etwa

.. code-block:: python

    [self.builder.get_object("comboboxtext2").append(None,entry) for entry in ("bla","blubb","ja","nein")]

Der aktuell angewählte Eintrag wird mit der Funktion ``widget.set_active_text()`` ermittelt, diese gibt auch den Text des optionalen Texteintragfeldes aus.

.. listing:: 08_combospin.py python

