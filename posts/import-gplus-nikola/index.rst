.. title: Nikola-Import-Plugin für Google+
.. slug: import-gplus-nikola
.. date: 2019-02-03 10:25:00 UTC+02:00
.. tags: nikola,google+
.. category: socialmedia
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

.. note::

    Der Countdown des Shutdowns läuft nun endgültig.
    Der Artikel wurde hinsichtlich einiger Veränderungen ergänzt:

    * Importfilter
    * Konfigurationsdatei
    * Post-Analyse mit der Option ``-s``
    * Wasserzeichen zu Imagedateien hinzufügen

Das Ende ist nah
================

Häufig wurde das Ende von Google+ herbeigeunkt. Nun, da es tatsächlich am 2. April 2019 so weit ist, weicht Geschäftigkeit dem ersten Schock.

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
    Zuerst das Plugin als Archiv herunterladen und entpacken oder das Repository klonen: `encarsia/gplus_nikola_import <https://github.com/encarsia/gplus_nikola_import>`_. Anschließend muss man noch den Ordner in die im vorigen Schritt angelegten Seite in den noch anzulegenden ``plugins``-Ordner kopieren.

4.  Optional:
    Um die Übersicht zu behalten, kann man auch den Takeout-Ordner in die Nikola-Seite verschieben.

Import ausführen
================

Dateistruktur
*************

Vor dem Ausführen des Imports öffnet man zunächst die Konfigurationsdatei ``config.yaml``. Hier lassen sich zum Beispiel Filteroptionen einstellen.

Die Ordnerbezeichnungen entsprechen der deutschen Spracheinstellung des Takeouts, bei abweichender Spracheinstellung muss man hier die entsprechenden Bezeichnungen der Dateistruktur anpassen.

Es werden Beiträge nach Verteilungsstatus unterschieden:

1. *Öffentlich* geteilt
2. Mit *Meinen Kreisen* geteilt
3. Mit *Erweiterten Kreisen* geteilt
4. Mit bestimmten Kreisen oder Personen/Profilen geteilt
5. Beiträge in *Communites*
6. Beiträge in *Sammlungen*

.. tip::

    Um sich einen Überblick zu verschaffen, kann man die die Plugin-Option ``-s`` nutzen. Damit werden die Verteilungsstatus aller Beiträge analysiert und aufgelistet, ohne dabei den eigentlichen Import auszuführen.

    .. code:: console

        $ nikola import_gplus_html -s takeout
        [...]
        ************************************************
        *                                              *
        * Share information of your G+ Takeout archive *
        *                                              *
        ************************************************
        
        =======
        General
        =======
        
        (edit the "shared" section of your config.yaml)
        
        Geteilt mit: Öffentlich (1832)
        Shared to the community (704)
        Shared to the collection (429)
        [...]
        
        ===========
        Communities
        ===========
        
        (edit the "import" section of your config.yaml:
            > set "com" to True to include communities
            > exclude communities by listing them in "com_filter")
        
        E-Book (275)
        Das Gruselkabinett des Dr. Goo (196)
        Deleted community (65)
        [...]
        
        ===========
        Collections
        ===========
        
        (collections are considered public so this is FYI only)
        
        Zapping (66)
        Street|p|arts (61)
        Unterwegs (54)
        [...]

Beiträge filtern
****************

Mit der Option ``import_private`` lässt sich einstellen, ob mit bestimmten Kreisen oder Personen/Profilen geteilte Beiträge importiert werden sollen.

Die Option ``import_com`` schaltet den Import von Communitybeträgen ein oder aus. Dabei wird nicht nach öffentlichen oder geschlossenen Communities unterschieden.

.. class:: pull-right

.. figure:: /images/GPlus_plugin/watermark.jpg

    Albrecht-Daniel-Thaer-Saal

Bilddateien markieren
*********************

Falls man sein Archiv öffentlich zur Verfügung stellen möchte, mag es hilfreich oder erwünscht sein, Bilddateien mit einem Wasserzeichen oder Hinweis auf den Ursprung zu versehen.

Dafür setzt man ``watermark`` auf *True* und legt eine Textzeile fest (``watermark_text``). Dies erzeugt mit Hilfe von `ImageMagick <https://www.imagemagick.org>`_ ein horizontales Textbanner für alle Bilder.

Die Dateien werden in einem separaten Ordner erstellt, ohne die Originaldateien zu überschreiben. Das bedeutet, man kann den Build-Prozess beliebig für beide Optionen laufen lassen, ohne den Import erneut ausführen zu müssen.

Import
======

Im ``gplus_dummy_site``-Verzeichnis führt man nun den Import aus, dabei wird als Argument der Ordner des entpackten Takeout-Verzeichnisses übergeben:

.. code:: bash

    $ nikola import_gplus_html path/to/takeout_folder

Nikola initialisiert eine neue Seite namens "new_site", dort werden alle Posts, die dazugehörigen Metadaten und die Mediendateien gespeichert.

Mit der Option ``-o`` lässt sich ein individueller Name für die neu angelegte Seite vergeben. Dies ist praktisch, wenn man zum Beispiel verschiedene Versionen der selben Ausgangsdaten erstellen möchte.

Statische Seite erstellen
=========================

conf.py
*******

Nun wechselt man in das Verzeichnis der neuen Nikola-Instanz (standardmäßig "new_site").

Dort befindet sich die Konfigurationsdatei ``conf.py``. In dieser lassen sich nun Anpassungen vornehmen. Da im Beispiel das Thema `hyde <https://themes.getnikola.com/v8/hyde/>`_ verwendet wird, wird dieses hier gleich angepasst, außerdem die Auslieferung des RSS-Feeds deaktiviert:

.. code:: python

    THEME = "hyde"
    GENERATE_RSS = False

Thema
*****

Hyde ist ein persönlicher Favorit und wird deshalb hier installiiert:

.. code:: bash

    $ nikola theme -i hyde

Im Pluginordner befindet sich eine CSS-Datei ``custom.css``, die einige optische Anpassungen für diesen Anwendungsfall enthält, diese einfach in das Verzeichnis ``themes/hyde/assets/css`` kopieren.

Grundsätzlich funktioniert die Seite mit jeden Theme. Eine Liste der verfügbaren `Themes <https://themes.getnikola.com>`_ erhält man folgendermaßen:

.. code:: bash

    $ nikola theme -l   # installierbar
    $ nikola theme --list-installed     # installiert

Um ein Thema zu verwenden, muss es in der ``conf.py`` angegeben und die Seite neu gebaut werden. Ein erneuter Datenimport ist natürlich nicht notwendig.

Bilder
******

Möchte man die Bilddateien mit Textbanner verwenden, muss in der ``conf.py`` noch der entsprechende Ordner zugewiesen werden:

.. code:: python

    IMAGE_FOLDERS = {"images_wm": "images"}

Bei einem größeren Bildervolumen ist es eventuell sinnvoll, die Bild- und Thumbnailgröße einzuschränken:

.. code:: python

    MAX_IMAGE_SIZE = 800  # default 1280
    IMAGE_THUMBNAIL_SIZE = 200   # default 400


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
