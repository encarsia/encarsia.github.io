.. title: NoN: v0.6 release
.. slug: non-0.6
.. date: 2018-11-12 16:10:57 UTC+01:00
.. tags: nikola,non,python
.. category: repository
.. link: 
.. description: 
.. type: text

**Let's just use it as it is now.**

The `last release <link://slug/non-0.5>`_ was a huge step for the project. Now it's time for some details and polish before I focus on a neglected project of mine.

New feature: upload files to GitHub without deployment
******************************************************

There are two new toolbuttons to push or pull changes to or from GitHub without building or deploying the site. This imitates 'cloud' support so you can edit articles, drafts, listings etc. within the GitHub web interface and/or download/pull changed files on multiple locations.

.. figure:: /images/non/pushdraft06.png
    :scale: 70%
    
    Push files to the origin/src branch

This is a very basic implementation and you may have to manually resolve conflicts if you are editing in various places simultaneously.

.. warning::

    Consider this feature marked as *testing*.

Changelog
*********

* show input file format in statusbar
* detect if separate metadata file exists and show info in statusbar, open file on right click
* use the webbrowser Python package instead of subprocess commands; the package also uses the subprocess module but the code just looks nicer
* the "New post" dialog is a *GtkMessageDialog* now
* FileChooserDialog has its OK/Cancel buttons back
* if the current working directory is bookmarked, the menu entry is labeled as "(active)" and deactivated
* gettext localization strings in the POT file are now complete
* German localization is complete
* some icons changed

.. figure:: /images/non/menu06.png

    Menu: open bookmark is deactivated

.. figure:: /images/non/meta06.png

    Information about file format and metafile in statusbar, open separate metafile on right click if it exists

Links
*****

* `Get it on GitHub! <https://github.com/encarsia/non/releases>`_
* evolution of Ni:

 * `v0.5 release <link://slug/non-0.5>`_
 * `v0.4 release <link://slug/non-release>`_
 * `Konsoledierung <link://slug/non-konsole>`_
 * `Fortschritte <link://slug/non-fortschritte>`_
 * `Neues Projekt: Knights of Ni <link://slug/neues-projekt-knights-of-ni>`_

