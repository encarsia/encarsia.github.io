.. title: Texteditor mit GtkSourceView
.. slug: gtksv
.. date: 2017-11-11 18:27:40 UC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Text-Widget mit GtkSourceView**

Gtk+ bietet mit *Gtk.TextView* ein Widget zum Anzeigen und Bearbeiten von Text/-dateien an. Wie beim `TreeView-Widget <link://slug/uberlistet>`_ werden die Daten (model) und die Anzeige (view) getrennt voneinander gehandhabt. Das datentragende Modell zu *TextView* ist *TextBuffer*.

GtkSourceView_ ist eine Erweiterung und Unterklasse von TextView, die Syntaxhighlighting, Farbschemata, Laden/Speichern, Vervollständigung und andere Funktionen unterstützt.

Im Beispiel wird ein Editor ergestellt, der bestimmte Dateien laden und speichern kann, sowie eine rudimentäre Suchfunktion und ein Widget zum Farbschemawechseln bereitstellt.

.. thumbnail:: /images/22_editor_gtksv.png
    :width: 600px

Glade
-----

GtkSourceView
*************

Die SourceView-Widgets befinden sich unterhalb einer eigenen gleichnamigen Hauptkategorie in der Seitenleiste.

* **GtkSourceView**: das eigentliche Editorwidget, das in einem *ScrolledWindow* platziert wird
* **GtkSourceMap**: Miniaturansicht und Unterklasse von SourceView
* **GtkSourceStyleSchemeChooserWidget**: Widget zur Auswahl eines StyleSchemes

In Glade lassen sich bereits viele Eigenschaften des Editorbereichs festlegen wie die Anzeige der Zeilennummern, Einrückung, Umbruchverhalten usw., die sich natürlich auch über ``set_property`` festlegen oder ändern lassen.

Beim StyleChooser-Widget wird das Signal ``button-release-event`` belegt, um das ausgewählte StyleScheme auf die SourceView-Widgets anzuwenden.

SourceMap
*********

Das Widget muss mit der anzuzeigenden Quelle, einem SourceView-Widget, verknüpft werden (über *"Allgemein > View"*). Es wird dann der Inhalt des SourceView-Widgets verkleinert (standardmäßig mit Schriftgröße in 1pt) angezeigt. Durch scrollen in SourceMap verändert man gleichzeitig die Anzeige in SourceView.

Headerbar
*********

Die Headerbar enthält verschiedene Buttons zum Laden, Suchen und Speichern:

* "Python file" und "Glade file" laden die entsprechenden Dateien dieses Beispieles in den Editor (Signal ``clicked``)
* Die Sucheingabe ist ein *Gtk.SearchEntry*-Widget (Signale ``search-changed`` und ``activate``)
* "Save .bak" und "Save" speichern die Dateien (Signal ``clicked``)

Python
------

SourceView
**********

Initialisierung
===============

Widgets, die nicht zum *Gtk*-Modul gehören, müssen zunächst als initialisiert werden (siehe auch `Vte-Terminal <link://slug/exterminate>`_):

.. code:: python

    GObject.type_register(GtkSource.View)

Das SourceView-Widget besitzt bereits einen integrierten Textbuffer, welcher mit ``get_buffer`` abgefragt werden kann:

.. code:: python

    self.buffer = self.view.get_buffer()

Desweiteren werden noch Objekte zum Laden und Speichern von Dateien sowie fürs Syntaxhighlighting benötigt:

.. code:: python

    self.sourcefile = GtkSource.File()
    self.lang_manager = GtkSource.LanguageManager()

Datei laden
===========

Die zu öffnende Datei muss dem *GtkSource.File*-Objekt im *Gio.File*-Format und anschließend an *GtkSource.FileLoader* übergeben werden. Die Information zum Syntaxhighlighting erhält der Buffer:

.. code-block:: python

    sourcefile.set_location(Gio.File.new_for_path("file"))
    buffer.set_language(self.lang_manager.get_language("language"))
    loader = GtkSource.FileLoader.new(buffer, sourcefile)
    loader.load_async(0, None, None, None, None, None)

Datei speichern
===============

Analog zum Laden erfolgt das Speichern mit *GtkSource.FileSaver*. Im Beispiel speichert der "Save"-Button die bestehende Datei (es erfolgt keine "Überschreiben?"-Sicherheitsabfrage) und der "Save .bak"-Button speichert den Inhalt als neue Datei mit genannter Endung ab. Die Übergabe der Dateien erfolgt wie beim Laden *Gio.File*-formatiert:

.. code-block:: python

    #bestehende Datei überschreiben
    saver = GtkSource.FileSaver.new(buffer, sourcefile)
    #Datei unter anderem Namen speichern
    saver = GtkSource.FileSaver.new_with_target(buffer, sourcefile, targetfile)
    #Speichern ausführen
    saver.save_async(0, None, None, None, None, None)

Text hervorheben
================

Zunächst ist festzustellen, dass es sich bei den Funktionen suchen(/ersetzen)/markieren und Texthervorhebungen um zwei getrennt voneinander auszuführenden Mechanismen handelt, für die *GtkSource.Settings* eingerichtet werden müssen:

.. code-block:: python

    settings = GtkSource.SearchSettings()
    search_context = GtkSource.SearchContext.new(buffer, settings)

Alle Vorkommen eines Strings im TextView lassen sich auf zwei Arten visualisieren, einer naheliegenden und einer eleganten.

Die naheliegende Lösung ist die Ausführung von ``settings.get_search_text`` bei der Eingabe von Text in das Suchfeld (Signal ``search-changed``):

Die andere Möglichkeit, bei der kein Signal benötigt wird, ist die direkte Anbindung der SearchSettings-Eigenschaft "search-text" an das Sucheingabefeld:

.. code-block:: python

    builder.get_object("search_entry").bind_property('text', settings, 'search-text')

Text markieren
==============

*GtkSource.SearchContext* wird für die Suchen-/Ersetzen-Funktion innerhalb eines *GtkSource.Buffer* verwendet. Dieser wurde bereits mit den SearchSettings initialisiert.

Die Markierungsfunktionen und Cursorplatzierung erbt *GtkSource.Buffer* von *Gtk.TextBuffer*, die Suche wird mit SeachContexts ``forward2`` ausgeführt.

.. code-block:: python

    def find_text(self, start_offset=1):
        buf = self.buffer
        insert = buf.get_iter_at_mark(buf.get_insert())
        start, end = buf.get_bounds()
        insert.forward_chars(start_offset)
        match, start_iter, end_iter, wrapped = self.search_context.forward2(insert)

        if match:
            buf.place_cursor(start_iter)
            buf.move_mark(buf.get_selection_bound(), end_iter)
            self.view.scroll_to_mark(buf.get_insert(), 0.25, True, 0.5, 0.5)
            return True
        else:
            buf.place_cursor(buf.get_iter_at_mark(buf.get_insert()))

Durch die Signalbindung von ``activate`` im Suchfeld wird die Suche durch Drücken der Eingabetaste an der letzten Position fortgeführt. Für eine Rückwärtssuche muss analog zu ``forward2`` oder ``forward_async`` ``backward2`` oder ``backward_async`` verwendet werden.

StyleChooser
************

Das Widget zeigt die verfügbaren Stile an. Es ist nicht möglich, lokale Stile anzugeben oder sie zu verändern.

Der angewählte Style lässt sich dann einfach auf den gewünschten Buffer anwenden:

.. code-block:: python

    def on_signal_emitted(self, widget, event):
        buffer.set_style_scheme(widget.get_style_scheme())

.. image:: /images/22_editor_gtksv.gif

Links
-----

* `GtkSourceView <https://wiki.gnome.org/Projects/GtkSourceView>`_
* `GtkSourceView 3 Reference Manual <https://developer.gnome.org/gtksourceview/stable/>`_
* `GtkSourceView style schemes <https://wiki.gnome.org/Projects/GtkSourceView/StyleSchemes>`_
* `Text Widget Overview <https://developer.gnome.org/gtk3/stable/TextWidget.html>`_
* `Multiline Text Editor-Tutorial <http://python-gtk-3-tutorial.readthedocs.io/en/latest/textview.html>`_
* `meld <http://meldmerge.org/>`_, `Repository auf GitHub <https://github.com/GNOME/meld>`_


.. TEASER_END

Listings
--------

Python
******

.. listing:: 22_editor_gtksv.py python

Glade
*****

.. listing:: 22_editor_gtksv.glade xml

.. raw:: html

    <br>
    <a class="discuss-on-gplus" href="https://plus.google.com/105146352752269764996/posts/g7qQT8wi5bJ">Kommentieren auf <i class="fa fa-google-plus"></i></a>

