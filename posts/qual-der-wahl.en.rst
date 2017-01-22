.. title: Spoilt for choice
.. slug: qual-der-wahl
.. date: 2016-11-11 15:28:18 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Spinbutton and Combobox**

Named widgets simplify input of values by providing a value list or range. Value input is normally done via mouseclicks, key input is optional.


Glade
-----

.. thumbnail:: /images/08_combospin.png

Spinbutton
**********

In Glade some properties of spinbutton widgets can be set like the minimum/maximum/default value. It is required to tie a *adjustment* widget to the spinbutton. To do so select *"General > Spin Button Attributes > Adjustment"* and assign or create an adjustment.

Looking at the example file the two spinbuttons represent month and year dates. The month spinbutton is set to be circular, the minimum value follows after passing the maximum value. This act emits the *wrapped* signal which is assigned to then adjust the year date of the second spinbutton.

Combobox
********

There are two different combobox widgets in GTK+:

GtkComboboxText
    The list items of the dropdown menu are strings directly that are directly set in the Glade widget properties

GtkCombobox
    The list items are stored in a ListStore or TreeStore element that can hold data sets instead of a plain list. These data stores are accessible to different widgets (see the `"List article" <link://slug/uberlistet>`_).

Both widgets can include an optional entry widget which has to be activated in *"General > Has Entry"*. By activating an internal *GtkEntry* widget is created. It is important to set *"Common > Widget Flags > Can focus*".

The first ComboboxText widget in the exampe does not possess an entry field, the user can only select an item from the list. In both widgets the *changed* signal is assigned to retrieve the selection.

Python
------

Spinbutton
**********

The value of a spinbutton can be easily retrieved and set via ``get_value`` and ``set_value``.

In the example the values for the month and year date are set with the current dates. The ``on_spin_m_wrapped`` function changes the year date up or down according to the value set in month date.

Combobox
********

Combobox lists can be extended by using the ``append`` function, p.e.

.. code-block:: python

    [self.builder.get_object("comboboxtext2").append(None,entry) for entry in ("foo","bar","yes","no")]

You get the selected item by calling ``widget.set_active_text()`` which also passes the text of the optional text entry widget.

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 08_combospin.glade xml

Python
******

.. listing:: 08_combospin.py python

