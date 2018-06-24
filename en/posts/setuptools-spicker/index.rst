.. title: GTK+-Anwendung mit setuptools packen
.. slug: setuptools-spicker
.. date: 2018-06-24 18:55:10 UTC+02:00
.. tags: python,setuptools,glade
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Der einzige Zweck dieser Seite besteht darin, die Links in meiner setup.py zu entfernen.**

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

Abhängigkeiten
==============

.. code:: python

    from setuptools import setup

    REQUIRED = ["PyGObject", ...]

    setup(
        ...
        install_requires=REQUIRED,
        ...
        )

Angabe des PyPI-Paketnamens, bei GTK+-Pythonprogrammen also mindestens die entsprechenden Bindings, da sonst ``import gi`` scheitert.

Nicht Python-Paketdateien
=========================

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

Das Paket "my_package" wird aus dem Verzeichnis "my_package_dir" im Verzeichnis "my_package" gepackt.

Die Dateien, die keinen Python-Code enthalten, also etwa Glade-Dateien, werden als Liste in ``package_data`` übergeben. Im Beispiel werden alle Dateien im Unterverzeichnis "ui" sowie die Datei "logging.yaml" ins Paket integriert.

Desktop-Dateien
===============

Der Speicherort von .desktop-Dateien und Icons richtet sich nach den Freedesktop-Spezifikationen. .desktop-Dateien befinden sich zum Beispiel in den Verzeichnissen

.. code::

    /usr/share/applications
    /usr/local/share/applications
    ~/.local/share/applications

Während der Ausführung von ``install`` wird das Präfix ermittelt, es ist also nur die Angabe des relativen Pfads in der ``data_files``-Option notwendig. Gleiches gilt für Icons.

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

Dieser Schritt kopiert nur die Dateien in die entsprechenden Zielverzeichnisse. Die korrekten Pfadangaben IN der .desktop-Datei werden durch eine eigene Funktion innerhalb des Install-Kommandos angepasst.

Bestehendes Kommando anpassen
=============================

Die .desktop-Datei enthält Pfadangaben zur auszuführenden Datei sowie zum dazugehörigen Icon. Da das Zielverzeichnis der Installation nicht vorhersehbar ist, müssen diese Pfade während der Installation an die Gegebenheiten angepasst werden.

Um eigene Funktionen in bestehende Kommandos auszuführen, muss man eine eigene Instanz der entsprechenden Klasse (install, build, bdist etc.) generieren und die "run"-Funktion anpassen.

Setuptools wird dann mit der Option ``cmd_class`` auf diese eigene Klasse übergeben.

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

Eine Liste mit verfügbaren Kommandos erhält man durch

.. code:: console

    $ python setup.py --help-commands

Neues Kommando erstellen
========================

Es ist einfach möglich, eigene Kommandos mit setuptools zu erzeugen. Möchte man beispielsweise die zuvor installierten Dateien, also das Python-Paket und die Desktop-Dateien, loswerden, muss dies manuell erfolgen. Dafür bietet es sich an, ein Uninstall-Kommando zu erstellen.

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
