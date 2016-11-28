.. title: Bars
.. slug: bars
.. date: 2016-11-08 14:20:08 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Progressbar und Levelbar**

Glade
-----

.. thumbnail:: /images/06_progresslevel.png

Progressbar
***********

Fortschrittsbalken zeigen für gewöhnlich den Status eines länger dauernden Prozesses an. Es gibt dabei zwei Modi:

    1. verhältnismäßige Anzeige, der Fortschritt wird mit einem Wert zwischen 0 und 1 ausgedrückt 
    
    2. Aktivitätsmodus, ein beweglicher Block läuft nach zugewiesener Schrittweite hin und her

Zusätzlich hat das Widget eine optionale Textanzeige. Wird der Inhalt nicht spezifiziert, wird der Fortschritt in Prozent angezeigt.

Levelbar
********

Levelbars werden normalerweise als Füllstandsanzeiger genutzt. Der Füllstand wird dabei wie beim Fortschrittsbalken angezeigt, weitere Widget-Eigenschaften sind:

    1. Zwei Anzeigenmodi:

        1. *continuous*: ein einzelner Block repräsentiert den gegebenen Wert
        
        2. *discrete*: Levelbar wird in eine festgelegte Anzahl von Blöcken geteilt, ein Block steht für einen Wertebereich

    2. Festlegen von Minimal-/Maximalwert möglich, Standardwert ist 0 bzw. 1; beim Anzeigenmodus *discrete* entspricht der Maximalwert der Anzahl der Blöcke

    3. Farbliche Änderungen des Balkens bei Überschreiten bestimmter Werte (siehe `CSS-Artikel <link://slug/css>`_)

.. TEASER_END

.. listing:: 06_progresslevel.glade xml

Python
------

Progressbar
***********

Im Beispiel repräsentiert der erste Balken den Wert, der zweite befindet sich im Aktivitätsmodus. Möchte man bei letzterem trotzdem eine Prozentangabe im Textfeld darstellen, muss man diesen manuell einsetzen:

.. code-block:: python

    #verhältnismäßige Anzeige
    widget.set_fraction(value)
    #Aktivitätsanzeige mit Prozentangabe im Tetxfeld
    widget.pulse()
    widget.set_text("%d %%" % perc_value)


Levelbar
********

Was ``set_fraction`` für Progressbar, ist ``set_value`` für Levelbar. Im *continuous*-Modus ist dies selbsterklärend, im *discrete*-Modus muss man bedenken, wie viele Blöcke definiert wurden.

Auf die Funktion ``add_offset_value`` und Farbänderung des Balkens beim Überschreiten definierter Werte wird im `CSS-Artikel <link://slug/css>`_ eingegangen.

.. listing:: 06_progresslevel.py python
