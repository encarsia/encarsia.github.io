.. title: Desktopintegrationsbemühungen
.. slug: application-fortsetzung
.. date: 2017-01-15 13:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Desktopintegration: Icon, Headerbar, Kommandozeilenoptionen**

(Fortsetzung zum Artikel `GtkApplication <link://slug/application>`_)

.. thumbnail:: /images/15_application.png

Glade
-----

Icon
****

Einem Fenster lässt sich direkt in Glade unter *"Allgemein > Darstellung > Symboldatei"* ein Icon auswählen. Das Problem dabei ist, dass Glade Bilddateien nur anzeigt, wenn sie sich im selben Verzeichnis wie die Gladedatei selbst befinden, auch wenn man ein anderes Verzeichnis auswählt.

Am einfachsten behebt man dies, indem man die Gladedatei in einem Texteditor bearbeitet und den (relativen) Pfad zum `Icon <https://openclipart.org/detail/22535/ducky-icon>`_ angibt. Diese Einstellung bleibt auch erhalten, wenn die Datei später mit Glade bearbeitet und gespeichert wird:

.. code-block:: xml

  <object class="GtkApplicationWindow" id="window">
    ...
    <!-- <property name="icon">duckyou.svg</property> -->
    <property name="icon">../files/duckyou.svg</property>
    ...

Headerbar
*********

Die Headerbar wurde mit GNOME 3.10 eingeführt und vereint Titelleiste und Toolbar in einem Widget, d.h neben Titel und Untertitel können rechts und/oder links verschiedene Widgets (Menüs, Buttons) angelegt sowie clientseitige Fensterkontrollknöpfe angezeigt werden.

Die Headerbar ist optional. Möchte man sie nutzen, muss in den Fenstereinstellungen *"Allgemein > Darstellung > Klienseitige Fensterdekoration"* ausgewählt werden. Daraufhin erscheint im oberen Bereich des Fensters ein reservierter Bereich, in dem die Headerbar platziert wird. Wird die Headerbar außerhalb davon platziert, wird weiterhin zusätzlich die normale Titelleiste angezeigt.

.. image:: /images/15_headerbarglade.png

Kommandozeilenoptionen
----------------------

*GtkApplication* stellt die erforderlichen Mittel für anwendungseigene Kommandozeilenoptionen zur Verfügung (`Handling command line options in GApplication <https://wiki.gnome.org/HowDoI/GtkApplication/CommandLine>`_).

Optionen anlegen
****************

Verfügbare Optionen werden mit der Funktion ``add_main_option_entries(entrylist)`` hinzugefügt. Diese Einträge haben das Format *GLib.OptionEntry*, welches allerlei Parameter besitzt.

.. code-block:: python

    def __init__(self):
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.add_main_option_entries([
            self.create_option_entry("--version", description="Show version numbers and exit"),
            self.create_option_entry("--setlabel", description="Set label widget",arg=GLib.OptionArg.STRING,),
            self.create_option_entry("--bollocks", description="Additional test option - exit"),
        ])

    def create_option_entry(self,
                            long_name,
                            short_name=None,
                            flags=0,
                            arg=GLib.OptionArg.NONE,
                            arg_data=None,
                            description=None,
                            arg_description=None):
        option = GLib.OptionEntry()
        option.long_name = long_name.lstrip('-')
        option.short_name = 0 if not short_name else ord(short_name.lstrip('-'))
        option.flags = flags
        option.arg = arg
        option.arg_data = arg_data
        option.description = description
        option.arg_description = arg_description
        return option

Shortnames
**********

Eine Option kann ein aus einem Buchstaben (oder besser gesagt "printable ASCII character different from ‘-‘") bestehenden Synonmym besitzen, den Shortname. Bei der Option ``--help`` ist dies gemeinhin ``-h``.

Die ``short_name``-Variable von *OptionEntry* ist allerdings integer. Die in der `Dokumentation <https://lazka.github.io/pgi-docs/#GLib-2.0/classes/OptionEntry.html#GLib.OptionEntry>`_ nicht ersichtliche Lösung besteht darin, in der Variable die Dezimalkodierung des entsprechenden Zeichens zu übergeben, also etwa 97 für "a". Bei ungültigen Werten wird eine Fehlermeldung ausgegeben. Optionen ohne Shortname erhalten den Wert 0.

Signal verbinden
****************

Der *GtkApplication*-eigene "handle-local-options"-Handler verarbeitet die Optionen. Sobald Optionen angelegt sind, wird dieses Signal noch vor dem "startup"-Signal ausgelöst

.. code:: python

    self.app.connect("handle-local-options", self.on_local_option)

Optionen verarbeiten
********************

Die an die Handler-Funktion übergebene ``option`` ist ein Element der Klasse *GLib.VariantDict*. Mit ``contains("option")`` lässt sich nach der übergebenen Option suchen.

.. code-block:: python

    def on_local_option(self, app, option):
        if option.contains("option1"):
            #do something and exit normally
            return 0
        elif option.contains("option2"):
            #do something different and exit
            return 0
        elif option.contains("option3"):
            #do more and continue
        return -1

Ein übergebener String kann extrahiert werden, indem *GLib.VariantDict* mit ``end()`` in *GLib.Variant* konvertiert wird, das sich wiederum mit ``keys()`` auslesen lässt:

.. code-block:: python

    var = GLib.VariantDict.end(option)
    option_string = var[var.keys()[0]]

Ein Return-Wert ist zwingend erforderlich, er entspricht dabei dem Exit-Status:
    * **-1**: Anwendung wird weiter ausgeführt
    * **0**: erfolgreiche Ausführung, Anwendung wird beendet, "startup/activate" werden nicht ausgeführt
    * **1** bzw. positiver Wert: nicht erfolgreiche Ausführung, Anwendung wird beendet


Optionen übergeben
******************

Die Option, die immer verfügbar ist, ist ``--help``. Hier werden unter "Anwendungsoptionen" die angelegten Optionen samt Beschreibung aufgeführt. Die Optionen können wie definiert angegeben werden:

.. code:: console

    $ python script.py --version
    Python: 3.6.0
    GTK+:   3.22.6

oder mit ``--setlabel`` einen String an *Gtk.Label* übergeben:

.. code:: console

    $ python script.py --setlabel "I can haz options!"

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 15_application.glade xml

Python
******

.. listing:: 15_application.py python
