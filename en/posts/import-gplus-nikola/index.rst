.. title: Nikola-Import-Plugin für Google+
.. slug: import-gplus-nikola
.. date: 2018-10-17 15:25:00 UTC+02:00
.. tags: nikola,google+
.. category: socialmedia
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

Das Ende ist nah
================

Häufig wurde das Ende von Google+ herbeigeunkt. Nun, da es tatsächlich in etwa einem Jahr so weit ist, weicht Geschäftigkeit dem ersten Schock.

In weiser Vorraussicht beschäftigte ich mich bereits vor einer Weile damit, die Daten brauchbar zu konservieren und entschied mich für eine Lösung mit dem statischen Webseitengenerator Nikola_: `Verloren im Kaninchenbau von Google Takeout <link://slug/google-takeout>`_.

.. figure:: /images/takeout_gplus_slow.gif

    Resultat der Nikola-generierten Seite mit hyde-Thema

Vorbereitungen
==============

Google Takeout
**************

Zunächst benötigt man die Daten aus dem `Takeout <https://takeout.google.com/settings/takeout>`_. Da sich hier große Datenmengen ansammeln, ist es ratsam, keine weiteren außer Googe+-relevanten Produkte auszuwählen:

* Button "Nichts auswählen", dann *"Stream in Google+"* aktivieren
* Als Dateiformat HTML wählen
* Als Archivformat **zip** wählen, bei tar.gz kann es Encodingprobleme geben
* Nach Fertigstellung kann das/die Archiv/e heruntergeladen  und entpackt werden
* die *index.html* gibt Hinweise auf Fehler bei der Archiverstellung

Nikola
******

1. Installation:
    Nikola kann über pip oder je nach verwendeter Distribution über die Paketverwaltung installiert werden: `Getting Started <https://getnikola.com/getting-started.html>`_.

2. Initialisierung:
    Das Plugin kann in einer bestehenden mit Nikola verwalteten Webseite erstellt werden. Es ist aber auch möglich, für diesen Verwendungszweck eine neue leere Seite zu erstellen, die dann später wieder gelöscht wird:

.. code:: bash

    $ nikola init gplus_dummy_site

3. Plugin installieren:
    Das Plugin aus dem als Archiv herunterladen und enpacken oder das Repository klonen: `encarsia/gplus_nikola_import <https://github.com/encarsia/gplus_nikola_import>`_. Den Ordner in die im vorigen Schritt angelegten Seite in den anzulegenden ``plugins``-Ordner kopieren.

4.  Optional:
    Um die Übersicht zu behalten, kann man auch den Takeout-Ordner in die Nikola-Seite verschieben.

Import ausführen
================

Dateistruktur
*************

Bevor der Import ausgeführt wird, sollte man einen Blick in die ``import_gplus_html.py`` werfen. Die Ordnerbezeichnungen entsprechen der deutschen Spracheinstellung des Takeouts, bei abweichender Spracheinstellung muss man hier die entsprechenden Bezeichnungen der Dateistruktur anpassen.

Es werden Beiträge nach Verteilungsstatus unterschieden:

1. *Öffentlich* geteilt
2. Mit *Meinen Kreisen* geteilt
3. Mit *Erweiterten Kreisen* geteilt
4. Mit bestimmten Kreisen oder Personen/Profilen geteilt
5. Beiträge in *Communites*
6. Beiträge in *Sammlungen*

Beiträge filtern
****************

Mit der Option ``import_private`` lässt sich einstellen, ob mit bestimmten Kreisen oder Personen/Profilen geteilte Beiträge importiert werden sollen.

Die Option ``import_com`` schaltet den Import von Communitybeträgen ein oder aus. Dabei wird nicht nach öffentlichen oder geschlossenen Communities unterschieden.

Import
======

Im ``gplus_dummy_site``-Verzeichnis führt man nun den Import aus, dabei wird als Argument der Ordner des entpackten Takeout-Verzeichnisses übergeben:

.. code:: bash

    $ nikola import_gplus_html takeout

Nikola initialisiert eine neue Seite namens "new_site", dort werden alle Posts, die dazugehörigen Metadaten und die Mediendateien gespeichert.

Statische Seite erstellen
=========================

conf.py
*******

Nun wechselt man in das neue Verzeichnis "new_site", das wiederum eine Nikola-Instanz ist. 

Dort befindet sich die Konfigurationsdatei ``conf.py``. In dieser lassen sich nun Anpassungen vornehmen. Da im Beispiel das Thema `hyde <https://themes.getnikola.com/v7/hyde/>`_ verwendet wird, wird dieses hier gleich angepasst, außerdem RSS deaktiviert:

.. code:: python

    THEME = "hyde"
    GENERATE_RSS = False

Thema
*****

Hyde ist ein perönlicher Favorit und wird deshalb hier installiiert:

.. code:: bash

    $ nikola theme -i hyde

Im Pluginordner befindet sich eine CSS-Datei ``custom.css``, die einige optische Anpassungen für diesen Anwendungsfall enthält, diese einfach in das Verzeichnis ``themes/hyde/assets/css`` kopieren.

Grundsätzlich funktioniert die Seite mit jeden Theme. Eine Liste der verfügbaren `Themes <https://themes.getnikola.com>`_ erhält man folgendermaßen:

.. code:: bash

    $ nikola theme -l   # installierbar
    $ nikola theme --list-installed     # installiert

Um ein Thema zu verwenden, muss es in der ``conf.py`` angegeben und die Seite neu gebaut werden. Ein erneuter Datenimport ist natürlich nicht notwendig.

Build
*****

Die eigentliche Generierung der Seite erfolgt zum Schluss mit

.. code:: bash

    $ nikola build

Den lokalen Server startet man mit

.. code:: bash

    $ nikola serve
    [2018-10-18T09:57:02Z] INFO: serve: Serving on http://127.0.0.1:8000/ ...

Screenshots
===========

.. figure:: /images/GPlus_plugin/postview.png
    :scale: 100 %

    Beitragsansicht (Postception!)

.. figure:: /images/GPlus_plugin/archiv.png
    :scale: 100 %

    Archiv

.. figure:: /images/GPlus_plugin/sharestatus.png
    :scale: 100 %

    Der Verteilungsstatus ist als Kategorie erfasst

.. figure:: /images/GPlus_plugin/cat_ubersicht.png
    :scale: 100 %

    Kategorieansicht

Links
=====

* Hier: `Verloren im Kaninchenbau von Google Takeout <link://slug/google-takeout>`_
* Hier: `The Notwork - lasst G+ sterben <link://slug/diegplusdie>`_
* Import-Plugin für Nikola_: `gplus_nikola_import <https://github.com/encarsia/gplus_nikola_import/>`_
* Alternative mit G+-Import: `net2o <https://git.net2o.de/bernd/net2o>`_ - reinvent the internet, `Bernd Paysan auf G+ <https://plus.google.com/+BerndPaysan>`_


.. _Nikola: https://getnikola.com/
