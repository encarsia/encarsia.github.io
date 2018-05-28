.. title: NoN: Fortschritte und Release
.. slug: non-release
.. date: 2018-05-28 18:01:55 UTC+02:00
.. tags: nikola,python,non
.. category: repository
.. link: 
.. description: 
.. type: text

**Knights of Ni - little release on the prairie**

The GTK+ desktop client for static website generator Nikola has made some progress since mentioned last time here.

Nikola v8 will soon be released in June. I saved the current development status as a `release <https://github.com/encarsia/non/releases/tag/v.0.4>`_ because I cannot estimate how much effort I have to put into to make it ready for v8.

News
====

Headerbar
    The submenu moved to the right side; on the left there is the GUI/teminal StackSwitcher; new: button that opens the Nikola handbook.

More deployment options
    * GitLab: use the *"Deploy to GitHub"* button, for help on configuration see `this example Nikola site using GitLab <https://gitlab.com/pages/nikola>`_.
    * Other: if there is ``DEPLOY_COMMANDS`` variable set in your ``conf.py`` the *"Deploy"* button will execute the 'default' preset.
    
GtkApplication
    NoN now runs as a `GtkApplication <link://slug/application>`_.

Desktop entry
    Duckduckduckduckduck...

Open post/page in browser
    Right click on an article to open it in the default webbrowser.
    
Bits and pieces
    Bugfixes, improved logging, Python code is now conform to PEP8 (says pycodestyle).

.. thumbnail:: /images/non3.png

Links
=====

* `Knights of Ni-Repository <https://github.com/encarsia/non>`_
* `Nikola <https://getnikola.com>`_
* Previous posts
   * `New project: Knights of Ni <link://slug/neues-projekt-knights-of-ni>`_
   * `NoN: progress <link://slug/non-fortschritte>`_
   * `NoN: Konsoledierung <link://slug/non-konsole>`_ (in German only)

