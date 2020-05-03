.. title: Bluetooth on startup
.. slug: bluetooth-on-startup
.. date: 2020-05-03 14:23:42 UTC+02:00
.. tags: bluetooth,archlinux
.. category: tipps&tricks
.. link: 
.. description: 
.. type: text

I had some trouble getting the Bluetooth controller working on system start.

According to the `Archlinux wiki`_ I set ``AutoEnable=true`` in the */etc/bluetooth/main.conf* but the Bluetooth service had to be started manually every time.

The simple solution was that the systemd service still had to be enabled by executing

.. code:: console

    $ sudo systemctl enable bluetooth

It's easy if you know what to do...



.. _Archlinux wiki: https://wiki.archlinux.org/index.php/bluetooth#Auto_power-on_after_boot