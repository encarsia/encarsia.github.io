.. title: Embed Mastodon toots with Nikola
.. slug: mastodon-nikola
.. date: 2018-09-18 15:50:16 UTC+02:00
.. tags: nikola,mastodon
.. category: socialmedia
.. link: 
.. description: 
.. type: text

{{% mastodon status=https://mastodon.social/@kevingimbel/100745593232538751 %}}

Reading the post `Mastodon Embed Shortcode for hugo <https://www.kevingimbel.com/mastodon-embed-shortcode-for-hugo/>`_ I became envious and thought 'We Nikola users might want that, too'. The `Nikola handbook <https://getnikola.com/handbook.html#shortcodes>`_ plainly admits to have 'adopted' the shortcode feature from Hugo so how hard can it be?

Here are three ways of embedding toots in your Nikola site using reStructuredText.

The *raw* directive
*******************

This directive enables you to pass content to the output without being processed. See `reStructuredText Directives documentation <http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through>`_ for details.

.. listing:: raw.txt rest
    :end-line: 3

The *raw* shortcode
*******************

This is part of the built-in shortcodes. It works like the directive, you only need to use shortcode tags.

.. listing:: raw.txt html
    :start-line: 4
    :end-line: 7

Create your own shortcode
*************************

A separate shortcode can easily be realized by a `template-based shortcode <https://getnikola.com/extending.html#template-based-shortcodes>`_.

All you have to do is create a template and save it as ``your_shortcode_name.tmpl`` in the ``shortcode`` folder of your Nikola site. If you do not use any custom shortcodes yet you will probably have to create the folder.

Depending on the template engine used by your theme you have to provide shortcode templates for Jinja2 or Mako:

.. gist:: 52728167ac7d2fe79caf480c291931ea

.. gist:: da438431ca42781045b4d63ac1b9ea5c

The shortcode can be used as intended, pass a status and optionally width and height.

.. listing:: raw.txt html
    :start-line: 8
    :end-line: 10
    
This is working for me but if the shortcode fails you should use the shortcode role to pass the text unaltered (consult the `handbook <https://getnikola.com/handbook.html#using-a-shortcode>`_ for more information):

.. listing:: raw.txt rest
    :start-line: 11
    :end-line: 12
