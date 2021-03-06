.. title: Tutorial-Reihe zu Glade
.. slug: tutorial-reihe-glade
.. date: 2016-11-02 15:23:57 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

Motivation
----------

Bei der Erstellung der grafischen Oberfläche sowohl für gpt_ als auch NoN_ habe ich auf Glade zurückgegriffen, einem grafischen Werkzeug, mit dem man relativ einfach `GTK+ <http://www.gtk.org/>`_-Oberflächen erstellen kann.

Mit Glade erstellte Projektdateien sind GtkBuilder_-XML-Dateien, die Verbindung zum eigentlichen Programm erfolgt über Signale, dabei werden zahlreiche Programmiersprachen unterstützt. Hier werde ich Python verwenden.

Da es in den letzten Jahren Versionssprünge sowohl bei Python als auch GTK+ gegeben hat (jeweils von 2.x auf 3.x), gibt es viele Dokumentationen und Tutorials, die nicht 1:1 anwendbar sind, d.h. die Funktionen sind meist gleich, nur die Syntax unterscheidet sich minimal (siehe Links).

An dieser Stelle versuche ich aktuell zu bleiben, derzeit mit Python 3.7.1 und Glade 3.22.1.

.. _gpt: https://github.com/encarsia/gpt
.. _GtkBuilder: https://developer.gnome.org/gtk3/stable/GtkBuilder.html
.. _NoN: https://github.com/encarsia/non

Themen
------

- `Minimalbeispiel <link://slug/fenster-mit-aussicht>`_
- `Buttons und Labels <link://slug/push-the-button>`_
- `Fenster und Dialoge <link://slug/durchzug>`_
- `Schalter, Checkbox und Radiobutton <link://slug/clickbaiting>`_
- `Menü, Toolbar und Statusbar <link://slug/drei-gange-menu>`_
- `Fortschrittsbalken und Levelbar <link://slug/bars>`_
- `CSS <link://slug/css>`_
- `Spinbutton und Combobox <link://slug/qual-der-wahl>`_
- `ListStore und TreeView <link://slug/uberlistet>`_
- `TreeStore mit Sortierung und Filterung <link://slug/ansichtssache>`_
- `Lokalisation mit locale und gettext <link://slug/romani-ite-domum>`_
- `VTE-Terminal <link://slug/exterminate>`_
- `Dialoge <link://slug/dialoge>`_
- `Programm als eigenständige GTK+-Anwendung <link://slug/application>`_
- `Icon, Headerbar und Kommandozeilenoptionen <link://slug/application-fortsetzung>`_
- `Dateiauswahldialog <link://slug/fcdialog>`_
- `GSettings-Konfigurationssystem <link://slug/gsettings>`_
- `Mediaplayer mit GStreamer <link://slug/gst-player>`_
- `Mediaplayer mit GStreamer (Edition gtksink) <link://slug/gtksink-player>`_
- `Mediaplayer mit LibVLC <link://slug/vlc-player>`_
- `Stack und Notebook <link://slug/stacksnotebooks>`_
- `Texteditor mit GtkSourceView <link://slug/gtksv>`_
- `Überarbeitete Oberfläche in Glade 3.22 <link://slug/glade-322>`_
- `Widget-Änderungen in GTK+ 2.20+ <link://slug/gtk220neu>`_
- `GTK+-Anwendung mit setuptools packen <link://slug/setuptools-spicker>`_
- `Desktop-Dateien <link://slug/desktop-dateien>`_

Dateien
-------

- Verzeichnis der Beispieldateien: `encarsia.github.io/listings <https://encarsia.github.io/listings/>`_
- `E-Book <https://encarsia.github.io/pages/downloads>`_

Nicht exklusiv
--------------

GTK+-Elemente können natürlich auch ohne Glade direkt im Quellcode des Programms erstellt werden. Es ist möglich, beide Optionen parallel zu verwenden oder auch im Entwicklungs-Verlauf das eine gegen das andere zu ersetzen.

Da Glade in verschiedenen Programmiersprachen eingesetzt werden kann, ist es ebenso denkbar, Programme in verschiedenen Sprachen mit derselben Oberfläche zu erstellen (migrieren).

Links
-----

- `The Python GTK+ 3 Tutorial <http://python-gtk-3-tutorial.readthedocs.io/>`_ - Grundlagen der Programmierung von GTK+-GUI mit Python
- `PyGObject Tutorial <https://pygobject.readthedocs.io>`_ - PyGObject-Dokumentation
- `Creating a GUI using PyGTK and Glade <http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/>`_ - Grundlagentutorial für PyGTK (Python 2.x)
- `Programmieren mit Python und Glade <https://www.florian-diesch.de/doc/python-und-glade/online/index.html>`_ - umfangreiches Tutorial auf Deutsch
- `Python GObject Introspection API Reference <https://lazka.github.io/pgi-docs/>`_ - vollständige Dokumentation des GI-Moduls (bookmark this!)
