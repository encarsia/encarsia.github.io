.. title: The GSettings configuration storage system
.. slug: gsettings
.. date: 2017-04-22 23:47:12 UTC+01:00
.. tags: glade,python,gsettings
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Manage application settings with GNOME's GSettings**

GSettings is the central application configuration system of the GNOME desktop. Settings are stored in binary form so you will need to use a low-level configuration tool which provides a  backend for GSettings. This can be either have a graphical (dconf-editor) or commandline interface (gsettings).

In this article's example background images will be read, set and bookmarked.

.. thumbnail:: /images/17_gsettings.png

Schemas
-------

An initial configuration for an application is defined in a schema file. This XML formatted text file then will be transformed into its machine readable equivalent.

This is an example for a schema file with one property (key):

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

The nomenclature for the file is "``schema.id.gschema.xml``".
The standard installation directory for schema files is ``/usr/share/glib-2.0/schemas``. Schema files can also be stored outside of this folder (p.e. local, for testing purposes) but these will not be shown by dconf-editor.

Now the schema files must be compiled

.. code:: bash

    glib-compile-schemas /path/to/schema/files/
    #default directory
    glib-compile-schemas /usr/share/glib-2.0/schemas/

The compiled file which is now used by GSettings is named ``gschemas.compiled``.

Glade
-----

For displaying image files the *GtkImage* widget is required. All controls of the example app are placed in the headerbar:

 * "Open File" button: opens `FileChooserDialog <link://slug/fcdialog>`_
 * switch: turns desktop icons on or off
 * "Fav" togglebutton: bookmarks file drawn in the image widget, shows whether image file is bookmarked as favourite
 * "Set as wallpaper" button: use file as background image
 * *MenuButton*: list of bookmarked files

Python
------

Load global schema
******************

Load an existing configuration:

.. code:: python

    setting = Gio.Settings.new("full.schema.path")
    #load desktop background configuration
    setting = Gio.Settings.new("org.gnome.desktop.background")

Load local schema
*****************

If the schema file is not stored in the standard directory the location of the ``schemas.compiled`` file must be given first:

.. code:: python

    schema_source = Gio.SettingsSchemaSource.new_from_directory(os.getcwd(), 
                Gio.SettingsSchemaSource.get_default(), False)
    schema = Gio.SettingsSchemaSource.lookup(schema_source,"org.example.wallpaper-changer",False)
    setting = Gio.Settings.new_full(schema, None, None)

Bind widget
***********

It is possible to directly bind GSettings properties to a widget. Property statuses then can be displayed or manipulated:

.. code:: python

    setting.bind("setting-key", widget, property, Gio.SettingsBindFlags...)

In the example app this is done with the switch widget:

.. code:: python

    self.bg_setting.bind("show-desktop-icons", self.obj("switch"), "active", Gio.SettingsBindFlags.DEFAULT)

The switch shows the current configuration status on application startup. Changes on the switch control button are applied instantly.

Get and set values
******************

Property settings can be retrieved and defined by ``get_"type"`` and ``set_"type"``. The relevant function to use is dependent on the key type, use ``get_string`` and ``set_string`` for strings, ``get_int`` and ``set_int`` for interger and so on (see `PyGObject API Reference <https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html>`_).

A property value request via ``get_value(key)`` returnes a value of type `GLib.Variant <https://lazka.github.io/pgi-docs/#GLib-2.0/classes/Variant.html#GLib.Variant>`_.
Therefore the  ``set_value(key)`` function also requires this datatype.

Value contents can be converted into simple datatypes:

.. code:: python

    #return string
    setting.get_value(key).get_string()
    #return anything (list, string, bool etc.)
    setting.get_value(key).unpack()
    
and vice versa:

.. code:: python

    setting.set_value(key, GLib.Variant(string_type, value)

The `GNOME developer documentation <https://developer.gnome.org/glib/stable/gvariant-format-strings.html>`_ provides a list of avaliable string types.

In the example app this is used to update the bookmark list:

.. code:: python

    app_setting.set_value("favourites", GLib.Variant('as',fav_list))



Links
-----

 * `Standardeinstellungen in GSettings ändern (German) <https://www.florian-diesch.de/doc/gnome3/standardeinstellungen-in-gsettings-aendern.html>`_
 * `Introduction to GSettings in Python <http://zderadicka.eu/gsettings-flexible-configuration-system/>`_
 * `Short Example of GSettings Bindings with Python using a Gtk Switch <https://marianochavero.wordpress.com/2012/04/03/short-example-of-gsettings-bindings-in-python/>`_
 * `GSettings - flexible configuration system <http://zderadicka.eu/gsettings-flexible-configuration-system/>`_
 * `dconf (ubuntuusers-Wiki) <https://wiki.ubuntuusers.de/GNOME_Konfiguration/dconf/>`_
 * `First steps with GSettings <https://blog.gtk.org/2017/05/01/first-steps-with-gsettings/>`_

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
