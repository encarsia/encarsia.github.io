.. title: Embed Pixelfed posts (with Nikola)
.. slug: embed-pixelfed
.. date: 2019-11-29 21:59:17 UTC+01:00
.. tags: pixelfed,fediverse,nikola
.. category: socialmedia
.. link: 
.. description: 
.. type: text

Pixelwhat?
----------

Pixelfed_ is the photo sharing platform of the fediverse. The FOSS version of Instagram so to speak.

Recently I stumbled over the option to embed posts. You can generate the code via the post's centext menu. I discovered that embedding posts work even if this context menu is not available.

.. _Pixelfed: https://pixelfed.org

.. image:: /images/pixelfed-embed.png

Shortcode for Nikola
--------------------

The approach for creating and using a custom shortcode for Pixelfed corresponds basically to embedding Mastodon toots which I have already written a pretty `informative blog post`_ about.

.. _informative blog post: link://slug/mastodon-nikola

How to use
**********

Save the ``pixelfed.tmpl`` file in the ``shortcode`` folder of your Nikola site.

.. gist:: f7ec256b32003d179326d6ebdec2a6ab

.. gist:: 6c63d9433b05878b7c751036a903f8d0


You can use the shortcode with reStructuredText and Markdown markup.

What's hot & what's not
***********************

As stated before Pixelfed is in an early stage of development and not everything works flawlessly.

================= ==========
**Embedding...**   **Status**
================= ==========
single photo post works
album post        `does not work`_
animated GIF      works
video             works
collection        does not work
================= ==========

.. _does not work: https://github.com/pixelfed/pixelfed/issues/776

I post pictures of small things.

{{% pixelfed status=https://pixelfed.social/p/encarsia/104187465195196416 %}}

Alm posts pictures of cats.

{{% pixelfed status=https://pixelfed.de/p/alm10965/106018103883862016 %}}

esureL posts pictures of painted distribution boxes (and food).

{{% pixelfed status=https://pixelfed.social/p/esureL/106030673873211392 %}}

Keep moving.

{{% pixelfed status=https://pixelfed.social/p/encarsia/3294 %}}

{{% pixelfed status=https://pixelfed.social/p/atomjack/103513270102659072 %}}

This points to an `album post <https://pixelfed.social/p/JOX/95141123726643200>`_.

{{% pixelfed status=https://pixelfed.social/p/JOX/95141123726643200 %}}

This points to a `collection <https://pixelfed.social/c/106059557062709248>`_.

{{% pixelfed status=https://pixelfed.social/c/106059557062709248 %}}
