.. title: Use Markdown extensions in Nikola
.. slug: md-extensions-nikola
.. date: 2019-03-15 20:00:43 UTC+01:00
.. tags: nikola,markdown
.. category: tipps&tricks
.. link: 
.. description: 
.. type: text

.. contents::

**The default markup language of input files in Nikola is restructuredText. You can, of course, configure Nikola to also process Markdown formatted files but by default there are missing some features like admonitions or table of contents which can be enabled by extensions.**

Basic configuration
*******************

First things first: you have to edit the variables ``COMPILERS``, ``POSTS`` and ``PAGES`` of the *conf.py* and uncomment or add a line in order to make Nikola recognize and render Markdown files:

.. code:: python

    COMPILERS = {
        "rest": ('.rst', '.txt'),
        "markdown": ('.md', '.mdown', '.markdown'),
        ...
        }
    POSTS = (
        ("posts/*.rst", "posts", "post.tmpl"),
        ...
        ("posts/*.md", "posts", "post.tmpl"),
    )
    PAGES = (
        ("pages/*.rst", "pages", "story.tmpl"),
        ...
        ("pages/*.md", "pages", "story.tmpl"),
    )

Markdown extensions
*******************

There are two types of Markdown extensions:

1. `Officially supported extensions <https://python-markdown.github.io/extensions/#officially-supported-extensions>`_ that are shipped with the *python-markdown* package.

2. `Third party extensions <https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions>`_ which have to be installed separately on your system.

Enable
======

An extension is enabled by adding it to the ``MARKDOWN_EXTENSIONS`` variable.

If you want to enable officially supported extensions you add the extensions' *entry point* as list item. If the extension is part of the *extra* folder you can use ``extra`` as list item or the name of the extension, p.e. you enable definition lists with either ``def_list`` or ``extra``.

The list item for a third party extension is the exact dot notation (see the extension's documentation).

Examples
++++++++

.. code:: python

    MARKDOWN_EXTENSIONS = [# all extensions of extra available
                           "extra",
                           # other officially supported extensions
                           "admonition",
                           "toc",
                           # third party extension
                           "markdown_include.include",
                          ]

Configure
=========

Some extensions offer configuration options. These are defined in the ``MARKDOWN_EXTENSIONS_CONFIGS`` variable. The dictionary's structure is

.. code:: python

    MARKDOWN_EXTENSIONS_CONFIGS = {
        DEFAULT_LANG: {
            "ext1": {"option1": value1,
                     "option2": value2",
                },
            "ext2": {"option1": value1,
                     "option2": value2",
                },
            ...
        },
        "other_configured_lang": {
            "ext1": {"option1": value1,
                     "option2": value3",
                },
            ...
        },
    }


Use
===

Consult the extension's documentation for details. Useful extensions:

Table of contents
+++++++++++++++++

Enabled by:
    "toc"

Usage:
    .. code::

        [TOC]

Definition lists
++++++++++++++++

Enabled by:
    "extra"

Usage:
    .. code::

        item1
        :   text
        item2
        :   text

Admonitions
+++++++++++

Enabled by:
    "admonition"

Usage:
    Common types in reST are the attention, caution, danger, error, hint, important, note, tip, and warning directives but any type can be defined (css editing may be required).
    
    .. code::

        !!! danger
            no trespassing

        !!! important "custom title"
            you better read this

Include
+++++++

Enabled by:
    "markdown_include.include"

Usage:
    .. code::

        {!posts/this-is-another-markdown-file.md!}

    The input file will not be rendered if it has not been changed even if an included file was edited.

Links
*****

* `Nikola <https://getnikola.com/>`_
* `What is Markdown? <https://www.markdownguide.org/getting-started>`_
* `Markdown extensions <https://python-markdown.github.io/extensions/>`_
* `Third party extension: Markdown-Include <https://github.com/cmacmackin/markdown-include>`_
* `What is restructuredText? <http://docutils.sourceforge.net/rst.html>`_
* `More posts about Nikola on this site <link://tag/nikola>`_

.. admonition:: Fun fact

    This posts has been written in restructuredText.
