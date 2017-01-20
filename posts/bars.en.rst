.. title: Bars
.. slug: bars
.. date: 2016-11-08 14:20:08 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Progressbars and levelbars**

Glade
-----

.. thumbnail:: /images/06_progresslevel.png

Progressbar
***********

Progressbars usually show the current state of a longer lasting process. The widget offers two operation modes:

1. proportional mode, the progress is expressed by a value between 0 and 1
2. activity mode, a block moves back and forth 

The widget posseses an optional text field. It shows the progress in percent if the field content is not specified otherwise.

Levelbar
********

Levelbar widgets are used as level indicators. The level is visualized like in a progressbar but it has some more properties:

1. Two operation modes:

    1. *continous*: one single block represents the value
    2. *discrete*: the levelbar is split into a defined number of blocks, each block represents a value range

2. Define minimum/maximum value, default is 0/1; the default number of blocks in discrete mode corresponds to the maximum value

3. Change colours when exceeding predefined values (see also `CSS article <link://slug/css>`_)

Python
------

Progressbar
***********

In the example the first progressbar operates in proportional mode, the second in activity mode. The latter does not show the progress in the text field, this has to be accomplished manually:

.. code-block:: python

    widget.pulse()
    widget.set_text("%d %%" % perc_value)


Levelbar
********

What ``set_fraction`` is for progressbar is ``set_value`` for levelbar. This is self-explanatory for the continous mode. In discrete mode the number of blocks have to be factored in:

.. code-block:: python

    widget.set_value(fraction*blocks)

For the ``add_offset_value`` function and colour schemes read the `CSS article <link://slug/css>`_.

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 06_progresslevel.glade xml

Python
******

.. listing:: 06_progresslevel.py python
