.. title: Selbständig
.. slug: application
.. date: 2017-01-14 13:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Programm als GtkApplication laufen lassen**

*GtkApplication* handhabt verschiedene wichtige Aspekte einer GTK+-Anwendung, wie etwa der GTK+-Initialisierung, dem Sessionmanagement und der Desktopintegration.

.. thumbnail:: /images/14_application.png


XML-Dateien
-----------

Glade
*****

In Glade verändert sich im Prinzip nichts. Als Hauptfenster sollten *GtkApplicationWindows* zum Einsatz kommen. Als Beispiel wird hier das Gladefile aus dem `Artikel zu Dialogen <link://slug/dialoge>`_ wieder verwendet.

GMenu
*****

Die GNOME-Shell unterstützt Appmenüs, erreichbar über das obere Panel. Die XML-Datei muss so formatiert sein, dass sie als *GioMenu* erkannt wird:

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

Von Glade selbst würde diese XML-Datei als veraltetes Format erkannt, aber sie lässt sich trotzdem von *GtkBuilder* laden und anschließend kann man die Identifier nutzen.

Python
------

Initialisierung von *GtkApplication*
************************************

Bei der Initialisierung wird eine *application_id*- und *flags*-Angabe benötigt. Letztere können in der Regel bei 0 bzw. FLAGS_NONE belassen werden (siehe `Gio.ApplicationFlags <https://lazka.github.io/pgi-docs/Gio-2.0/flags.html#Gio.ApplicationFlags>`_), die Konventionen für die application_id sind `hier dokumentiert <https://people.gnome.org/~gcampagna/docs/Gio-2.0/Gio.Application.id_is_valid.html>`_.

Die Application kann nun mit verschiedenen Signalen verbunden werden, die zu bestimmten Ereignissen ausgelöst werden, aber es muss mindestens ``activate`` verbunden werden:

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

Wie oben bereits erwähnt, lässt sich die GMenu-XML von *GtkBuilder* laden, dann wird das Menü der Application zugewiesen:

.. code-block:: python

    builder.add_from_file("menu.ui")
    app.set_app_menu(builder.get_object("appmenu"))

Die zu den Menüeinträgen verknüpften Funktionen müssen nun als Actions, genauer *GioSimpleActions*, erstellt und analog zur herkömmlichen Signalverknüpfung über ``connect`` verbunden werden.

.. code-block:: python

    def add_simple_action(self, name, callback):
        action = Gio.SimpleAction.new(name)
        action.connect("activate", callback)
        self.app.add_action(action)

Im Beispiel werden Actions zum Aufrufen der Dialoge erstellt.

Starten und Beenden
*******************

*GtkApplication* übernimmt die Handhabung des GTK+-Mainloops, das heißt, es nicht mehr notwendig GTK+ manuell zu starten oder zu beenden. Stattdessen werden ``run()`` und ``quit()`` verwendet:

.. code::

    Gtk.main()      ->  app.run(argv)
    Gtk.main_quit() ->  app.quit()

Beendet man das Programm über den [X]-Button oder den "Schließen"-Eintrag des Appmenus (immer vorhanden), wird automatisch das "shutdown"-Signal ausgelöst (siehe oben). Das heißt, es müssen keine entsprechenden Signale definiert werden. "Shutdown" wird auch ausgelöst, wenn bei der Initialisierung nicht mit einer Funktion verbunden wird.

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
