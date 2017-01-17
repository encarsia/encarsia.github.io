.. title: Tutorial-Reihe zu Glade
.. slug: tutorial-reihe-glade
.. date: 2016-11-02 15:23:57 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

Intro
-----

Bei der Erstellung der grafischen Oberfläche für gpt_ habe ich auf Glade zurückgegriffen, einem grafischen Werkzeug, mit dem man relativ einfach `GTK+ <http://www.gtk.org/>`_-Oberflächen erstellen kann.

Mit Glade erstellte Projektdateien sind GtkBuilder_-XML-Dateien, die Verbindung zum eigentlichen Programm erfolgt über Signale, dabei werden zahlreiche Programmiersprachen unterstützt. Hier werde ich Python verwenden.

Da es in den letzten Jahren Versionssprünge sowohl bei Python als auch GTK+ gegeben hat (jeweils von 2.x auf 3.x), gibt es viele Dokumentationen und Tutorials, die nicht 1:1 anwendbar sind, d.h. die Funktionen sind meist gleich, nur die Syntax unterscheidet sich minimal (siehe Links).

An dieser Stelle versuche ich aktuell zu bleiben, derzeit mit Python 3.5.2 und Glade 3.20.0.

.. _gpt: https://github.com/encarsia/gpt
.. _GtkBuilder: https://developer.gnome.org/gtk3/stable/GtkBuilder.html

Nicht exklusiv
--------------

GTK+-Elemente können natürlich auch ohne Glade direkt im Quellcode des Programms erstellt werden. Es ist möglich, beide Optionen parallel zu verwenden oder auch im Verlauf das eine gegen das andere zu ersetzen.

Links
-----

- `The Python GTK+ 3 Tutorial <http://python-gtk-3-tutorial.readthedocs.io/>`_ - Grundlagen der Programmierung von GTK+-GUI mit Python
- `Creating a GUI using PyGTK and Glade <http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/>`_ - Grundlagentutorial für PyGTK (Python 2.x)
- `Programmieren mit Python und Glade <https://www.florian-diesch.de/doc/python-und-glade/online/index.html>`_ - umfangreiches Tutorial auf Deutsch
- `Python GObject Introspection API Reference <https://lazka.github.io/pgi-docs/>`_ - vollständige Dokumentation des GI-Moduls (bookmark this!)


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

- Geplant:
    - Notebook
    - FileChooserDialog
    - Medien und GStreamer
    - Textfelder mit GtkTextView und GtkSourceView
    - Interaktion mit anderen Anwendungen mit und ohne Threading

- Verzeichnis der Beispieldateien: `encarsia.github.io/listings <https://encarsia.github.io/listings/>`_
