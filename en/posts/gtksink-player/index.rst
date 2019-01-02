.. title: Mediaplayer mit GStreamer (Edition gtksink)
.. slug: gtksink-player
.. date: 2019-01-01 19:54:13 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Mediaplayer mit GStreamer**

Im einführenden Artikel zu `Mediaplayer mit GStreamer <link://slug/gst-player>`_ werden Probleme beschrieben, die auf die Verwendung von "xvimagesink" als Videosink zurückzuführen sind.

In diesem Artikel wird als Alternative der Videosink `"gtksink" <https://thiblahute.github.io/GStreamer-doc/gtk-1.0/gtksink.html>`_ verwendet und nur auf die Unterschiede zu `"xvimagesink" <https://thiblahute.github.io/GStreamer-doc/xvimagesink-1.0/index.html>`_ eingegangen, da die weitere Vorgehensweise identisch ist.

Installation
------------

*Gtksink* war ursprünglich Teil der "bad" plugins, befindet sich aber seit der GStreamer-Version 1.14 in den "good" plugins, die im Normalfall bei der Installation von GStreamer mitinstalliert werden.

Eine Ausnahme bildet Ubuntu, wo das Plugin separat im Paket ``gstreamer1.0-gtk3`` (universe) zur Verfügung steht.

Glade
-----

Der Darstellungsbereich der Mediendatei wird durch das *gtksink*-eigene Widget bereitgestellt. Da dies nicht in Glade verfügbar ist, wird ein leeres Containerwidget (*Gtk.Box*) benötigt, in das das Widget platziert werden kann.

Python
------

Videosink einrichten
********************

.. code:: python

        self.sink = Gst.ElementFactory.make("gtksink")
        

Widget einrichten
*****************

.. code:: python

        video_widget = self.sink.get_property("widget")
        builder.get_object("video_box").add(video_widget)


.. TEASER_END

Listings
--------

Python
******

.. listing:: 23_gtksink_simpleplayer.py python

Glade
*****

.. listing:: 23_gtksink_player.glade xml

Beispieldateien
***************

 * `Video (13,7 MB)`__
 * `Image (553 kB)`__

__ /files/mediaplayer.avi
__ /files/mediaplayer.jpg


