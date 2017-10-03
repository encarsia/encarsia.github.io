.. title: Media player with GStreamer
.. slug: gst-player
.. date: 2017-09-21 15:19:40 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Creating a media player with GStreamer 1.x**

`GStreamer <https://gstreamer.freedesktop.org/>`__ is a multimedia framework that can be used ti show (de)code and otherwise alter media files.

.. thumbnail:: /images/19_gst_player.png

Glade
-----

 * **display area of the media file:** *Gtk.DrawingArea* widget
 * **control elements:** skip for-/backward (*Gtk.Button*), pause/resume playback (*Gtk.Togglebutton*)
 * **select media:** buttons to show video or image file

Python
------

Set up player
*************

Elements and pipelines
======================

GStreamer manages all kinds of media data streams. Every step in the procession chain is defined as an *element* connected to *pipelines*. A common pipeline consists of "source", "filter"/"decode" and "sink" elements.

.. code::

    ------------------------------------------------------
    |  pipeline                                          |
    |                                                    |
    |  -------------   ----------------   -------------- |
    |  | source    |   | filter       |   | sink       | |
    |  |           |->>| decoder      |->>|            | |
    |  | input     |   | processing   |   | output     | |
    |  -------------   ----------------   -------------- |
    ------------------------------------------------------

This is done by the *Gst* module:

.. code-block:: python

    #init Gst and create pipeline
    Gst.init()
    pipeline = Gst.Pipeline()

    #create elements
    src = Gst.ElementFactory.make("filesrc","source")
    decode = Gst.ElementFactory.make("decodebin","decode")
    sink = Gst.ElementFactory.make("xvimagesink")

    #configure elements       
    src.set_property("location",file_location)
        
    #add elements to pipeline
    pipeline.add(src)
    pipeline.add(decode)
    pipeline.add(sink)
        
    #link elements together
    src.link(decode)
    decode.link(sink)

Predefined pipelines
====================

There are plenty of possibilities such like handling audio and video signals separated from each other by assigning a "videosink" and an "audiosink" and so on. On the other hand there are given pipelines for standard tasks like media playback.
In this case there can be made use of the "playbin" element which also significantly reduces the code:

.. code-block:: python

    Gst.init(None)
    player = Gst.ElementFactory.make("playbin","player")
    sink = Gst.ElementFactory.make("xvimagesink")
    player.set_property("uri",uri_of_file)
    player.set_property("video-sink", sink)

And action!
***********

A pipeline or playbin element can now be controled by *Gst.STATE*:
.. code-block:: python

    player.set_state(Gst.State.PLAYING)
    player.set_state(Gst.State.PAUSED)

Progress bar
************

The video progress in this example will not be visualized by a *Gtk.ProgressBar* but by a horizontal *Gtk.Scale*. This widget allows to manually set a position with the mouse instead of just showing a value using the *value-changed* signal. Strictly speaking the *change-value* signal is a much cleaner solution here which will be used in the `follow-up article <link://slug/vlc-player>`__ on relizing the media player with LibVLC.

Possibilities and limitations
-----------------------------

Getting to know how to utilize GStreamer there appear a bunch of obstacles (read as: the incompetent author of this article tend to widely generalize based on her experiences):

There are plenty of tutorials but two circumstances make them difficult to comply with:

1. The primary language in GStreamer is C. Good luck with your Python stuff.
2. Many older tutorials and manuals do not work out of the box because of major version leap of both GStreamer (0.10 to 1.x) and Python (2.x auf 3.x).

In addition there are effects that are hard to understand. The example given in this article does not work if the Gtk window contains a headerbar. In theory this should be solved by using the "gtksink" but I haven't figured out yet how to assign that sink to a specific widget.

Links
-----

 * `Tutorial on using GStreamer Python Bindings in org-mode <http://brettviren.github.io/pygst-tutorial-org/>`__
 * `gstreamer-python-player/seek.py example <https://github.com/hadware/gstreamer-python-player/blob/master/seek.py>`__
 * `GStreamer List of Elements and Plugins <https://gstreamer.freedesktop.org/documentation/plugins.html>`__
 * `GStreamer documentation <https://gstreamer.freedesktop.org/documentation/index.html>`__
 * `Using GStreamer 1.0 with Python <https://adnanalamkhan.wordpress.com/2015/03/01/using-gstreamer-1-0-with-python/>`__
 * `Mediaplayer mit VLC <link://slug/vlc-player>`__

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 19_gst_player.glade xml

Python
******

.. listing:: 19_gst_simpleplayer.py python

Example files
*************

 * `Video (13,7 MB)`__
 * `Image (553 kB)`__

__ /files/mediaplayer.avi
__ /files/mediaplayer.jpg

