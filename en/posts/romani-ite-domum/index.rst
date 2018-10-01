.. title: Romani ite domum
.. slug: romani-ite-domum
.. date: 2016-11-28 14:50:22 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Localization with gettext and locale**

.. thumbnail:: /images/10_lokalisation.png

Glade
-----

Strings in widgets are by default configurated as translatable so there are no preparations required. GetText directly provercesses Glade project files.

Python
------

Translatable strings
********************

Approved translatable strings are recognized by ``xgettext`` by brackets with a leading underscore:

.. code:: python

    _ = gettext.gettext
    translatable_string = _("translate me")

configure (bind)textdomain
**************************

Now name and location of the MO files have to be configured in the source code:

.. code:: python

        locale.bindtextdomain(appname,locales_dir)
        locale.textdomain(locales_dir)
        gettext.bindtextdomain(appname,locales_dir)
        gettext.textdomain(appname)
        builder.set_translation_domain(appname)

``set_translation_domain`` has to be called before loading Glade files.

GetText
-------

POT
***

POT is the abbrevation for Portable Object Template. This file contains all original translatable strings. After generating an empty POT file, ``xgettext`` is executed for all source files containing translatable strings:

.. code:: console

    $ xgettext --options -o output.pot sourcefile.ext

The identified strings are added to the POT file.

.. code-block:: console

    #: sourcefile.ext:line number
    msgid "translatable string"
    msgstr ""

The file number reference comment can be avoided by passting the option ``--no-location``.

In this article's example it is required to run xgettext once for the Glade file and once for the Python source code; the ``-j`` (``--join-existing``) option adds new found strings to an existing file:

.. code:: console

    $ xgettext --sort-output --keyword=translatable --language=Glade -j -o 10_localization/TUT.pot 10_lokalisation.glade
    $ xgettext --language=Python -j -o 10_localization/TUT.pot 10_lokalisation.py 

PO
**

Translated strings are stored in a PO file per language. A new translation ist invoked by

.. code:: console

    $ msginit --input=source.pot --locale=xx
    # xx=language code

that generates a file after the pattern xx.po (p.e. de.po). This file can be edited in any text editor or dedicated tools such like `PoEdit <https://poedit.net/>`_. A German localization for example is created by the command

.. code:: console

    $ msginit --input=TUT.pot --locale=de

If the POT file is altered the PO files are updated with the new strings by executing ``msgmerge``:

.. code:: console

    $ msgmerge lang.po template.pot > new_lang.po

MO
**

MO files are (machine readable) binary files and mandatory for gettext to work. Localization files are located below the *bindtextdomain* following the file structure ``path/to/bindtextdomain)/locale/language code/LC_MESSAGES/appname.po``.

In the example the bindtextdomain is created in the local directory, the generated `de.po` translation text file then transformed into the  corresponding MO file:

.. code:: console

    $ msgfmt --output locale/de/LC_MESSAGES/TUT.mo de.po

Tipps
*****

xgettext options
================

``--no-location``
    Oppress writing line number(s) and file name as comment

``--omit-header``
    Avoid overwriting header information

Remove obsolete strings
=======================

Strings that are removed from the template remain in the translation files. You can get rid of these by executing this command:

.. code:: bash

    $ msgattrib --set-obsolete --ignore-file=PRJ.pot -o xx.po xx.po


.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 10_lokalisation.glade xml

Python
******

.. listing:: 10_lokalisation.py python

POT
***

.. listing:: 10_localization/TUT.pot bash
