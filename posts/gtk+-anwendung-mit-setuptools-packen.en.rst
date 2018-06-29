.. title: Packing GTK+ applications with setuptools
.. slug: setuptools-spicker
.. date: 2018-06-24 18:55:10 UTC+02:00
.. tags: python,setuptools,glade
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**The only reason this page exists is to remove the links in my setup.py file.**

Links
=====

* `example setup.py <https://github.com/kennethreitz/setup.py/blob/master/setup.py>`_
* `(stackoverflow) Install .desktop file with setup.py <https://stackoverflow.com/questions/25284879/install-desktop-file-with-setup-py>`_
* `How To Add Custom Build Steps and Commands To setup.py <https://seasonofcode.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy.html>`_
* `(stackoverflow) How to get installation directory using setuptools and pkg_ressources <https://stackoverflow.com/questions/36187264/how-to-get-installation-directory-using-setuptools-and-pkg-ressources>`_
* `Custom subcommand at setup.py <https://coderwall.com/p/3q_czg/custom-subcommand-at-setup-py>`_
* `Adding custom commands to setup.py <https://dankeder.com/posts/adding-custom-commands-to-setup-py/>`_
* `setuptools documentation <https://setuptools.readthedocs.io/en/latest/>`_
* `setup.py of my GTK+ application with custom install and uninstall commands <https://github.com/encarsia/non/blob/master/setup.py>`_

Dependencies
============

.. code:: python

    from setuptools import setup

    REQUIRED = ["PyGObject", ...]

    setup(
        ...
        install_requires=REQUIRED,
        ...
        )

Pass the PyPI package name, for GTK+ applications you will need at least the GObject Python bindings to successfully run the ``import gi`` command.

Non-code files
==============

.. code:: python

    from setuptools import setup

    PACKAGES = ["my_package"]
    PACKAGE_DIR = {"my_package": "my_package_dir"}
    PACKAGE_DATA = {"my_package": ["ui/*", "logging.yaml"]}

    setup(
        ...
        packages=PACKAGES,
        package_dir=PACKAGE_DIR,
        package_data=PACKAGE_DATA,
        ...
        )

The package "my_package" will be built from the files in "my_package_dir" folder into the "my_package" folder.

Non-code files like Glade files are passed as a list to the ``package_data`` option. In the example all files of the subfolder "ui" and the file "logging.yaml" are integrated into the package.

Desktop files
=============

The locations of .desktop files and icons are defined by the Freedesktop specifications. Desktop entries for example are located in

.. code::

    /usr/share/applications
    /usr/local/share/applications
    ~/.local/share/applications

While running ``install`` the suitable prefix will be identified so only relative paths are required to be passed to the ``data_files`` option.

.. code:: python

    from setuptools import setup

    rel_app_path = "share/applications"
    rel_icon_path = "share/icons/hicolor/scalable/apps"

    DATAFILES = [
                (destination_dir, ["list", "of", "files"]),
                (rel_app_path, ["my_app.desktop"]),
                (rel_icon_path, ["my_appicon.svg"]),
                ]

    setup(
        ...
        data_files=DATAFILES,
        ...
        )

This step only copies the files into the specific directories. The correct path declaration WITHIN the .desktop file has to be customized during the install command which will be accomplished by a custom function.

Customizing existing commands
=============================

The .desktop file includes information about the program to be executed as well as a corresponding icon, keywords etc.
Because the target installation location may vary the file has to be adapted during the installation process.

To run own methods in existing commands you will have to create an instance of the specific command class (install, build, bdist etc.) and customize the "run" method.

In setuptools this information is passed to the ``cmd_class`` option.

.. code:: python

    from setuptools import setup
    from setuptools.command.install import install

    class CustomInstall(install):
        
        def run(self):
            self.my_function(args, go, here)
            install.run(self)
            
        def my_function(self, *args):
            try:
                do_some_shit()
            except:
                pass 

    setup(
        ...
        cmdclass={"install": CustomInstall}
        ...
        )

A list of available commands can be obtained by

.. code:: console

    $ python setup.py --help-commands

Creating new commands
=====================

Setuptools enables you to simply create your own commands. It may be useful to create an 'uninstall' command to get rid of all the files dumped to the system during installation to avoid to do that manually.

.. code:: python
    
    from setuptools import setup, Command
    
    class UnInstall(Command):
    
        description = "description shown by setup.py --help-commands"
        user_options = [("myoption",
                         "m",
                         "myoption description shown by setup.py cmd --help")]
    
        def initialize_options(self):
            # method must exist
            # define all options with default value
            self.myoption = None
    
        def finalize_options(self):
            # method must exist
            pass
    
        def run(self):
            # method must exist
            # code to be executed goes here
            print("This is a custom command.")
    
    setup(
        ...
        cmdclass={"uninstall": UnInstall}
        ...
        )
