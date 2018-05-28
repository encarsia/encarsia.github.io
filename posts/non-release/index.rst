.. title: NoN: Fortschritte und Release
.. slug: non-release
.. date: 2018-05-28 18:01:55 UTC+02:00
.. tags: nikola,python,non
.. category: repository
.. link: 
.. description: 
.. type: text

**Knights of Ni - little release on the prairie**

Der GTK+-Desktopclient für den statischen Webseitengenerators Nikola hat seit der letzten Erwähnung hier weitere Fortschritte machen können.

Da Nikola v8 im Juni zu erwarten ist und ich noch nicht weiß, was an Nacharbeiten auf mich zukommt, habe ich den aktuellen Status `als Release gespeichert <https://github.com/encarsia/non/releases/tag/v.0.4>`_.

Neuigkeiten
===========

Headerbar
    Das Untermenü ist auf die rechte Seite gewandert, links befindet sich der GUI-/Terminal-StackSwitcher, neu ist der Button zum Öffnen des Nikola-Handbuchs.

Erweiterte Deployment-Optionen
    * GitLab: *"Deploy to GitHub"*-Button nutzen, Hilfe zur Konfiguration gibt es `hier <https://gitlab.com/pages/nikola>`_
    * Andere: existiert in der ``conf.py`` die Variable. ``DEPLOY_COMMANDS``, wird mit dem *"Deploy"*-Button das 'default'-Preset ausgeführt.
    
GtkApplication
    NoN läuft nun als echte `GtkApplication <link://slug/application>`_.

Desktop-Eintrag
    Enteenteenteente...

Post/Page im Browser öffnen
    Per Rechtsklick lässt sich aus der Übersicht der Beitrag im Browser öffnen.

Diverser Kleinkram
    Bugfixes, verbessertes Logging, Python-Code ist nun PEP8-konform (sagt pycodestyle).

.. thumbnail:: /images/non3.png

Links
=====

* `Knights of Ni-Repository <https://github.com/encarsia/non>`_
* `Nikola <https://getnikola.com>`_
* Beiträge im Blog
   * `Neues Projekt: Knights of Ni <link://slug/neues-projekt-knights-of-ni>`_
   * `NoN: Fortschritte <link://slug/non-fortschritte>`_
   * `NoN: Konsoledierung <link://slug/non-konsole>`_

