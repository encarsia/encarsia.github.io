.. title: NoN: v0.7 release
.. slug: non-0.7
.. date: 2019-03-29 14:40:10 UTC+01:00
.. tags: nikola,non,python
.. category: repository
.. link: 
.. description: 
.. type: text

**Search and Popovers**

The latest release of my GTK+ client for Nikola_ features a brand-new search function and some GUI enhancements.

.. _Nikola: https://getnikola.com

.. image:: /images/non/main07.png

NEW: search function
********************

This is quite self-explanatory: you can find strings in posts, pages and listings.

.. image:: /images/non/search07.png

NEW: Popovers
*************

All menus and context menus are GtkPopovers_ or GtkPopoverMenus now to follow the guidelines and for a better desktop integration. Popovers do not extend the main window's dimensions like menus sometimes do. They look better as they are larger and point to their parent widget/origin (so right-click context menus do not appear kind of 'lost' on the screen anymore).

.. _GtkPopovers: https://developer.gnome.org/hig/stable/popovers.html.en

.. image:: /images/non/preferences07.png

.. image:: /images/non/ref_menu.png

There is also a new Popover hiding behind the *"Status"* button which displays the output of ``nikola status``.

This helps to show and resolve errors and warnings which may occur p.e. due to Nikola upgrade.

.. image:: /images/non/status_popover.png


Changelog
*********

* **Fixes:**

  * all issues regarding non-flat file structure
  * get paths and extensions for posts and pages from conf.py so files are shown that are stored aside from the default folder structure
  * remove tags/categories with zero occurences
  * quit preview if other menu items are clicked
  * return from console to main window after command execution is done 

* **New:**

  * search function: find strings in posts, pages and listings
  * menu button to open application config file

* **Updates**:

  * all menus are Popovers/PopoverMenus now
  * localization strings
  * screenshots

Links
*****

* `Get it on GitHub! <https://github.com/encarsia/non/releases>`_
* evolution of Ni:

 * `v0.6 release <link://slug/non-0.6>`_
 * `v0.5 release <link://slug/non-0.5>`_
 * `v0.4 release <link://slug/non-release>`_
 * `Konsoledierung (article in German) <link://slug/non-konsole>`_
 * `Making progress <link://slug/non-fortschritte>`_
 * `New project: Knights of Ni <link://slug/neues-projekt-knights-of-ni>`_