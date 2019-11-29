.. title: Mastodon-Tröts mit Nikola einbetten
.. slug: mastodon-nikola
.. date: 2018-09-18 15:50:16 UTC+02:00
.. tags: nikola,mastodon,fediverse
.. category: socialmedia
.. link: 
.. description: 
.. type: text

{{% mastodon status=https://mastodon.social/@kevingimbel/100745593232538751 %}}

Beim Lesen des Artikels `Mastodon Embed Shortcode for hugo <https://www.kevingimbel.com/mastodon-embed-shortcode-for-hugo/>`_ dachte ich neidisch 'Wir Nikola-Nutzer könnten sowas auch gebrauchen'. Im `Nikola-Handbuch <https://getnikola.com/handbook.html#shortcodes>`_ gibt man freimütig zu, dieses Feature sowieso von Hugo entlehnt zu haben, wie kompliziert kann es also sein?

Hier sind drei Arten, mit reStructuredText Tröts in eine Nikola-Seite einzubinden.

Die *raw*-Directive
*******************

Diese Directive ermöglicht es, Inhalt ohne Verarbeitung an die Ausgabe weiterzureichen, siehe auch `reStructuredText Directives documentation <http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through>`_.

.. listing:: raw.txt rest
    :end-line: 3

Der *raw*-Shortcode
*******************

Dieser Shortcode ist standardmäßig verfügbar. Er funktioniert genau wie die Directive, der Inhalt muss nur zwischen Shortcode-Tags platziert werden.

.. listing:: raw.txt html
    :start-line: 4
    :end-line: 7

Mach dir deinen eigenen Shortcode
*********************************

Mittels `vorlagenbasierten Shortcodes <https://getnikola.com/extending.html#template-based-shortcodes>`_ kann man einfach individuelle Shortcodes erstellen.

Dafür muss man eine Vorlage namens ``your_shortcode_name.tmpl`` erstellen und im ``shortcodes``-Ordner der Nikola-Seite speichern. Wenn noch keine eigenen Shortcodes verwendet werden, muss der Ordner höchstwahrscheinlich noch angelegt werden.

Abhängig von der verwendeten Template-Engine, die das aktuell verwendete Theme nutzt, muss der Shortcode in Jinja2 oder Mako geschrieben werden:

.. gist:: 52728167ac7d2fe79caf480c291931ea

.. gist:: da438431ca42781045b4d63ac1b9ea5c

Der Shortcode kann nun wie ursprünglich genutzt werden, es muss ein Link zum Status angegeben werden, optional noch Höhe und/oder Breite des Elements.

.. listing:: raw.txt html
    :start-line: 8
    :end-line: 10

Diese Lösungen funktionieren für mich. Falls nicht, wird die Nutzung der Shortcode-Role empfohlen (siehe `Handbuch <https://getnikola.com/handbook.html#using-a-shortcode>`_):

.. listing:: raw.txt rest
    :start-line: 11
    :end-line: 12

Man kann auch `Pixelfed-Posts einbinden <link://slug/embed-pixelfed>`_.