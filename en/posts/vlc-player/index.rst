.. title: Media player with VLC
.. slug: vlc-player
.. date: 2017-09-22 19:28:18 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Creating a media player with LibVLC**

VLC is not just a multimedia player but also a framework  with Python bindings available. In this example app a simple media player will be set up via LibVLC (see also the `GStreamer mediaplayer article <link://slug/gst-player>`__).

.. thumbnail:: /images/20_vlc_player.png

LibVLC
------

The installation of the VLC Python bindings are mandatory. The package is coomonly found under the name ``python-vlc``.

Glade
-----

 * **display area of the media file:** *Gtk.DrawingArea* widget
 * **control elements:** skip for-/backward (*Gtk.Button*), pause/resume playback (*Gtk.Togglebutton*)
 * **select media:** buttons to show video or image file
 * **manipulate playback:** buttons to mute and rotate video

Python
------

Set up player
*************

The VLC player is initiated when the corresponding widget (*Gtk.DrawingArea*) is drawn. The ``realize`` is required for that task. This signal in general is available for the widget class.

.. code-block:: python

    vlcOptions = "--no-xlib"
    win_id = widget.get_window().get_xid()
    setup_player(vlcOptions)
    vlcInstance = vlc.Instance(options)
    player = vlcInstance.media_player_new()
    player.set_xwindow(win_id)

Given options can be regular VLC commandline options. In the example app a click on the "rotate" button turns the video 180 degrees. Therefore the player must be initiated again with the option ``--video-filter=transform{type=180}`` given.

Media playback
**************

Just like the GStreamer player VLC is capable of showing various video, audio and image formats.

.. code-block:: python

    player.set_mrl(file_url)
    #start playback
    player.play()
    #pause/resume playback
    player.pause()

Position scale
**************

The implementation of the progress bar using a slide control is pretty simple.

.. code-block:: python

    #retrieve position
    player.get_position()
    #define positition
    player.set_position(val)

Possible values are float numbers between 0 and 1. These functions are quite resource demanding resulting into stuttering playback. In this example the ``get_position`` is avoided by retrieving the slider position instead of the video.

Possibilities and limitations
-----------------------------

Working with LibVLC Python bindings is easy and intuitive in contrast to GStreamer. In addition the `"headerbar problem" <https://plus.google.com/105146352752269764996/posts/jDcBAztBxM9>`__ is non-existent.

On the other hand it is not quite minimalistic to resort to a huge and indepentant project. You will have to install VLC and Python bindings instead of just importing the GStreamer module from the GObject Introspection repository.

The overall consumption of resources is bigger.

Links
-----

 * `LibVLC Python bindings documentation <https://www.olivieraubert.net/vlc/python-ctypes/doc/>`__
 * `How to Build a Python Media Player using LibVLC and GTK+ <https://www.codementor.io/princerapa/python-media-player-vlc-gtk-favehuy2b>`__
 * `How to get video duration in seconds? <https://superuser.com/questions/650291/how-to-get-video-duration-in-seconds>`__
 * `Mediaplayer mit GStreamer <link://slug/gst-player>`__

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 20_vlc_player.glade xml

Python
******

.. listing:: 20_vlc_simpleplayer.py python

Beispieldateien
***************

 * `Video (13,7 MB)`__
 * `Image (553 kB)`__

__ /files/mediaplayer.avi
__ /files/mediaplayer.jpg
