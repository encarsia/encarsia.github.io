.. title: NoN: jetzt noch viel toller
.. slug: non-jetzt-noch-viel-toller
.. date: 2018-06-24 15:45:12 UTC+02:00
.. tags: nikola,python,non
.. category: repository
.. link: 
.. description: 
.. type: text

**Knights of Ni - sag niemals nie**

Nach den `kürzlichen Änderungen <link://slug/non-release>`_ an der Oberfläche gibt es nun erfreuliche Fortschritte darunter zu vermelden.

Neuigkeiten
===========

1.  Man kann NoN jetzt richtig (mit Hilfe von setuptools) installieren und deinstallieren.

2.  Vom Programm generierte Dateien werden nun wie üblich im eigenen Verzeichnis im Homeverzeichnis gespeichert.

3.  Der Programmablauf wurde beschleunigt und die Dateizugriffe massiv reduziert, indem die Posts-/Pages-Informationen für den wiederholten Abruf geparst und in einer JSON-Datei abgelegt werden.

Installation via setuptools
===========================

Bei der Installation via `setuptools <https://pypi.org/project/setuptools/>`_ werden sowohl das Programm inklusive der UI als auch ein Desktopeintrag installiert. Nach der Installation lässt sich das Programm in GNOME also bequem über ``[super]`` + ``[n]`` (... ``[o]`` ... ``[n]``) + ``[enter]`` starten.

Um dies alles auch wieder loszuwerden, gibt es ein zusätzliches `uninstall`-Kommando. Beide Kommandos sind mit der Option ``--user`` möglich:

.. code:: console

    # (De-/)Installation im lokalen Nutzerverzeichnis
    $ python setup.py install --user
    $ python setup.py uninstall --user

    # systemweite (De-/)Installation
    $ sudo python setup.py install
    $ sudo python setup.py uninstall

Dateistruktur
=============

Die Nutzerdaten liegen jetzt in ``~/.non``. Dort befinden sich

    1. die Konfigurationsdatei ``config.yaml``, in der der Pfad zur aktuellen/letzten Nikola-Seite und die Bookmarks gespeichert sind,

    2. die Logdatei ``non.log`` sowie

    3. die geparsten Daten der aufgerufenen Nikola-Seiten jeweils als JSON-Datei.

Speicherung von (Meta-)Daten
============================

Für die Anzeige im TreeStore wurden die Daten bisher sowieso intern als Dictionary gespeichert. Das Ineffiziente daran war allerdings, dass die Daten bei jedem Refresh immer neu abgerufen wurden. Dies ist nicht notwendig und mit zunehmender Größe der Seite auch sehr zäh.

Die Lösung bestand also darin, die Daten des Dictionary zum einen für den späteren Gebrauch in einer Datei zu speichern und zum anderen es nur durch eine Update-Funktion auf aktualisierte Inhalte zu überprüfen.

Auf diese Weise werden beim ersten Aufruf einer Nikola-Konfiguration alle Posts/Pages, Tags und Kategorien oder bei erneutem Aufruf die Daten aus der entsprechenden JSON-Datei eingelesen. Die Aktualisierung erfolgt über den Abgleich der letzten Dateimodifikation. Die JSON-Datei wird beim Wechsel in eine andere Nikola-Seite (z.B. über ein Bookmark) oder bei Programmende gespeichert.

Links
=====

* `Knights of Ni-Repository <https://github.com/encarsia/non>`_
* `Nikola <https://getnikola.com>`_
* Beiträge im Blog
   * `Neues Projekt: Knights of Ni <link://slug/neues-projekt-knights-of-ni>`_
   * `NoN: Fortschritte <link://slug/non-fortschritte>`_
   * `NoN: Konsoledierung <link://slug/non-konsole>`_
   * `NoN: Fortschritte und Release <link://slug/non-release>`_
   * `Der setuptools-Spicker <link://slug/setuptools-spicker>`_
