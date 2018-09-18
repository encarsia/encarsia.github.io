<!--
.. title: Embed Mastodon toots with Nikola
.. slug: embed-mastodon-nikola
.. date: 2018-09-18 19:22:24 UTC+02:00
.. tags: nikola,mastodon
.. category: socialmedia
.. link: 
.. description: 
.. type: text
-->

**Reading the post [Mastodon Embed Shortcode for hugo](https://www.kevingimbel.com/mastodon-embed-shortcode-for-hugo/) I became envious and thought 'We Nikola users might want that, too'.**

<!--
<iframe src="https://mastodon.social/@kevingimbel/100745593232538751/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="600" height="333"</iframe>
-->

The [Nikola handbook](https://getnikola.com/handbook.html#shortcodes) plainly admits to have 'adopted' the shortcode feature from Hugo so how hard can it be?

Here are three ways of embedding toots in your Nikola site using reStructuredText.

## The *raw* directive

This directive enables you to pass content to the output without being processed. See [reStructuredText Directives documentation](http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through) for details.

```rst
.. raw:: html

    <iframe src="https://mastodon.social/@kevingimbel/100745593232538751/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="600" height="333"</iframe>
```

## The *raw* shortcode

This is part of the built-in shortcodes. It works like the directive, you only need to use shortcode tags.

```html+jinja
{{% raw %}}
<iframe src="https://mastodon.social/@kevingimbel/100745593232538751/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="600" height="333"</iframe>
{{% /raw %}}
```

## Create your own shortcode

A separate shortcode can easily be realized by a [template-based shortcode](https://getnikola.com/extending.html#template-based-shortcodes).

All you have to do is create a template and save it as ``your_shortcode_name.tmpl`` in the ``shortcode`` folder of your Nikola site. If you do not use any custom shortcodes yet you will probably have to create the folder.

The shortcode can be used as intended, pass a status and optionally width and height.

```html+jinja
{{% mastodon status=https://mastodon.social/@kevingimbel/100745593232538751 %}}
{{% mastodon status=https://mastodon.social/@kevingimbel/100745593232538751 width=300 height=600 %}}
```

This is working for me but if the shortcode fails you should use the shortcode role to pass the text unaltered (see the [Ǹikola handbook] (https://getnikola.com/handbook.html#using-a-shortcode) for more information):

``rst
:sc:`{{% mastodon status=https://mastodon.social/@kevingimbel/100745593232538751 %}}`
```

## Fun fact

This post was written in MarkDown because all this literal raw code input really confused all of us (not blaming anyone, just stating that ReST is not meant for those meta content).

