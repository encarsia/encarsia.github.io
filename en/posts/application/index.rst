.. title: Stand-alone
.. slug: application
.. date: 2017-01-14 13:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Run program as GtkApplication**

*GtkApplication* handles different important aspects of a GTK+ application like GTK+ initialization, session management and desktop integration.

.. thumbnail:: /images/14_application.png

XML files
---------

Glade
*****

Glade is used as usual, main windows should be **GtkApplicationWindows*. As example the file from the `dialogue article <link://slug/dialoge>`_ is reused.

GMenu
*****

The GNOME Shell supports appmenus residing in the (top) panel. The Gmenu XML file must be formatted to be recognized as *GioMenu*:

.. code-block:: xml

 <?xml version="1.0"?>
 <interface>
  <menu id="appmenu">
     <section>
       <item>
         <attribute name="label" translatable="yes">Menu Item</attribute>
         <attribute name="action">app.item</attribute>
       </item>
     </section>
   </menu>
 </interface>

Glade identifies this file format as an outdated Glade file and refuses to open it. Apart from that *GtkBuilder* can handle the menu and address identifiers.

Python
------

Initialize *GtkApplication*
***************************

The initialization process requires the parameters *application_id* and *flags*. Flags can normally set to 0 being the same as FLAGS_NONE (see `Gio.ApplicationFlags <https://lazka.github.io/pgi-docs/Gio-2.0/flags.html#Gio.ApplicationFlags>`_), naming conventions for application_id are `listed here <https://people.gnome.org/~gcampagna/docs/Gio-2.0/Gio.Application.id_is_valid.html>`_.

The application can be connected to different signals being emitted on preassigned events. It is mandatory to at least define an ``activate`` signal:

.. code-block:: python

    def __init__(self):
        
        self.app = Gtk.Application.new("org.application.test", 0)
        #self.app.connect("startup", self.on_app_startup) #optional
        self.app.connect("activate", self.on_app_activate)
        #self.app.connect("shutdown", self.on_app_shutdown) #optional

    def on_app_activate(self, app):

        #setting up GtkBuilder etc.
        ...
        ...
        ...

Appmenu
*******

GMenu XML files are loaded by *GtkBuilder*:

.. code-block:: python

    builder.add_from_file("menu.ui")
    app.set_app_menu(builder.get_object("appmenu"))

Menu entries now have to be connected to actions which are created as *GioSimpleActions*:

.. code-block:: python

    def add_simple_action(self, name, callback):
        action = Gio.SimpleAction.new(name)
        action.connect("activate", callback)
        self.app.add_action(action)

In the example file actions invokes dialog windows.

Start and quit
**************

*GtkApplication* takes over the handling of the GTK+ mainloop so there is no need of starting and quitting GTK+ manually and ``run()`` and ``quit()`` called instead:

.. code::

    Gtk.main()      ->  app.run(argv)
    Gtk.main_quit() ->  app.quit()

Links
-----

 * `GNOME Developer: GtkApplication <https://developer.gnome.org/gtk3/stable/GtkApplication.html>`_
 * `How to use GTK+ 3 in Python to manage your whole application <http://www.bachsau.com/2015/07/13/how-to-use-gtk-3-in-python-to-manage-your-whole-application/>`_
 * `Stackoverflow: How to create a complete menu using GIO Actions in PyGI GTK? <http://stackoverflow.com/questions/19481439/how-to-create-a-complete-menu-using-gio-actions-in-pygi-gtk>`_

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 13_dialoge.glade xml

GMenu
*****

.. listing:: 14_giomenu.ui xml

Python
******

.. listing:: 14_application.py python
