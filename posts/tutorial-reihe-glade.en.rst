.. title: Glade tutorial series
.. slug: tutorial-reihe-glade
.. date: 2016-11-02 15:23:57 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

Motivation
----------

Glade was my weapon of choice when I started creating the graphical interface for gpt_ and NoN_. It itself is a GUI for creating `GTK+ <http://www.gtk.org/>` GUIs.

Glade project files are XML formatted GtkBuilder_ files. The connection to the source code is established by signals. Numerous languages are supported, I will use Python here.

There are plenty of tutorials and docs around that are not or only partly working or valid due to recent development progress (GTK+ and Python from 2.x to 3.x) but for the most part they are a good start (see links below).

I attempt to keep this basic tutorial up to date (Python 3.5.2 (3.6 just hit my machine and there aren't any problems so far but I will have a closer look on the examples) and Glade 3.20.0).

.. _gpt: https://github.com/encarsia/gpt
.. _NoN: https://github.com/encarsia/non
.. _GtkBuilder: https://developer.gnome.org/gtk3/stable/GtkBuilder.html


Topics
------

- `Minimal example <link://slug/fenster-mit-aussicht>`_
- `Buttons and labels <link://slug/push-the-button>`_
- `Windows and dialogues <link://slug/durchzug>`_
- `Switch, checkbox and radiobutton <link://slug/clickbaiting>`_
- `Menu, toolbar and statusbar <link://slug/drei-gange-menu>`_
- `Progressbars and levelbars <link://slug/bars>`_
- `CSS <link://slug/css>`_
- `Spinbutton and combobox <link://slug/qual-der-wahl>`_
- `ListStore and TreeView <link://slug/uberlistet>`_
- `TreeStore with sorting and filtering <link://slug/ansichtssache>`_
- `Localization using locale and gettext <link://slug/romani-ite-domum>`_
- `VTE terminal <link://slug/exterminate>`_
- `Dialogues <link://slug/dialoge>`_
- `Run program as GTK+ application <link://slug/application>`_
- `Icon, headerbar and commandline options <link://slug/application-fortsetzung>`_
- `File chooser dialog <link://slug/fcdialog>`_
- `Media player with GStreamer <link://slug/gst-player>`_
- `Media player with LibVLC <link://slug/vlc-player>`_
- `Stack and Notebook <link://slug/stacksnotebooks>`_

Directory of example files: `encarsia.github.io/listings <https://encarsia.github.io/listings/>`_


Non-exclusive
-------------

Of course GTK+ elements can be directly constructed in the source code. It is also possible to use both ways simultaneously or replace one with the other during development process.

The fact that Glade supports various programming languages it may also be possible to create applications in different programming languages using the same graphical interface.

Links
-----

- `The Python GTK+ 3 Tutorial <http://python-gtk-3-tutorial.readthedocs.io/>`_ - Introduction to GTK+ with Python
- `PyGObject Tutorial <https://pygobject.readthedocs.io> - PyGObject documentation
- `Creating a GUI using PyGTK and Glade <http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/>`_ - Basic tutorial to PyGTK (Python 2.x)
- `Programmieren mit Python und Glade <https://www.florian-diesch.de/doc/python-und-glade/online/index.html>`_ - extensive tutorial in German
- `Python GObject Introspection API Reference <https://lazka.github.io/pgi-docs/>`_ - complete reference of the GI module (bookmark this!)

Todo
----

- WebKit2
- Interaction between other applications


