.. title: Romani ite domum
.. slug: romani-ite-domum
.. date: 2016-11-28 14:50:22 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Lokalisation mit gettext und locale**

.. thumbnail:: /images/10_lokalisation.png

Glade
-----

Strings von Labels oder Menüs sind standardmäßig als übersetzbar konfiguriert (Checkbox unter "Beschriftung"), insofern muss hier nichts weiter beachtet werden. Glade-Projektdateien werden direkt von GetText verarbeitet.

Python
------

Übersetzbare Strings
********************

Zur Übersetzung freigegebene Strings werden durch eine Einklammerung mit vorausgehendem Unterstrich markiert und beim Aufruf von ``xgettext`` erkannt:

.. code:: python

    _ = gettext.gettext
    translatable_string = _("translate me")

(bind)textdomain einrichten
***************************

Nun muss man Python noch zeigen, unter welchem Namen und Pfad die MO-Dateien (siehe unten) zu finden sind:

.. code:: python

        locale.bindtextdomain(appname, locales_dir)
        locale.textdomain(locales_dir)
        gettext.bindtextdomain(appname, locales_dir)
        gettext.textdomain(appname)
        builder.set_translation_domain(appname)

``set_translation_domain`` muss vor dem Laden der Glade-Datei(en) aufgerufen werden.

GetText
-------

POT
***

POT steht für Portable Object Template und ist dem Namen zufolge die Vorlage für Übersetzungen. Diese Datei enthält alle übersetzbaren Strings. Nachdem eine leere POT-Datei erstellt wurde, ruft man nun ``xgettext`` nach folgendem Muster für alle Quelldateien auf:

.. code:: console

    $ xgettext --options -o output.pot sourcefile.ext

Die erkannten Strings werden nach dem Schema

.. code-block:: console

    #: sourcefile.ext:line number
    msgid "translatable string"
    msgstr ""

der angegebenen POT-Datei hinzugefügt. Die Markierung der Fundstelle(n) des Strings kann mit der Option ``--no-location`` verhindert werden.

Für das Beispiel wird also je ein Aufruf für die Glade- und Python-Datei benötgt:

.. code:: console

    $ xgettext --sort-output --keyword=translatable --language=Glade -j -o 10_localization/TUT.pot 10_lokalisation.glade
    $ xgettext --language=Python -j -o 10_localization/TUT.pot 10_lokalisation.py 

Mit der Option ``-j`` (``--join-existing``) wird eine bestehende Datei um zusätzliche Strings ergänzt und funktioniert deshalb sowohl bei der Initiierung (vorher einfach mit ``touch template.pot`` die leere Datei erstellen) als auch bei erneutem Aufruf zum Aktualisieren neuer Strings.


PO
**

Die übersetzten Strings werden in jeweils einer PO-Datei gespeichert. Eine neue Übersetzung legt man mit

.. code:: console

    $ msginit --input=source.pot --locale=xx
    # xx=language code

an, das eine PO-Datei mit dem Namen xx.po (z.B. de.po) anlegt. Diese kann direkt im Texteditor oder mittels Tools wie `PoEdit <https://poedit.net/>`_ bearbeitet werden. Die deutschsprachige Lokalisation wird also angelegt mit

.. code:: console

    $ msginit --input=TUT.pot --locale=de

Wird die POT-Datei verändert, kann man die PO-Dateien mit ``msgmerge`` abgleichen und anschließend die neuen Strings übesetzen:

.. code:: console

    $ msgmerge lang.po template.pot > new_lang.po

MO
**

MO-Dateien sind auf Maschinenlesbarkeit optimierte PO-Dateien und letztlich die, die vom Programm benutzt werden. Unterhalb der angegebenen *bindtextdomain* liegen die Lokalisationsdateien nach der Verzeichnisstruktur ``(path/to/bindtextdomain)/locale/language code/LC_MESSAGES/appname.po``

Im Beispiel wird die bindtextdomain einfach im lokalen Verzeichnis angelegt, die erzeugte `de.po` wird mit ``msgfmt`` in die MO-Datei überführt:

.. code:: console

    $ msgfmt --output locale/de/LC_MESSAGES/TUT.mo de.po

Tipps
*****

xgettext-Optionen
=================

``--no-location``
    Ausgabe der Zeilennummer(n) und Datei (als Kommentar) des Strings verhindern

``--omit-header``
    Überschreiben der Header-Informationen verhindern

``--sort-output``
    Alphabetische Sortierung der Strings

Obsolete Strings entfernen
==========================

Strings, die aus der POT entfernt werden, bleiben in den Übersetzungen erhalten. Dies lässt sich durch den Aufruf von

.. code:: bash

    $ msgattrib --set-obsolete --ignore-file=PRJ.pot -o xx.po xx.po

beheben.


.. TEASER_END

Listings
--------

Python
******

.. listing:: 10_lokalisation.py python

Glade
*****

.. listing:: 10_lokalisation.glade xml

POT
***

.. listing:: 10_localization/TUT.pot bash
