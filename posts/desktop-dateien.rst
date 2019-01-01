.. title: GNOME-Anwendungsstarter
.. slug: desktop-dateien
.. date: 2019-01-01 13:21:19 UTC+01:00
.. tags: desktop,gnome,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Anwendungsstarter in GNOME**

Anwendungsstarter in GNOME und anderen Desktopumgebungen werden mit Desktopeinträgen in Form von Textdateien mit der Endung "desktop" realisiert.

Weiterlesen
===========

* `Desktop Entry Specifications <https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>`_
* `.desktop-Dateien (ubuntuusers-de-Wiki) <https://wiki.ubuntuusers.de/.desktop-Dateien/>`_
* `Desktop files: putting your application in the desktop menus <https://developer.gnome.org/integration-guide/stable/desktop-files.html.en>`_
* `XDG Basedir Library <https://docs.racket-lang.org/basedir/index.html>`_

Speicherort
===========

Der Speicherort von .desktop-Dateien richtet sich nach den Freedesktop-Spezifikationen. Desktop-Dateien befinden sich in ``$XDG_DATA_DIRS/appications``, also normalerweise in den Verzeichnissen

.. code::

    ~/.local/share/applications
    /usr/local/share/applications
    /usr/share/applications

und werden in dieser Reihenfolge durchsucht. Alle Dateien in diesen Verzeichnissen werden in der GNOME-Shell-Übersicht bzw. der Suche berücksichtigt.

Minimalkonfiguration
====================

Ein funktionierender Desktopeintrag muss mindestens die drei folgenden Attribute enthalten:

.. code:: YAML

    [Desktop Entry]
    Name=Application name
    Exec=python path/to/script.py
    Type=Application

WM_CLASS
========

Die WM_CLASS-Eigenschaft wird von X-Windowmanager-Systemen zur Zuordnung zwischen Anwendung und Windowmanager verwendet.

Fehlt diese Zuordnung, wird der Programmname nicht in der Topbar dargestellt, in der Seitenleiste wird das Programm nicht als Instanz angesehen, wenn es als Favorit markiert ist sondern separat und die Anwendung kann nicht von der Übersicht aus als Favorit gespeichert werden.

.desktop
********

In der Desktopdatei muss das Attribut ``StartupWMClass`` definiert werden.

Um die WM_CLASS-Bezeichnung eines Fensters herauszufinden, kann man in einem Terminal

.. code:: console

    $ xprop | grep WM_CLASS

aufrufen und das gewünschte Fenster anklicken.

Gtk+-Python-Anwendung
*********************

Setzt man den Programmnamen mit der Funktion ``GLib.set_prgname("appname")``, so entspricht dies dem Attribut WM_CLASS. In der Desktopdatei muss demzufolge ``StartupWMClass=appname`` definiert sein.

Die bisher für diese Aufgabe verwendete Funktion ``set_wmclass(wmclass_name, wmclass_class)`` von *Gtk.Window* ist seit Version 3.22 veraltet. Sie funktioniert zwar noch, sollte aber nicht mehr verwendet werden.

Nützliche Attribute
===================

``Path``
    Arbeitsverzeichnis des Programms. So kann zum Beispiel die ``Exec``-Zeile verkürzt bzw. übersichtlicher gestaltet werden:

    .. code::

        # ohne Path
        Exec=python /long/path/to/your/application/folder/run.py

        # mit Path
        Path=/long/path/to/your/application/folder
        Exec=python run.py

``Icon``
    Mit Icons verhält es sich ähnlich zu Desktop-Dateien, sie werden zunächst in``$XDG_DATA_DIRS/icons`` vermutet, können aber auch als absoluter Pfad angegeben werden.

``Keywords``
    Da es mit der GNOME-Shell kein klassisches Anwendungsstartermenü mehr gibt, ist es hilfreich, wenn ein Programm unter verschiedenen Stichworten und nicht nur unter ``Name`` selbst in der Startersuche gefunden werden kann. Die Stichwörter werden als semikolonseparierte Strings angegeben.

``Categories``
    Hier kann man Kategorien für die Einsortierung in Menüs angeben.

Zusätzliche Programmaktionen
============================

Desktopeinträge können sogenannte Aktionen enthalten, die zusätzliche Wege enthalten, Anwendungen zu starten. Diese werden als Untermenüs in Form von "Quicklists" oder "Jumplists" dargestellt.

Im Desktopeintrag wird das Attribut ``Actions`` angelegt, diese Actions werden innerhalb der Datei darunter in "Desktop Action"-Abschnitten definiert:

.. code:: YAML

    [Desktop Entry]
    ...
    Actions=option1;option2;

    [Desktop Action option1]
    Name=Start with Option 1
    Exec=python run.py --option1

    [Desktop Action option2]
    Name=Start with Option 2
    Exec=python run.py --option2

.. figure:: /images/desktop_action.png
    
    Zusätzliche Anwendungsstarter von `GPT <https://github.com/encarsia/gpt>`_

