.. title: Überarbeitete Oberfläche in Glade 3.22
.. slug: glade-322
.. date: 2018-05-13 23:33:16 UTC+02:00
.. tags: glade
.. category: tutorial
.. link: 
.. description: 
.. type: text

**Im Zuge der Veröffentlichung von GNOME 3.28 wurde auch Glade eine ordentliche Portion Zuwendung zuteil.**

Headerbar
=========

Das in GNOME 3.10 (Veröffentlichung 2013) eingeführte Headerbar-Widget ließ sich selbst bereits in `Glade <https://glade.gnome.org/>`_ verwenden, die Anwendung selbst nutzte sie bisher nicht. Sie vereint Titelleiste, Menü, Toolbar und die Projekt-Tableiste. Durch diese Komprimierung wird viel leerer Raum eingespart (siehe Screenshots).

Arbeitsfläche
=============

Die Dreiteilung der Oberfläche ist erhalten geblieben, es gibt aber zwei wesentliche Änderungen:

    1. Die Widgetauswahl erfolgt nicht mehr aus der linken Spalte, sondern sie ist oben auf der mittleren Arbeitsfläche als Buttonleiste mit Dropdown-Menü erreichbar.

    2. In der nun freien Spalte werden die Widgetstruktur des aktuellen Projekts angezeigt. Diese war zuvor in der oberen Hälfte der rechten Spalte zu finden.

Die Verlagerung der Widgetauswahl ermöglicht eine komplette Nutzung des vertikalen Platzes für die Anzeige der Struktur auf der linken sowie deren Eigenschaften auf der rechten Seite. 

Tour
====

Beim ersten Aufrug der neuen Version startet ein Assistent, der etwas aufdringlich die Neuerungen anpreist. Dieser kann jederzeit über die Einstellungen in der Headerbar unter *"Einführung in interaktive Benutzeroberflächen"* erneut aufgerufen werden.

.. figure:: /images/glade322_tour.png

    Tour-Wizard

Screenshots
===========

.. thumbnail:: /images/glade322.png
    :width: 600px

    Glade 3.22

.. thumbnail:: /images/01_glade.png
    :width: 600px

    Glade 3.20

