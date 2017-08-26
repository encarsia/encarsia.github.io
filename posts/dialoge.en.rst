.. title: Dialogues
.. slug: dialoge
.. date: 2016-12-31 17:51:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Handle dialogue windows**

Dialogues are complementary windows which are useful in interaction with the user, to show some relevant information or demand input. The *GtkDialog* class provides subclasses for common dialogue use cases like the *AboutDialog* and *MessageDialog* used in the example file. (`FileChooserDialog article <link://slug/fcdialog>`_).

.. thumbnail:: /images/13_dialoge.png

Glade
-----

In the widget sidebar dialog widgets are integrated to the *"Toplevel*" section next to window widgets.

Dialogs are complementary windows to grab the user's focus. They can fixed to a superordinated window but at least be configured transient to a parent window via *General > Window Attributes Transient For:"*.

AboutDialog
***********

The "About" dialog window in general gives information about the project, its version, license, participating programmers, translators etc. All this can be directly typed into Glade.

MessageDialog
*************

The MessageDialog is a standard dialog to show information or call for input. It is configurated to be drawn without window decoration or showing up seperately in the taskbar. Furthermore there is the possibility to add standard buttons.

Buttons and responses
*********************

Dialogs already own an intern *GtkButtonBox* to place any buttons in.

In constrast to regular windows the *clicked* signals of the buttons do not have to be assigned in these Buttonboxes (it's still possible to do so, of course). Instead in the *"General"* button properties you define a response answer (int) and assign the *response* signal of the *GtkDialog*.

Standard buttons available for example in MessageDialogs have a fixed response (see also `Python GI API Reference <https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.ResponseType>`_):

 * **Ok** -5
 * **Abort** -6
 * **Close** -7
 * **Yes** -8
 * **No** -9
 * **[X]** -4

The huge advantage of that procedure is that the response refers to the dialog object so the responses can be processed by a single function. 

Reestablish dialogues
*********************

The problem of windows closed via *destroy* signal is that they cannot be reactivated therefore the *delete-event* signal is used here.

Python
------

Responses
*********

When emitting the *response* signal the response is passed as parameter. As said before this offers the option to process all responses in one function:

.. code-block:: python

    def on_dialog_response(self,widget,response):
        if response == 0:
            widget.hide_on_delete()
        elif response == 1:
            do.something()
        elif response == (2 or 3):
            do.something.different()

Delete-event
************

The ``hide_on_delete()`` function removes a window but can be reestablished by ``show_all()``:

.. code-block:: python

    def on_dialog_delete_event(self,widget,event):
        widget.hide_on_delete()
        return True

Several Glade files
*******************

As `mentioned before <link://slug/fenster-mit-aussicht>`_ several Glade files can be used within a project. It is not possible though to associate dialogs with their parent window if separated into different files. So the ``set_transient_for`` function of *GtkWindow* is required:

.. code-block:: python

    dialog.set_transient_for(mainwindow) 

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 13_dialoge.glade xml

Python
******

.. listing:: 13_dialoge.py python
