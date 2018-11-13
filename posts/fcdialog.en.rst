.. title: File chooser dialog
.. slug: fcdialog
.. date: 2017-02-01 23:22:02 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**FileChooserDialog**

The *GtkFileChooserDialog* is a subclass of *GtkDialog* (see `diaogue article <link://slug/dialoge>`_) and provides opening and saving of files and folders.

.. thumbnail:: /images/16_fcd.png

Glade
-----

The dialog can be added from the *"Toplevel*" section of the widget sidebar. In addition to the file browser itself the widget has an intern *GtkBox* for additional widgets and a *GtkButtonBox* as "action area" for buttons.

First the *Gtk.FileChooserAction* mode must be defined (see `Python GI API Reference <https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.FileChooserAction>`_): open or save file, choose or create a folder.

Action area and Responses
*************************

The *response* signal is emitted on widget interaction in the action area which also passes the response value. So for these widgets there is no need to activate the *clicked* signal of buttons.

By default the "action area" is generated beneath the file browser area.

.. thumbnail:: /images/16_fcd_glade.png

If the *FileChooserDialog* is used without Glade (see below) the buttons are created in the headerbar. This seems to be standard procedure because Glade generated dialogs induce the warning

.. code::

 Gtk-WARNING **: Content added to the action area of a dialog using header bars

This message is not shown if buttons are not added to the intern action area.

If a headerbar with buttons is created in Glade the buttons cannot be assigned to a response value.

There may be several solutions to the problem:

XML file
========

After creating a headerbar with button(s) the Glade file is opened in a text editor and add line(s) to the ``<action-widgets>`` element:

.. code-block:: xml

  <object class="GtkFileChooserDialog" id="filechooser_dialog">
    <property ... ></property>
    <property ... ></property>
    <!-- ... -->
    <action-widgets>
      <!-- Buttons innerhalb der action area -->
      <action-widget response="0">button1</action-widget>
      <action-widget response="1">button2</action-widget>
      <!-- Button in Headerbar -->
      <action-widget response="-1">hb_button</action-widget>
    </action-widgets>
    <!-- ... -->
  </object>

This works but this procedure is surely not the intended way to deal with the problem because after altering the Glade file the edit is retracted.

add_action_widget function
==========================

The ``add_action_widget`` adds activatable widgets to the action area and hold a response value. This includes widgets of the *Gtk.Activatable* class: *Buttons*, *MenuItem*, *RecentChooserMenu*, *Switch* and *ToolItem*.

The scheme for creating a button is

.. code:: python

 widget.add_action_widget(button,response)

The widget property "can-default" of the button must be activated:

.. code:: python

 button.set_property("can-default",True)

In the example the standard buttons "apply/cancel" are added to the file dialog:

.. code-block:: python

    button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
    button.set_property("can-default",True)
    self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.CANCEL)
    button = Gtk.Button.new_from_stock(Gtk.STOCK_APPLY)
    button.set_property("can-default",True)
    self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.OK)

To apply file selection on doubleclick the *file-activated* is also required in addition to the *response* signal.

Preview widget
**************

The dialogue can contain an optional preview widget. To use it activate *"Preview Widget Active"* and choose a free widget (p.e. a *GtkImage*). It may be necessary to create the preview widget in an empty container widget and pull it into a free area.

If the preview requires a refresh the *update-preview* signal is emitted.

FileFilter
**********

Files can be filtered according to certain criteria by using *FileFilter*. There can be defined several (shell style glob) patterns or MIME-types for each filter.

In Glade filters can be found in the widget sidebar in the *"Miscellaneous"* group. A filter for a dialog can be selected in the general widget properties. This corresponds to the ``set_filter`` function.

Python
------

Dialog without Glade
********************

The *FileChooserDialog* is a complex but also easy to use graphic interface item. Realizing the dialog without Glade also avoids the headerbar problem discussed above. Creating a dialog follows the scheme

.. code-block:: python

 dialog = Gtk.FileChooserDialog("window title",
                                parent_window,
                                file_chooser_action,
                                (button1,response1,
                                button2,response2))

The dialog then can be directly run and processed:

.. code-block:: python

 response = dialog.run()
 if response == response1:
     ...
 elif response == response2:
     ...
 dialog.destroy()


FileFilter
**********

There are two possibilities to apply a *FileFilter*:

1. No user choice. The applied filter is preset:

.. code:: python

 dialog.set_filter(filter)

2. Selection per dropdown menu. The user can choose between different defined filters:

.. code:: python

 dialog.add_filter(filter1)
 dialog.add_filter(filter2)
 ...

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 16_filechooser.glade xml

Python
******

.. listing:: 16_filechooser.py python

