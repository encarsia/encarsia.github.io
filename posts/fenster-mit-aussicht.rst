.. title: Fenster mit Aussicht - ein Minimalbeispiel
.. slug: fenster-mit-aussicht
.. date: 2016-11-02 17:14:04 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

Glade
-----

Nach dem Start präsentiert sich Glade dreigeteilt, links ist die Fenster-/Widget-Auswahl, in der Mitte die Projektansicht und rechts eine Baumansicht des Projekts, im unteren Bereich können Eigenschaften und Signale editiert werden.

Nun erstellt man ein Fenster und gibt ihm eine Kennung. Mit dieser Kennung wird das Objekt im Programmcode angesprochen.

.. thumbnail:: /images/01_glade.png

Um die Ausführung von Funktionen zu initiieren, müssen sie mit Signalen gekoppelt werden. Signale können je nach Objektart verschieden ausgelöst werden, durch Anklicken, Markieren, Editieren, Schalten etc.

Um in diesem Beispiel das Programmfenster mit dem Schließen-Button zu schließen, wird das Signal *destroy* benötigt. Beim Funktionsnamen hilft die Vorschlagsfunktion nach dem Schema ``on_kennung_signal``.
Ich empfehle, diesen Vorschlägen im allgemeinen zu folgen, sie erleichtern die Tipparbeit.

.. thumbnail:: /images/01_destroysignal.png

Mit Glade wird kein Programmcode, sondern eine XML-Datei des Typs GtkBuilder erstellt. Diese sieht hier wie folgt aus:

.. listing:: 01_minimal.glade xml

Python
------

First things first. Die GtkBuilder-Funktionen stehen im Gtk-Modul aus den Python GObject Introspection-Bindings zur Verfügung:

.. code-block:: python

    import gi
    gi.require_version('Gtk','3.0')
    from gi.repository import Gtk

Nach dem Aufruf von ``Gtk.Builder()`` wird die Glade-Datei geladen. Um die Übersicht zu bewahren, können dies auch mehrere Dateien sein, es sollte allerdings auf eine eindeutige Kennung geachtet werden. Bei doppelten Kennungen ist die zuletzt geladene aktiv.

Anschließend werden die Signale verbunden. Meine Empfehlung ist hier, die dazugehörigen Funktionen der Übersicht wegen in eine eigene Klasse auszulagern.

.. listing:: 01_minimal.py python

Dieses Skript öffnet ein leeres Fenster, das per Schließen-Button beendet werden kann.

Ohne Glade
----------

Das oben konstruierte Beispiel entspricht dem Basisbeispiel im `Python GTK+ 3 Tutorial <http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html>`_:

.. code-block:: python

    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

Man sollte sich von der Kürze dieses Beispiels nicht täuschen lassen. Die eigentlichen Elemente, Boxen, Widget, Buttons, Leisten etc. fehlen hier komplett.