.. title: TUXEDO laptop keyboard
.. slug: tuxedo-keyboard-tweaks
.. date: 2020-05-05 20:11:41 UTC+02:00
.. tags: tuxedo,keyboard,backlight
.. category: hardware
.. link: 
.. description: 
.. type: text

.. contents::
    :depth: 2

**Recently it was finally time to replace my beloved Dell notebook. I gave TUXEDO Computers a try.**

**This article may in part apply to other models but I refer to the TUXEDO Book BC1510 using Archlinux.**

Driver installation
*******************

This seems a no-brainer but for the sake of completeness it shall be mentioned to install the TUXEDO keyboard driver to enable backlight functions and Fn/media keys. The easiest way to do this is installing the package from the AUR_.

.. _AUR: https://aur.archlinux.org/packages/tuxedo-keyboard


Toggle touchpad on shortcut
***************************

Oddly enough there doesn't seem to be a Fn/media key for toggling the touchpad which is a function I personally use quite often.

The common way to assign keyboard shortcuts is using xmodmap_ by customizing the *.Xmodmap* file in the user's home.

.. _xmodmap: https://wiki.archlinux.org/index.php/Xmodmap

Assign ``XF86TouchpadToggle`` to a key or shortcut.

You can find out whether the function is theoretically assigned to any key by searching for it:

.. code:: console

    $ xmodmap -pke | grep Touchpad
    ------------------
    output for BC1510:
    ------------------
    keycode 199 = XF86TouchpadToggle NoSymbol XF86TouchpadToggle NoSymbol XF86TouchpadToggle
    keycode 200 = XF86TouchpadOn NoSymbol XF86TouchpadOn NoSymbol XF86TouchpadOn
    keycode 201 = XF86TouchpadOff NoSymbol  XF86TouchpadOff NoSymbol XF86TouchpadOff

Test the functionality by executing the keystroke via xdotool:

.. code:: console

    $ xdotool key 199

This probably works except you are using...

GNOME Shell
+++++++++++

Long story short: xmodmap does not work with GNOME Shell/Wayland. If you intend to take the red pill `take this way to XKB`_, or take the blue pill by just assigning the function to a shortcut via gsettings.

Open *dconf-editor* and pilot to ``org.gnome.settings-daemon.plugins.media-keys/touchpad-toggle`` and set a custom value, p.e. ['F4'].

{{% thumbnail "/images/tuxedo_Fn.png" title="No touchpad symbol? F4 unoccupied." %}}<h4><i>No touchpad symbol? F4 unoccupied.</i></h4>{{% /thumbnail %}}

.. _take this way to XKB: https://medium.com/@damko/a-simple-humble-but-comprehensive-guide-to-xkb-for-linux-6f1ad5e13450


Keyboard backlight
******************

Now comes the fun part. You don't buy a device with keyboard backlight without making use of it.

By default on boot the backlight is white. The integrated backlight of the BC1510 model is RGB so it's playtime.

Media keys
++++++++++

Backlight control via shortcuts is available on numpad keys:

* **Fn + /**: cycle through a preset of colors (red, lime, blue, yellow, fuchsia, aqua, white, off)
* **Fn + \***: toggle backlight on/off
* **Fn + +**: increase brightness
* **Fn + -**: decrease brightness

{{% thumbnail "/images/tuxedo_num.png" title="Backlight keys." %}}<h4><i>Backlight keys.</i></h4>{{% /thumbnail %}}

TUXEDO Backlight Control
++++++++++++++++++++++++

The `TUXEDO Backlight Control`_ provides a CLI and Tkinter GUI to control the keyboard backlight. The package can be installed from the AUR.

There are some shortcomings:

1. The authentication restrictions are annoying and IMHO pointless. There is no need to require superuser rights when changing backlight colors.
2. There is no option to adjust brightness.
3. Custom colors can be defined but must be written in a colors.conf file (required superuser rights).

The enhanced TUXEDO Backlight Control
+++++++++++++++++++++++++++++++++++++

.. attention::
    Only developed and tested with Arch.

I created a tweaked version to get rid of the negative aspects mentioned above.

First, there are no more password prompts when executing a *backlight* command or launching the GUI (adjusted PolicyKit permissions).

Second, there are two new functions in the CLI:

.. code:: console

    # brightness control, set a value between 0 and 255, example:
    $ backlight 124
    
    # set a custom color by passing the hex color code, example:
    $ backlight color ff5900

One may want to process the backlight command in scripts, for example visualize low battery status, notifications or graduently changing colors depending on the time of day...

Download forked version from `encarsia/tuxedo-backlight-control`_ (Arch package available).

Looping through color preset
----------------------------

.. raw:: html

    <embed src="../../files/tuxedo-bl.mp4" autostart="true" height="400" width="700" />

.. _TUXEDO Backlight Control: https://github.com/webketje/tuxedo-backlight-control

.. _encarsia/tuxedo-backlight-control: https://github.com/encarsia/tuxedo-backlight-control

