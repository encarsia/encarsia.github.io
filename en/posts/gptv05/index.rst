.. title: GPT: v0.5 release
.. slug: gptv05
.. date: 2018-12-14 15:18:15 UTC+01:00
.. tags: gopro,actioncam,gpt,python,gtk
.. category: repository
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

.. image:: /images/gpt/gpt_icon.png

**It has been a while since I have taken some care of my tool to manage my GoPro footage with but it has gotten some attention so I could not just abandon it without losing my face so here we are...**

Intro
=====

When I first noticed, without much surprise, that there is no official GoPro desktop client for Linux, I wrote a bash script to automatically rename the files. Second step was converting this into a python script with a simple text based menu. In a weak moment of delusions of grandeur I decided to dive into GUI programming and use this application as my personal guinea pig.

Download
========

First things first: the result of my efforts can be downloaded from the Git repository:

    * archive of the official `v0.5 release "rubula infans" <https://github.com/encarsia/gpt/releases/tag/v0.5>`_
    * download or clone the repo from `encarsia/gpt <https://github.com/encarsia/gpt>`_

.. note::

    If you have cloned the repo sometime in the past and haven't altered anything I recommend to delete and clone again because there may be conflicts caused by a force push because I cannot git.

.. raw:: html

    <video width="600" autoplay loop>
     <source src="../../files/cast_0.5.webm" type="video/webm">
     Your browser does not support the video tag.
    </video>

We've come a long way, baby
===========================

Icon
****

First things first:  we have an icon. This is my way of coping with pedantry and an attempt to keep up the illusion of competence.
I found it at `The Noun Project <https://thenounproject.com/>`_.

{{% mastodon status=https://octodon.social/@encarsia/101227233878331327 %}}

GtkApplication
**************

The application now runs as generic `Gtk.Application <https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Application.html>`_ which includes

    * starting/faving from the GNOME shell
    * identify/kill the process by name (no more random "Python" task)
    * commandline options are available
    * cleaner code, p.e. avoid starting the main loop manually

Application window
******************

Since v0.3 there is a second main application window available with media data information and a preview widget realized with GStreamer.

These two windows are now merged into one providing a StackSwitcher to switch between these alternative views. This now is the default application window.

Not convinced to drop the "single view" windows I decided to keep them for now. You can launch the application using by executing the run script passing one of these options:

.. code:: bash

    $ # compact/list view
    $ python run.py -c
    $ python run.py --alt-gui-compact
    $ # preview window
    $ python run.py -e
    $ python run.py --alt-gui-ext

If you want to use the old commandline interface, you can do so by running

.. code:: bash

    $ python run.py --cli

Run the script with ``--help`` option to show all available options.

Fixed issues
************

* importing from "other" places should do as planned now
* the GStreamer preview now uses the *gtksink* playbin (this story may be told another time)
* timelapse generation should not freeze the main loop


Burn the widge(t)
*****************

I replaced several widgets for modern looks and better desktop integration:
    * all dialogs are *Gtk.MessageDialogs* now
    * the dropdown menu is a *Gtk.PopoverMenu* instead of a *Gtk.Menu*

Logs and configuration
**********************

The output of logging and the configuration file have moved to ``~/.config/gpt``. You may have to set your working directory again if you have used GPT before.

Installation
************

Dependencies
------------

That'll do on Archlinux and derivates:

.. code:: bash

    $ sudo pacman -S python-gobject python-yaml python-setuptools python-lxml python-setproctitle mediainfo ffmpeg

And that on Ubuntu:

.. code:: bash

    $ sudo apt-get install python3-gi python3-setuptools python3-lxml gir1.2-gtk-3.0 gir1.2-gstreamer-1.0 gstreamer1.0-gtk3 mediainfo ffmpeg

Setuptools
----------

The application can be installed by using setuptools. After downloading or cloning the repository run

.. code:: bash

    $ python setup.py install --user  # or
    $ sudo python setup.py install

Desktop file
------------

Setuptools will also install a desktop file so you can launch GPT from the GNOME shell or menu. All alternative interface options are available via desktop action so you can start these on right click from the activities overview or dash if GPT is running or added as favourite.

.. image:: /images/gpt/dash_0.5.png

Bits and pieces
***************

* code improvements (formatting, readability, PEP8 compliance, removal of deprecated code, file structure)
* updated and detailed README
* updated localization files

Consult the README for details.
