.. title: Dateiauswahldialog
.. slug: fcdialog
.. date: 2017-02-01 23:22:02 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**FileChooserDialog**

Der *GtkFileChooserDialog* ist eine Subclass von *GtkDialog* (siehe `Artikel zu Dialogen <link://slug/dialoge>`_) und ermöglicht das Auswählen und Speichern von Dateien oder Ordnern.

.. thumbnail:: /images/16_fcd.png

Glade
-----

Den Dialog findet man in der Widget-Seitenleiste oben unter *"Oberste Ebene"*. Neben dem Dateibrowser besitzt er eine erweiterbare interne *GtkBox* für weitere Widgets sowie eine *GtkButtonBox* als interne "action area" für Buttons.

Es ist erforderlich anzugeben, für welche Aktion der Dialog gedacht ist, was *Gtk.FileChooserAction* entspricht (siehe `Python GI API Reference <https://lazka.github.io/pgi-docs/#Gtk-3.0/enums.html#Gtk.FileChooserAction>`_): Datei öffnen oder speichern, Ordner auswählen oder anlegen.

Action area und Responses
*************************

Responses sind Antwortkennungen, die beim Auslösen des Signals *response* übergeben werden. Buttons in der "action area" werden jeweils Response-Werte zugewiesen anstatt das *clicked*-Signal der Buttons zu nutzen.

Standardmäßig wird die "action area" unter dem Dateibrowserbereich angelegt.

.. thumbnail:: /images/16_fcd_glade.png

Verwendet man den *FileChooserDialog* ohne Glade (siehe unten), werden die Buttons in der Headerbar angezeigt. Letzteres sollte aber vermutlich der Standard sein, da es eine Warnung ausgegeben wird, die die Funktionalität des Dialogs allerdings nicht beeinträchtigt:

.. code::

 Gtk-WARNING **: Content added to the action area of a dialog using header bars

Diese Meldung wird nicht angezeigt, wenn man darauf verzichtet, in Glade Buttons zur intern action area hinzuzufügen. Dies betrifft auch andere Dialogarten.

Legt man nun in Glade eine Headerbar mit Buttons an, ist es standardmäßig nicht möglich, diesen Buttons Response-Werte zuzuweisen.

Dafür gibt es (mindestens) zwei Lösungsmöglichkeiten:

XML-Datei
=========

Man legt die Headerbar mit Button(s) an, anschließend öffnet man die Glade-Datei in einem Texteditor und fügt dem Element ``<action-widgets>`` die entsprechenden Zeilen hinzu:

.. code-block:: xml

  <object class="GtkFileChooserDialog" id="filechooser_dialog">
    <property ... ></property>
    <property ... ></property>
    ...
    <action-widgets>
      <!-- Buttons innerhalb der action area -->
      <action-widget response="0">button1</action-widget>
      <action-widget response="1">button2</action-widget>
      <!-- Button in Headerbar -->
      <action-widget response="-1">hb_button</action-widget>
    </action-widgets>
    ...
  </object>

Dies funktioniert zwar, ist aber ganz sicher nicht so gedacht, weil diese Änderung beim erneuten Bearbeiten der Glade-Datei wieder rückgängig gemacht wird.

add_action_widget-Funktion
==========================

Mit der Funktion ``add_action_widget`` können aktivierbare Widgets zur action area hinzugefügt und damit ebenfalls per *response*-Signal verarbeitet werden. Dies sind Widgets der *Gtk.Activatable*-Klasse und beinhaltet die Widgets *Buttons*, *MenuItem*, *RecentChooserMenu*, *Switch* und *ToolItem*.

Ein Button wird nach dem Schema

.. code:: python

 widget.add_action_widget(button,response)

hinzugefügt. Wichtig ist es, beim Button die Widget-Eigenschaft "can-default" zu aktivieren:

.. code:: python

 button.set_property("can-default",True)

Im Beispiel erhält der Dialog die beiden Standardbuttons "Anwenden"/"Abbrechen":

.. code-block:: python

    button = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
    button.set_property("can-default",True)
    self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.CANCEL)
    button = Gtk.Button.new_from_stock(Gtk.STOCK_APPLY)
    button.set_property("can-default",True)
    self.obj("filechooser_dialog").add_action_widget(button, Gtk.ResponseType.OK)
    self.obj("filechooser_dialog").add_action_widget(Gtk.Button.new(), Gtk.ResponseType.OK)

Um die Dateiauswahl auch auf Doppelklick zu ermöglichen, wird neben des *response*-Signals noch das Signal *file-activated* benötigt.

Vorschau-Widget
***************

Der Dialog besitzt die Option ein Vorschau-Widget einzubinden. Dafür aktiviert man in den Dialog-Eigenschaften *"Vorschau-Widget aktiv"* und wählt unter *"Vorschau-Widget"* ein freies Widget (z.B. ein *GtkImage*). Möglicherweise muss man dieses Widget zunächst in ein leeres Container-Widget erstellen und dort in einen freien Bereich ziehen.

Wenn eine Aktualisierung der Vorschau angefordert wird, wird das Signal *update-preview* ausgelöst.

FileFilter
**********

*FileFilter* dienen dazu, Dateien bestimmten Musters anzuzeigen. Pro Filter können mehrere (shell style glob) Patterns oder MIME-Types angegeben werden.

Den Filter findet man in Glade unter *"Sonstiges"*. Im Dialog kann man in den allgemeinen Widget-Einstellungen den gewünschten Filter auswählen. Dies entspricht der ``set_filter``-Funktion.

Python
------

Dialog ohne Glade
*****************

Der *FileChooserDialog* lässt sich auch ziemlich einfach ohne Glade realisieren, zudem lassen sich die oben genannten Probleme mit Buttons in der Headerbar vermeiden. Der Dialog wird nach folgendem Schema erstellt:

.. code-block:: python

 dialog = Gtk.FileChooserDialog("window title",
                                parent_window,
                                file_chooser_action,
                                (button1,response1,
                                button2,response2))

Der Dialog wird dann direkt aufgerufen und verarbeitet:

.. code-block:: python

 response = dialog.run()
 if response == response1:
     ...
 elif response == response2:
     ...
 dialog.destroy()


FileFilter
**********

Es gibt zwei Möglichkeiten, einen *Filefilter* anzuwenden:

1. Ohne Wahl. Der anzuwendende Filter ist voreingestellt:

.. code:: python

 dialog.set_filter(filter)

2. Wahl per Dropdown-Menü: Der Nutzer kann zwischen mehreren vorgegebenen Filtern wählen:

.. code:: python

 dialog.add_filter(filter1)
 dialog.add_filter(filter2)
 ...

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 16_filechooser.glade xml

Python
******

.. listing:: 16_filechooser.py python

