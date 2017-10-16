.. title: Mediaplayer mit VLC
.. slug: vlc-player
.. date: 2017-09-22 19:28:18 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Mediaplayer mit LibVLC realisieren**

VLC ist nicht nur ein Multimediaplayer, sondern auch ein Framework, zu dem Python-Bindings verfügbar sind. In diesem Beispiel wird analog zum `GStreamer-Artikel <link://slug/gst-player>`__ ein einfacher Mediaplayer mittels LibVLC umgesetzt.

.. thumbnail:: /images/20_vlc_player.png

LibVLC
------

Voraussetzung für die Verwendung ist die Installation der Python-Bindings. Diese sind unter der Paketbezeichnung ``python-vlc`` zu finden.

Glade
-----

 * **Darstellungsbereich der Mediendatei:** Widget *Gtk.DrawingArea*
 * **Steuerungselemente:** Vor-/Zurückspulen (*Gtk.Button*), Pause (*Gtk.Togglebutton*)
 * **Medienauswahl:** Buttons, um Video- oder Bilddatei anzuzeigen
 * **Playback manipulieren:** Buttons zum Stummschalten und Drehen des Videos

Python
------

Player einrichten
*****************

Der VLC-Player wird initiiert, sobald das dazugehörige Widget, in diesem Fall also *Gtk.DrawingArea* gezeichnet wird. Dazu wird das Signal ``realize`` genutzt, das grundsätzlich für die Klasse der Widgets verfügbar ist.

.. code-block:: python

    vlcOptions = "--no-xlib"
    win_id = widget.get_window().get_xid()
    setup_player(vlcOptions)
    vlcInstance = vlc.Instance(options)
    player = vlcInstance.media_player_new()
    player.set_xwindow(win_id)

Als Optionen können Kommandozeilenoptionen von VLC übergeben werden. Im Beispiel wird beim Klick auf den "Rotate"-Button das Bild um 180° gedreht. Der Player wird erneut initiiert und die zusätzliche Option ``--video-filter=transform{type=180}`` übergeben.

Medium abspielen
****************

Wie auch der GStreamer-Player kann der VLC-Player viele Video-/Audio- oder Bild-Formate anzeigen bzw. abspielen.

.. code-block:: python

    player.set_mrl(file_url)
    #Datei abspielen
    player.play()
    #Pause/Play-Schalter
    player.pause()

Positionsanzeige
****************

Die Umsetzung des Fortschrittsbalkens und die Nutzung als Schiebereglers gestaltet sich ziemlich einfach.

.. code-block:: python

    #Position abfragen
    player.get_position()
    #Position bestimmen
    player.set_position(val)

Der Wertebereich liegt dabei zwischen 0 und 1. Das Problem bei diesen Funktionen ist, dass sie relativ ressourcenintensiv arbeiten und das Playback mitunter verruckelt ist.
Die Lösung im hiesigen Beispiel besteht darin, ``get_position``-Abfragen zu umgehen, indem die Regler-Position herangezogen wird.

Möglichkeiten und Limitierungen
-------------------------------

Die Nutzung der LibVLC-Python-Bindings erweist sich als einfach und angesichts der GStreamer-Umsetzung als geradezu intuitiv. Auch das `"Headerbar-Problem" <https://plus.google.com/105146352752269764996/posts/jDcBAztBxM9>`__ besteht nicht.

Auf der anderen Seite greift man hier auf großes Projekt zurück, man muss VLC und die Python-Bindings installiert haben anstatt einfach das GStreamer-Modul aus dem GObject Introspection-Repository zu verwenden. Auch ist im Test der Ressourcenverbrauch von VLC gegenüber GStreamer größer.

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
