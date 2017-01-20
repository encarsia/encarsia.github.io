.. title: Clickbaiting
.. slug: clickbaiting
.. date: 2016-11-05 16:01:29 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Switch, checkbox, radiobutton - more elements to click on**

This article explains the usage of control and display widgets on the basis of these selected elements. The usage follows the pattern:

1) create container (box, toolbar etc.) for widget
2) add element
3) add an identifier to the element (that step canbe skipped for elements that do not need to be addressed in the source code like boxes or separators)
4) assign a function to a signal
5) (optional) test signal emission in Glade preview window
6) code funtion

All available GTK+ classes and their functions are documented in the `Python GI API Reference >> Gtk 3.0 >> Classes <http://lazka.github.io/pgi-docs/#Gtk-3.0/classes>`_.

.. thumbnail:: /images/04_clickableelements.png

Glade
-----

Switch
******

A switch is a widget that posseses two states, on and off. The current status can be retrieved by the *state_set* signal which is emitted on turning the switch on or off.

Checkbox
********

Checkboxes are basically just togglebuttons therefore the *toggled* signal is allocated.

Radiobutton
***********

The purpose of radiobuttons is the selection of _one_ list item. The widget is also a sub class of *GtkToggleButton* (allocate *toggled* signal).

Every radio button is a member of a group. This is done via *"General > Button Attributes > Group"*. There is one 'leading' radiobutton that are all other radiobuttons bound to.

Python
------

Given that checkboxes and radiobuttons are togglebuttons the status is retrieved by the ``widget.get_active()`` function.

When the *state_set* signal is emitted on the switch a parameter is passed containing the status as boolean (True/False).


.. code-block:: python

    def on_switch_state_set(self,widget,state):
        if state is True:
            print("switch is on")
        else:
            print("switch is off")

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 04_clickableelements.glade xml

Python
******

.. listing:: 04_clickableelements.py python
