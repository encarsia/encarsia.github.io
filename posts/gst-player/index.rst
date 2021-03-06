.. title: Mediaplayer mit GStreamer
.. slug: gst-player
.. date: 2017-09-21 15:19:40 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Mediaplayer mit GStreamer 1.x realisieren**

`GStreamer <https://gstreamer.freedesktop.org/>`__ ist ein Multimedia-Framework, das zum Anzeigen und (De-)Kodieren von Mediendateien verwendet werden kann.

.. thumbnail:: /images/19_gst_player.png

Glade
-----

 * **Darstellungsbereich der Mediendatei:** Widget *Gtk.DrawingArea*
 * **Steuerungselemente:** Vor-/Zurückspulen (*Gtk.utton*), Pause (*Gtk.Togglebutton*)
 * **Medienauswahl:** Buttons, um Video- oder Bilddatei anzuzeigen

Python
------

Player einrichten
*****************

Elemente und Pipelines
======================

GStreamer handhabt alle möglichen Arten von Medienflüssen. Jeder Schritt in dieser Verarbeitungskette wird per *Element* definiert und in *Pipelines* verbunden. Eine solche Pipeline besteht typischerweise aus "source"-, "filter"-/"decode"- und "sink"-Elementen.

.. code::

    ------------------------------------------------------
    |  Pipeline                                          |
    |                                                    |
    |  -------------   ----------------   -------------- |
    |  | source    |   | filter       |   | sink       | |
    |  |           |->>| decoder      |->>|            | |
    |  | Quelle    |   | Verarbeitung |   | Ausgabe    | |
    |  -------------   ----------------   -------------- |
    ------------------------------------------------------

Nach diesem Prinzip wird dies mittels *Gst*-Modul umgesetzt:

.. code:: python

    # init Gst and create pipeline
    Gst.init()
    pipeline = Gst.Pipeline()

    # create elements
    src = Gst.ElementFactory.make("filesrc", "source")
    decode = Gst.ElementFactory.make("decodebin", "decode")
    sink = Gst.ElementFactory.make("xvimagesink")

    # configure elements       
    src.set_property("location", file_location)
        
    # add elements to pipeline
    pipeline.add(src)
    pipeline.add(decode)
    pipeline.add(sink)
        
    #link elements together
    src.link(decode)
    decode.link(sink)

Fertige Pipelines
=================

Es besteht auch beispielsweise die Möglichkeit, Audio- und Videosignale voneinander getrennt werden, indem jeweils ein "videosink" und ein "audiosink" erstellt usw. Auf der anderen Seite gibt es vorgefertigte Pipelines für Standardaufgaben wie etwa das Abspielen von Medien.
Ein solches Element ist "playbin", das den Code signifikant vereinfacht:

.. code:: python

    Gst.init(None)
    player = Gst.ElementFactory.make("playbin", "player")
    sink = Gst.ElementFactory.make("xvimagesink")
    player.set_property("uri", uri_of_file)
    player.set_property("video-sink", sink)

Und los!
********

Eine Pipeline oder ein "playbin"-Element können nun über *Gst.STATE* gesteuert werden:

.. code:: python

    player.set_state(Gst.State.PLAYING)
    player.set_state(Gst.State.PAUSED)

Fortschrittsanzeige
*******************

Die Fortschrittsanzeige ist an dieser Stelle keine *Gtk.ProgressBar* sondern eine horizontale *GtkScale*. Mit diesem Widget lässt sich nicht nur eine Position anzeigen, sondern auch per Maus setzen. Für letzteres wird das Signal *value-changed* benötigt. Streng genommen ist das Signal *change-value* an dieser Stelle die sauberere Lösung, die `im nachfolgenden Beitrag <link://slug/vlc-player>`_ zur Umsetzung des Mediaplayers mit LibVLC verwendet wird.

Möglichkeiten und Limitierungen
-------------------------------

Bei der Einarbeitung in GStreamer stolpert man (an dieser Stelle generalisiert die Autorin weitgehend und möglicherweise unbegründet) über diverse Hürden:

Es gibt eine Reihe von Tutorials. Die Umsetzung wird durch zwei Umstände erschwert:

1. Die primäre Sprache von und mit GStreamer ist C. Mit Python steht man eher auf experimentellem Boden.
2. Durch die Versionssprünge sowohl bei GStreamer (von 0.10 auf 1.x) als auch Python (2.x auf 3.x) funktionieren viele ältere Anleitungen nicht mehr ohne weiteres.

Es gibt weiterhin Effekte, die sich nicht erschließen. Das in diesem Artikel aufgeführte Beispiel funktioniert nicht, wenn das Fenster eine Headerbar enthält. Des Weiteren ist die Videodarstellung unter Wayland fehlerhaft (Audio läuft). Beide Probleme sind mit der Verwendung von "gtksink" lösbar.

Links
-----

 * `Tutorial on using GStreamer Python Bindings in org-mode <http://brettviren.github.io/pygst-tutorial-org/>`_
 * `gstreamer-python-player/seek.py example <https://github.com/hadware/gstreamer-python-player/blob/master/seek.py>`_
 * `GStreamer List of Elements and Plugins <https://gstreamer.freedesktop.org/documentation/plugins.html>`_
 * `GStreamer documentation <https://gstreamer.freedesktop.org/documentation/index.html>`__
 * `Using GStreamer 1.0 with Python <https://adnanalamkhan.wordpress.com/2015/03/01/using-gstreamer-1-0-with-python/>`_
 * `Mediaplayer mit VLC <link://slug/vlc-player>`_
 * `Mediaplayer mit GStreamer (gtksink-Edition) <link://slug/gtksink-player>`_

.. TEASER_END

Listings
--------

Python
******

.. listing:: 19_gst_simpleplayer.py python


Glade
*****

.. listing:: 19_gst_player.glade xml

Beispieldateien
***************

 * `Video (13,7 MB)`__
 * `Image (553 kB)`__

__ /files/mediaplayer.avi
__ /files/mediaplayer.jpg

