.. title: Nikola: everything zen
.. slug: nikola-everything-zen
.. date: 2017-10-05 15:45:06 UTC+02:00
.. tags: nikola
.. category: 
.. link: 
.. description: 
.. type: text

**Aktualisiertes zen-Thema für Nikola**

Diese Seite wird mit dem statischen Webseitengenerator Nikola betrieben. Dabei wird das zen-Thema verwendet.

Die immer noch aktuelle Version des Themes verwendet Font Awesome 3.2.1, welches nicht mehr unterstützt wird. Die Icons lassen sich natürlich weiterhin verwenden, aber man muss auf aktualisierte und neue Icons verzichten.

Da ich dies sowie ein paar Kleinigkeiten am Theme verändert, aber an LESS vorbei einfach nur im CSS herumgepfuscht habe, werde ich dies nicht committen, sondern nur hier als gepacktes Archiv abladen (für den Fall, dass jemand Interesse daran hat).

Installation
************

Das Theme wird wie gehabt im entsprechenden Verzeichnis entpackt (``nikola_instanz/themes/``) und anschließend in der ``conf.py`` zu

.. code::

    THEME = "zen_fa4"

geändert. Die Änderungen werden natürlich erst nach dem nächsten

.. code::

    nikola build

wirksam.

Less LESS with CSS
******************

Die zen-Themes sind mit dem LESS-Framework erstellt. Der Vorteil daran ist, dass die LESS-Dateien in CSS-Dateien kompiliert werden, die dann ebenso editiert werden können.

Die CSS-Dateien befinden sich in ``.../themes/zen_fa4/assets/css/``, im Fall des zen-Themes benötigt man nur die ``main.css``. Die aktualisierten Font Awesome-Fonts befinden sich (logischerweise) in ``.../themes/zen_fa4/assets/fonts/``.

Möchte man bei LESS bleiben, steht dafür aber auch ein Nikola-Plugin bereit.

Links
*****

 * `Nikola static site generator <https://getnikola.com/>`_
 * `Themes for Nikola <https://themes.getnikola.com/>`_
 * `zen <https://themes.getnikola.com/v7/zen/>`_
 * `LESS stylesheet framework <http://lesscss.org/>`_
 * `LESS-Plugin für Nikola <https://plugins.getnikola.com/v7/less/>`_

Download
********

 * `zen_fa4.zip (791 kB)`__

__ /files/zen_fa4.zip
