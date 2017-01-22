.. title: Desktop integration
.. slug: application-fortsetzung
.. date: 2017-01-15 13:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Desktop integration: icon, headerbar, commndline options**

(Continuation if the `GtkApplication article <link://slug/application>`_)

.. thumbnail:: /images/15_application.png

Glade
-----

Icon
****

To assign an icon to an window just select *"General Appearance > Icon File"*. Problematic here is that Glade only shows image files located in the same folder as the Glade file even if an image from another folder is chosen.

A simple solution is editing the Glade file in a text editor and add the relative path to the `icon <https://openclipart.org/detail/22535/ducky-icon>`_. This edit is preserved even when changing and saving the file with Glade again:

.. code-block:: xml

  <object class="GtkApplicationWindow" id="window">
    ...
    <!-- <property name="icon">duckyou.svg</property> -->
    <property name="icon">../files/duckyou.svg</property>
    ...

Headerbar
*********

Headerbars were introduced in GNOME 3.10 and unite titlebar and toolbar. Besides title and subtitle there is room for widgets such as buttons or menus and client side window controls.

A headerbar is optional. To make use of it *"General > Appearance > Client side window decorations"* has to be activated if not set yet. This prepares a reserved container area in the upper window area to add the headerbar widget in. If a headerbar is placed out of this specific area a regular titlebar is generated in addition to the headerbar.

.. image:: /images/15_headerbarglade.png

Commandline options
-------------------

*GtkApplication* provides functions to define individual commandline options of the applications (`Handling command line options in GApplication <https://wiki.gnome.org/HowDoI/GtkApplication/CommandLine>`_).

Create Options
**************

Options are added by the ``add_main_option_entries(entrylist)`` function. The entries must be *GLib.OptionEntry* formatted which requires a bunch of parameters.

.. code-block:: python

    def __init__(self):
        self.app = Gtk.Application.new("org.application.test", Gio.ApplicationFlags(0))
        self.app.add_main_option_entries([
            self.create_option_entry("--version", description="Show version numbers and exit"),
            self.create_option_entry("--setlabel", description="Set label widget",arg=GLib.OptionArg.STRING,),
            self.create_option_entry("--bollocks", description="Additional test option - exit"),
        ])

    def create_option_entry(self,long_name, short_name=None, flags=0, arg=GLib.OptionArg.NONE,arg_data=None, description=None, arg_description=None):
        option = GLib.OptionEntry()
        option.long_name = long_name.lstrip('-')
        option.short_name = 0 if not short_name else short_name.lstrip('-')
        option.flags = flags
        option.arg = arg
        option.arg_data = arg_data
        option.description = description
        option.arg_description = arg_description
        return option

Connect signal
**************

The "handle-local-options" signal of *Gtk.Application* handles commandline options. If the signal is connected the signal is emitted before the "startup" signal.

.. code:: python

    self.app.connect("handle-local-options", self.on_local_option)

Processing options
******************

The ``option`` will be passed as an element of the *GLib.VariantDict* class which can be searched for by calling ``contains("option")``:

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

A string can be extracted by calling ``end()`` which converts *GLib.VariantDict* to a *GLib.Variant* element. That *GLib.Variant* then can be culled by calling ``keys()``:

.. code-block:: python

    var = GLib.VariantDict.end(option)
    option_string = var[var.keys()[0]]

The handler function demands a return value that corresponds to the exit status:

    * **-1**: application execution will be continued
    * **0**: execution successful, application will be quit, "startup/activate" will not be emitted
    * **1** or positive value: execution was not successful, application will be quit

Run application with options
****************************

The option ``--help`` is always available and lists all defined options of the application and their descriptions.

The options of the example file now can be executed:

.. code:: console

    $ python script.py --version
    Python: 3.6.0
    GTK+:   3.22.6

or pass a string to the application's *Gtk.Label*:

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
