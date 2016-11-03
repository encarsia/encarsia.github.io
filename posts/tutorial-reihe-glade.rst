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

GTK+-Elemente können natürlich auch ohne Glade direkt in den Quellcode des Programms geschrieben werden. Es ist möglich, beide Optionen parallel zu verwenden oder auch im Verlauf das eine gegen das andere zu ersetzen.

Links
-----

- `The Python GTK+ 3 Tutorial <http://python-gtk-3-tutorial.readthedocs.io/>`_ - Grundlagen der Programmierung von GTK+-GUI mit Python
- `Creating a GUI using PyGTK and Glade <http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/>`_ - Grundlagentutorial für PyGTK (Python 2.x)
- `Programmieren mit Python und Glade <https://www.florian-diesch.de/doc/python-und-glade/online/index.html>`_ - umfangreiches Tutorial auf Deutsch

Themen
------

- Fertig:
    - `Minimalbeispiel <link://slug/fenster-mit-aussicht>`_
    - `Buttons und Labels <link://slug/push-the-button>`_
    - `Fenster und Dialoge <link://slug/durchzug>`_

- In Arbeit:
    - Menü und Toolbar
    - Statusbar und Levelbar
    - Combobox und Spinbutton
    - ListView und TreeView
    - Schalter, Checkbox und Radiobutton
    - CSS
    - Lokalisation mit locale und gettext
    - Medien abspielen mit GStreamer


In Arbeit: