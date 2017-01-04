.. title: Drei-Gänge-Menü
.. slug: drei-gange-menu
.. date: 2016-11-07 22:10:09 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Menüs, Toolbars und Statusbar**

Glade
-----

.. thumbnail:: /images/05_menutoolbar.png


Menü
****

Das Menü-Element findet man unter den Containerelementen, es benötigt aber selbst eine leere Box. Es wird zunächst ein Standard-Menü angelegt, das sich bequem über "Edit..." in einem separaten Fenster bearbeiten lässt. Sehr simpel erfolgt das Anlegen von Shortcuts im "Edit..."-Fenster unter "Hierarchie > Eigenschaften > Tastenkürzel". Dort weist man der Tastenkombination ein Signal zu (im Falle von Menüeinträgen *activate*). Die Information erscheint im Menü automatisch, aber nicht in der Glade-Vorschau. Examplarisch wurden Shortcuts zum Beenden (Strg+Q) und zum Einblenden des About-Dialogs (Strg+I) angelegt.

Toolbar
*******

Toolbars können verschiedene Widgets wie Buttons, Togglebuttons, Radiobuttons oder (Unter-)Menüs enthalten. Die Erstellung und Bearbeitung erfolgt analog zum Menü über "Edit...".

Statusbar
*********

In der Statusbar können kurze Meldungen/Nachrichten eingeblendet werden. Die Meldungen werden analog zu einer Liste behandelt, das Widget bietet die Funktionen ``push`` und ``pop``.

.. TEASER_END

.. listing:: 05_menutoolbar.glade xml

Python
------

Um Nachrichten an die Statusbar zu senden, bedient man sich einfach der Funktion

.. code-block:: python

    widget.push(content_id,message)

Wenn man Meldungen ausschließlich "obendrauf" einblendet, kann man als content_id eine beliebige Zahl angeben, zum Beispiel ``0``.

.. listing:: 05_menutoolbar.py python

