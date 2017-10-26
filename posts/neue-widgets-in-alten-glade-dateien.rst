.. title: Neue Widgets in alten Glade-Dateien
.. slug: neue-widgets-in-alten-glade-dateien
.. date: 2017-10-25 10:12:09 UTC+02:00
.. tags: glade
.. category: tipps&tricks
.. link: 
.. description: 
.. type: text

**Problem: deaktivierte Widgets in älteren Glade-Dateien**

Es kann vorkommen, dass nach dem Öffnen einer Datei in Glade Widgets ausgegraut sind.

.. thumbnail:: /images/glade_widgetsinactive.png

Per Tooltip wird dann zum Beispiel angezeigt:

.. thumbnail:: /images/glade_widgetsinactive_tooltip.png

Die Ursache liegt in der angegebenen Gtk+-Version gleich am Anfang der Glade-Datei:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated with glade 3.20.1 -->
    <interface>
      <requires lib="gtk+" version="3.0"/>
      ...

Dieses Zeile wird auch beim neuerlichen Speichern mit einer aktuellen Glade-Version nicht verändert. Abhilfe kann hier ganz simpel geschaffen werden, indem ``"3.0"`` durch eine aktuellere Version ersetzt wird (derzeit ``"3.20"``).
