.. title: NoN: News, changes and release
.. slug: non-0.5
.. date: 2018-10-06 08:00:59 UTC+02:00
.. tags: nikola,non,python
.. category: repository
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Watch Knights of Ni grow up.**

Versions'n'distros
==================

Nikola v8
*********

If you have not done yet you should read the `upgrade guide to Nikola v8 <https://getnikola.com/blog/upgrading-to-nikola-v8.html>`_. NoN works with v7 and v8 nonetheless.

Runs on Archlinux and Ubuntu
****************************

I fiddled around until I got NoN working on a fresh Ubuntu 18.04 LTS installation. First install some dependencies:

.. code:: bash

    $ sudo apt-get install gir1.2-webkit2-4.0 python3-pip

and then in lack of a package in the repositories install Nikola via pip:

.. code:: bash

    $ pip3 install Nikola[extras]

If you are on (a) Archlinux (derivate) you can install Nikola from the repos:

.. code:: bash

    $ sudo pacman -S nikola python-yaml

This is new since last release
==============================

Install/uninstall via setuptools
********************************

NoN is basically a Python script with a GtkBuilder GUI so in general you can get it running by executing ``non.py``.

As an alternative you can now install or uninstall the application using setuptools which will also install a desktop entry so you can start the application from the menu:

.. code:: python

    # install for current user
    python setup.py install --user
    # install system-wide
    sudo python setup.py install

Use the ``uninstall`` command to revert installation.

Config in YAML format
*********************

The configuration is stored in easy readable YAML format. As of now there are only bookmarks and the last working directory stored.

Editing or removing bookmarks can only be done here (GUI solution is on the roadmap).

Site data stored in JSON file
*****************************

Application has been sped up by storing the sites (meta) data in a JSON formatted file. If a ``conf.py`` and the corresponding site is loaded into the application for the first time the data will be indexed. This initial task can take some time. On every next refresh/start this data will only be checked for changes and updated.

Optimized window space
**********************

I rearraged some elements to save some vertical space:

.. |image1| image:: /images/non_info_old.png
.. |image2| image:: /images/non_info_new.png

.. table::
    :align: center
    
    +----------+
    | |image1| |
    +----------+
    | *is now* |
    +----------+
    | |image2| |
    +----------+

Summary tab
***********

The main window's notebook now has a new tab showing a HTML page with collected information about the current website:

* disk usage
* status (``nikola status``)
* broken internal links (``nikola check -l``)
* themes
* plugins and
* custom shortcodes

The CSS used is imitates GitHub style, credit goes to `sindresorhus/github-markdown-css <https://github.com/sindresorhus/github-markdown-css>`_.

The summary is generated when initially indexing the site. Choose the menu item to generate a new report.

.. figure:: /images/non_summary.png

    Summary tab

Localization support
********************

There is now a translation template file (POT) waiting for translation. In case you have German localization, don't be irritated, there are only some strings translated yet.

Create posts/pages in Markdown
******************************

The default input format of Nikola is reStructuredText but it supports various other formats. You can now create new posts or pages in Markdown. This option is only available if *"markdown"* is set in the ``conf.py``'s *COMPILERS* variable.

You must also configure the *POSTS* and *PAGES* dictionaries, NoN does not check for this and will not throw an error message if not set.

.. figure:: /images/non_md.png

    Markdown format checkbutton

Get help
********

The 'Help' button now contains a submenu with links to the Nikola handbook and to reStructuredText and Markdown syntax references so I...ehm you don't have to google them time and time again.

Thing left do do
================

Issues
******

* icon not shown under Wayland
* running application not marked at dock launcher (favorite), separate icon

Roadmap
*******

* preferences dialog/window
* article templates (make use of ``nikola new_post --import...``)
* editor tab for quick editing
* option to pull/push drafts from/to Git

Download
========

* `0.5 release <https://github.com/encarsia/non/releases/tag/v0.5>`_
* `clone or download from GitHub <https://github.com/encarsia/non/>`_
