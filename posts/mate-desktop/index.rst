.. title: Mimicry: make MATE taste like GNOME Shell
.. slug: mate-desktop
.. date: 2018-10-14 00:29:22 UTC+02:00
.. tags: mate,gnome
.. category: desktop environment
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**GNOME Shell is an elegant desktop environment. I like its appearance, modern looks and the basic concepts of using it. Although I consider myself as a loyal (and/because lazy) user it's not perfect. After testing something in a VM running MATE desktop I realized _how_ laggy it is on my machine. So I decided to trick myself by making MATE behave like GNOME. Does it work?**

My GNOME Shell setup
====================

The general desktop experience is given by the GNOME Shell itself but the everyday workflow is determinded by the use of extensions.
In fact I state that nobody uses a plain GNOME Shell.
So before tweaking the MATE desktop let's take a look at the customizations done to GNOME.

Extensions
**********

Essential
---------

* `Activities Configurator <https://extensions.gnome.org/extension/358/activities-configurator/>`_ - configure looks and behaviour of the hot corner and top panel (You want that!)
* `Auto Move Windows <https://extensions.gnome.org/extension/16/auto-move-windows/>`_ - start application windows on predefined workspaces
* Battery status indicators:
    * `Battery Percentage <https://extensions.gnome.org/extension/818/battery-percentage/>`_
    * `Battery Status <https://extensions.gnome.org/extension/817/battery-status/>`_
* `Dash to Dock <https://extensions.gnome.org/extension/307/dash-to-dock/>`_ - turn the dash into a full-grown dock (You want that, too!)
* `Drop Down Terminal <https://extensions.gnome.org/extension/442/drop-down-terminal/>`_ - unroll a terminal on keystroke
* `Multi Monitors Add-On <https://extensions.gnome.org/extension/921/multi-monitors-add-on/>`_ - extend top panel, add overview or workspaces on separate screens
* `Screenshot Tool <https://extensions.gnome.org/extension/1112/screenshot-tool/>`_ - make and save screenshots of the desktop or single windows
* `TaskBar <https://extensions.gnome.org/extension/584/taskbar/>`_ - show icons of running applications in the top panel

Honorable mentions
------------------
... of extensions that don't affect the general workflow

* `Appfolders Management extension <https://extensions.gnome.org/extension/1217/appfolders-manager/>`_ - edit appfolders from the application view
* `Arch Linux Updates Indicator <https://extensions.gnome.org/extension/1010/archlinux-updates-indicator/>`_
* `Backup Tools <https://extensions.gnome.org/extension/1312/backup-tools/>`_ - backup appfolders, extensions and their settings
* `Caffeine <https://extensions.gnome.org/extension/517/caffeine/>`_ - disable screensaver and auto suspend
* `Media Player Indicator <https://extensions.gnome.org/extension/55/media-player-indicator/>`_ - integrate media player controls into the system menu
* `OpenWeather <https://extensions.gnome.org/extension/750/openweather/>`_
* `Window Is Ready - Notification Remover <https://extensions.gnome.org/extension/1007/window-is-ready-notification-remover/>`_

Multi-monitor wallpaper
***********************

It's $CURRENT_YEAR and it's still an issue. While you can configure a multi-monitor setup in the preferences conveniently you still have to glue images together with ImageMagick to get different backgrounds on your screens like a caveman.

I highly recommend the application HydraPaper_ for this task.

.. _HydraPaper: https://github.com/gabmus/hydrapaper

Tweaking MATE
=============

Back in the days everybody™ loved GNOME 2. Starting the MATE desktop feels instant familiar.

It's great that the desktop has been completely ported to the GTK+ 3 framework. If you install the MATE packages in addition to GNOME there are hardly dependencies needed for installation. Also regular GNOME applications should fit nicely into the desktop.

Recommended packages and tools:

* Dconf-editor_ (``dconf-editor``)
* MATE Tweak (``mate-tweak``)

.. _Dconf-editor: https://wiki.gnome.org/Apps/DconfEditor


Getting things to work the GNOME Shell way
******************************************

Top Panel
---------

Easy one - it's already there and you can have as much panels as you like whereever you want (that includes all screens). Use the regular applets:

* Weather information is integrated into the clock applet.
* Battery applet exists but seems to be a little buggy.
* The TaskBar extension provides the functionality of the good old window list applet, just use the original.
* The number of workspaces is fixed, use the workspace switcher.

What's on the menu?
-------------------

You can choose between different menu variations:

Menu Bar:
    The classic GNOME 2-like applications menu split into "Applications", "Places" and "System" submenus.

Main Menu:
    Condensed classic menu with only the distribution logo (provided by the theme) visible.

Brisk menu:
    This menu originated in the `Solus project <https://getsol.us>`_ provides an additional search bar. By default this menu is activated by pressing the ``[Super]`` key so this may be the choice of a GNOME Shell user.


The Brisk menu is not installed by default. Install the ``brisk-menu`` package. Use dconf-editor to change property settings under *com.solus-project.brisk-menu*. You can enable the dark theme mode or remove the label text.

The displayed icon is determined by the used theme. If you want to use a custom icon you have to copy the chosen icon into the theme's folder as ``start-here``. This may be neccesary for different sizes:

.. code::

    /usr/share/icons/[theme]/places/[size]
    ~/.local/share/icons/[theme]/places/[size]

The icon for Brisk menu has to be copied as ``start-here-symbolic`` in

.. code::

    /usr/share/icons/[theme]/places/symbolic
    ~/.local/share/icons/[theme]/places/symbolic


You have to press ``[Esc]`` to return from the menu instead of hitting ``[Super]`` again.

No desktop icons
----------------

Who needs icons on the desktop if there are windows in the way anyway? You can disable desktop icons in MATE Tweak or by setting the *org.gnome.desktop.background.show-desktop-icons* property to "false".

Only show close button in windows
---------------------------------

You can get rid of the minimize/maximize buttons by editing the *org.mate.Marco.general.button-layout* to 'menu:close'.

This solution does not affect applications using a `Headerbar <link://slug/application-fortsetzung>`_.

Dock
----

There are `plenty of options <https://www.addictivetips.com/ubuntu-linux-tips/best-docks-to-use-on-linux/>`_ to add application docks on linux desktops. There is also a `specific applet <https://github.com/robint99/mate-dock-applet>`_ for the MATE panel which can be installed by the ``mate-dock-applet``.

My personal recommendation for now is `Plank <https://launchpad.net/plank>`_.

Keyboard application launcher
-----------------------------

Using a keyboard launcher is one option to emulate the search bar.

With its unobtrusive look and plenty of search options `Albert <https://github.com/albertlauncher/albert>`_ might be the choice of a dedicated GNOME Shell user.

Setting the shortcut to the ``[Super]`` key cannot be obtained in Albert's preferences. You will have to create a custom keybinding in dconf-editor:

1. Go to *org.mate.Marco.global-keybindings* and set a *"run-command-xx"* from 'diabled' to 'Super_L'. The "xx" is the number of the command.
2. Go to *org.mate.Marco.keybinding-commands* and set the corresponding *"command-xx"* to the value 'albert show'.

This will overwrite any other keybinding to the specific shortcut like Brisk menu.

Drop down terminal
------------------

I used Tilda_ on the GNOME 2 desktop so why not return to a long-serving application?

.. _Tilda: https://github.com/lanoxx/tilda

Even though the application is set to launch at session start in the preferences I had to add it to the startup applications manually.

.. figure:: /images/mate_or_gnome/mate_tilda.png

    Unrolled Tilda terminal on MATE, Plank dock

Multi-monitor setup
-------------------

The wallpaper issue is the same as in GNOME Shell. You may want to use HydraPaper_.

Dragging a window to another monitor might not always sets this window in the foreground (cannot completely reproduce).

You can drag a panel on an extended screen only if it is not set "extended" (uncheck in properties).

Screenshots
-----------

If you press ``[Print]`` you might be informed that "mate-screenshot" could not be found.

You can either install the ``mate-utils`` package which "mate-screenshot" is a part of or use the "gnome-screenshot" tool by editing the dconf entries *org.mate.Marco.keybinding-commands.command-screenshot* and *org.mate.Marco.keybinding-commands.command-window-screenshot* to the value ``gnome-screenshot``.

.. figure:: /images/mate_or_gnome/gn_empty.png

    Empty GNOME Shell

.. figure:: /images/mate_or_gnome/mate_empty.png

    Beware of fraud! This is MATE.


What does not work
******************

Hot corner
----------

The *Hot Corner* probably is the most symptomatic feature of the GNOME 3 desktop. By moving the mouse to the top left corner or clicking on *"Activities"* or by pressing the ``[Super]`` key you activate the *Activities Overview* which shows open windows, the dash, workspaces and the application search/launch bar.

This functionality cannot be fully emulated on the MATE desktop.

Using the Brisk menu or a keyboard launcher (or both) to get the search bar function seems like a valid compromise. This is probably the common use case when pressing the ``[Super]`` key.

What's still missing is a good way of showing running application windows. I have the habit of kicking the mouse into the corner to get to the windows overview (I realize when doing that occasionally on other desktop systems) and the old ``[Alt]``+``[Tab]`` is not a replacement.

.. figure:: /images/mate_or_gnome/gn_win.png

    Activities Overview showing open windows

Dynamic workspaces
------------------

There is currently no way to get dynamic workspaces with the Marco window manager.

Does it work?
=============

The MATE desktop is a great project. I'm glad that they managed to preserve the GNOME 2 spirit and upgrade it to a modern framework.

It is possible to integrate functionalities known from GNOME Shell into MATE turning it into a fast hybrid GTK+ desktop.

My MATE setup is a GNOME Shell copy. A good one but still. I have not decided yet if I want to live without the hot corner and I'd love to see Marco support headerbars.
