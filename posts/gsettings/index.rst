.. title: Das Konfigurationssystem GSettings
.. slug: gsettings
.. date: 2017-04-22 23:47:12 UTC+01:00
.. tags: glade,python,gsettings
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Das GNOME-eigene Konfigurationssystem GSettings**

GSettings ist GNOMEs zentrales Konfigurationssystem für Anwendungen. Es ist die Schnittstelle für verschiedenmögliche Backends, gemeinhin ist dies dconf.

Mittels grafischem (dconf-editor) oder Kommandozeilentool (gsettings) lassen sich Konfigurationen abfragen und manipulieren.

Das folgende Beispiel kann Hintergrundbilder laden, festlegen und bookmarken/favorisieren.

.. thumbnail:: /images/17_gsettings.png

Schemas
-------

Um eine Konfiguration für eine Anwendung zu erstellen, muss diese in einer Schema-Datei definiert werden. Diese Datei ist eine XML-formatierte Datei, die anschließend in sein maschinenlesbares Äquivalent überführt werden muss.

Ein Beispiel für eine Schema-Datei mit einer festzulegenden Eigenschaft (key) wäre etwa:

.. code-block:: xml
    
    <schemalist>
      <schema id="org.gtk.Test" path="/org/gtk/Test/">
    
        <key name="string-key" type="s">
          <default>""</default>
          <summary>A string</summary>
          <description>
            Configuration key defined for a string. Default value is set to an empty string.
          </description>
        </key>
    
      </schema>
    </schemalist>

Die Dateibenennung folgt der Vorgabe "``schema.id.gschema.xml``". Das Standardinstallationsverzeichnis für Schema-Dateien ist ``/usr/share/glib-2.0/schemas``. Schema-Dateien können auch außerhalb dieses Verzeichnisses genutzt werden (z.B. lokal, zu Testzwecken), sie werden dann aber nicht vom dconf-editor angezeigt.

Die erforderliche Kompilierung erfolgt mit

.. code:: bash

    glib-compile-schemas /path/to/schema/files/
    #default directory
    glib-compile-schemas /usr/share/glib-2.0/schemas/

Die kompilierte und nun von GSettings verwendete Datei ist ``gschemas.compiled``.

Glade
-----

Das Beispiel soll Bilder anzeigen, dafür wird das Widget *GtkImage* benötigt. Alle Steuerungselemente werden in der Headerbar untergebracht:

 * "Open File"-Button: öffnet einen `FileChooserDialog <link://slug/fcdialog>`_
 * Switch: schaltet Desktop-Icons an oder ab
 * "Fav"-Togglebutton: bookmarkt angezeigte Dateien, zeigt an, ob angezeigte Datei als Favorit markiert ist
 * "Set as wallpaper"-Button: angezeigte Datei als Hintergrundbild verwenden
 * *MenuButton*: unterhalb des Buttons wird eine Liste der favorisierten Dateien angezeigt, die von dort aus aufgerufen werden können

Python
------

Globales Schema laden
*********************

Eine bestehende Konfiguration zu laden, geschieht einfach per

.. code:: python

    setting = Gio.Settings.new("full.schema.path")
    #load desktop background configuration
    setting = Gio.Settings.new("org.gnome.desktop.background")

Lokales Schema laden
********************

Bei einem lokal gespeicherten Schema muss der Ort der ``schemas.compiled`` angegeben werden, bevor die Konfiguration geladen werden kann:

.. code:: python

    schema_source = Gio.SettingsSchemaSource.new_from_directory(os.getcwd(), 
                Gio.SettingsSchemaSource.get_default(), False)
    schema = Gio.SettingsSchemaSource.lookup(schema_source,"org.example.wallpaper-changer",False)
    setting = Gio.Settings.new_full(schema, None, None)

Widget verknüpfen
*****************

Es ist möglich, GSettings-Eigenschaften direkt an Widgets zu binden. Diese können dann bidirektional Zustände anzeigen bzw. man kann Änderungen an ihnen vornehmen:

.. code:: python

    setting.bind("setting-key", widget, property, Gio.SettingsBindFlags...)

Im Beispiel wäre dies also

.. code:: python

    self.bg_setting.bind("show-desktop-icons", self.obj("switch"), "active", Gio.SettingsBindFlags.DEFAULT)

Werte abrufen und festlegen
***************************

Eigenschaften können mit ``get_"type"`` und ``set_"type"`` ermittelt und festgelegt werden. Die relevante Funktion ist vom festgelegten Schlüsseltyp abhängig, also ``get_string`` und ``set_string`` für Zeichenketten, ``get_int`` und ``set_int`` für Ganzzahlen usw. (siehe `PyGObject API Reference <https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html>`_).

Wird der Wert einer Eigenschaft per ``get_value(key)`` abgefragt, wird dies immer als Wert des Typs `GLib.Variant <https://lazka.github.io/pgi-docs/#GLib-2.0/classes/Variant.html#GLib.Variant>`_ zurückgegeben. Entsprechend erwartet die Funktion ``set_value(key)`` ebenfalls diesen Typ.

Die Inhalte dieser Werte lassen sich einfach in simple Datentypen konvertieren, z.B.

.. code:: python

    #return string
    setting.get_value(key).get_string()
    #return anything (list, string, bool etc.)
    setting.get_value(key).unpack()
    
Umgekehrt lassen sich reguläre Datentypen nach folgendem Muster als *GLib.Variant*-Typ ausdrücken und an GSettings übergeben:

.. code:: python

    setting.set_value(key, GLib.Variant(string_type, value)

Eine Liste der verfügbaren Stringtypen finden sich in der `GNOME Developer-Dokumentation <https://developer.gnome.org/glib/stable/gvariant-format-strings.html>`_.

Im Beispiel wird auf diese Art die Favoritenliste aktualisiert:

.. code:: python

    app_setting.set_value("favourites", GLib.Variant('as',fav_list))



Links
-----

 * `Standardeinstellungen in GSettings ändern (German) <https://www.florian-diesch.de/doc/gnome3/standardeinstellungen-in-gsettings-aendern.html>`_
 * `Introduction to GSettings in Python <http://zderadicka.eu/gsettings-flexible-configuration-system/>`_
 * `Short Example of GSettings Bindings with Python using a Gtk Switch <https://marianochavero.wordpress.com/2012/04/03/short-example-of-gsettings-bindings-in-python/>`_
 * `GSettings - flexible configuration system <http://zderadicka.eu/gsettings-flexible-configuration-system/>`_
 * `dconf (ubuntuusers-Wiki) <https://wiki.ubuntuusers.de/GNOME_Konfiguration/dconf/>`_

Listings
--------

Schema
******

.. listing:: org.example.wallpaper-changer.gschema.xml xml

Glade
*****

.. listing:: 17_gsettings.glade xml

Python
******

.. listing:: 17_gsettings.py python
