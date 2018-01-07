.. title: Neu: der Kettlebattle-Generator
.. slug: kettlebattle-generator
.. date: 2018-01-07 13:51:18 UTC+01:00
.. tags: kettlebell,kettlebattle,flask
.. category: repository
.. link: 
.. description: 
.. type: text


**Der Kettlebattle-Generator - eine kleine Flask-App für die großen Muskelpartien**

.. class:: warning pull-right

.. contents::

.. thumbnail:: /images/kbgen.png

Kettle...was?
=============

Genau. Okay, du weißt nicht, was Kettlebattle ist, kein Problem. Die Menschen, die diesem Unsinn nachgehen, dürften sich zahlenmäßig aktuell im einstelligen Bereich bewegen (Stand: Januar 2018).

  **Kettlebattle ist ein kollaboratives Kettlebell-Home-Workout ab zwei Mitspielern.**

Die Frontlinie der "Battle" verläuft dabei nicht zwischen den Mitspielern, sondern zwischen Motivation, Schweinehund, Sofa und Hanteln. Team up!

Spielregeln
===========

1. Die Kontaktaufnahme
    Der potentielle Mitspieler wird mit *"Kettlebattle?"* kontaktiert.

2. Der Workout-Vorschlag
    Hat der Mitspieler die Kontaktaufnahme positiv beantwortet, schlägt der Initiator ein Workout vor, das der Mitspieler akzeptieren muss. Fairness geht vor. Wer nach einem langen Tag mitten in der Nacht seinem Mitspieler ein hartes Workout vorschlägt, hat schnell keine Mitspieler mehr.

3. Do you even lift?
    Do it.

4. Das Finisher-Selfie
    Der krönende Abschluss jeder Kettlebattle ist das Finisher-Foto, das man dem Mitspieler nach dem Workout als Beweis seiner Sportlichkeit zuschickt. Hierbei ist absolute Ernsthaftigkeit zu wahren, es geht hier schließlich um Kettlebattle!

Der Generator
=============
Der Kettlebattle-Generator ist eine Einseiten-Web-App, mit der sich aus einem zuvor definierten Übungspool ein Workout generieren lässt.

Habenwill!
**********

* für die Ausführung wird Flask_ benötigt
* Download und Entpacken des Quellcodes von GitHub_
* ``kbgen.py`` ausführen, dies startet den internen Flask-Server
* 127.0.0.1:5000_ aufrufen
* Workout generieren
* Werte können per Spinner geändert werden

.. _GitHub: https://github.com/encarsia/kbgen
.. _Flask: http://flask.pocoo.org
.. _127.0.0.1:5000: http://127.0.0.1:5000/

Konfiguration
*************

In der ``kbgen.py`` gibt es 3 Variablen für individuelle Einstellungen:

1. **`REPS_PRESET`**: Tupel mit 2 Werten (int) für die Preset-Buttons, Gesamtwiederholungen 

2. **`KB_EX`**: Liste von Übungen, die bei der Kettlebattle zur Auswahl stehen sollen, ein Listeneintrag ist ein Tupel nach dem Muster (Name, Minimum bei Preset 1, Minimum bei Preset 2)

3. **`MAX_EX`**: Maximale Anzahl (int) von Übungen, die aus der Liste durchgeführt werden sollen, Minimumwerte werden immer gezählt

Verweise
========

* Kettlebell-Image: openclipart.org_
* Layout: `An Introduction to Python’s Flask Framework <https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822>`_
* Kettlebattle ist eine Erfindung von ZeEvilKohl_ und encarsia_ (yours truly)
* `GitHub-Repository`__

.. _openclipart.org: https://openclipart.org/detail/241218/kettlebell
.. _ZeEvilKohl: https://twitter.com/ZeEvilKohl
.. _encarsia: https://twitter.com/encarsia_
__ GitHub_

Pläne für später?
=================

* Export in Textbildchen (leben wir nicht in tollen Zeiten?)
* Favoritenliste/Liste der letzten Kettlebattles
* Lokalisation

Zugegeben, darauf hat die Welt nicht gerade gewartet. Aber nun ist es irgendwie trotzdem da. Willkommen!

.. raw:: html

    <br>
    <a class="discuss-on-gplus" href="https://plus.google.com/105146352752269764996/posts/hB2mQLTRzWg">Kommentieren auf <i class="fa fa-google-plus"></i></a>

