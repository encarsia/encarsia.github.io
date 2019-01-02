.. title: Überlistet
.. slug: uberlistet
.. date: 2016-11-24 17:55:14 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Daten in ListStore speichern und mit ComboBox und TreeView anzeigen**

Für die Speicherung und Anzeige von Daten in Listen- oder Tabellenform benötigt man in GTK+-Anwendungen verschiedene Elemente:

1. Im Modell werden die Daten verwaltet, es gibt zwei Typen:
    
    * *ListStore:* flache Liste, die Spalten können neben Text-, Zahlenwerten auch GTK+-Elemente (z.B. Buttons, Checkboxen) enthalten
    * *TreeStore:* funktioniert prinzipiell wie ListStore, Zeilen können ihrerseits Kind-Einträge besitzen, Daten können im Gegensatz zu ListStore nicht in Glade angegeben werden (`TreeStore-Artikel <link://slug/ansichtssache>`_)

2. Widgets:

    * *TreeView:* dieses Widget eignet sich zum Anzeigen, Sortieren, Bearbeiten von Daten, wird von beiden Modelltypen verwendet; es können parallel mehrere TreeView-Widgets angelegt werden, die auf dieselbe Datenbasis (Modell) zurückgreifen, aber zum Beispiel verschiedene Spalten anzeigen
    * *ComboBox:* Comboboxen dienen der Auswahl aus einer gegebenen Liste, deren Datenbasis ein List- oder TreeStore sein kann (siehe Artikel zu `Spinbutton und Combobox <link://slug/qual-der-wahl>`_)
    * *CellRenderers:* Unterwidgets, in denen die anzuzeigenden Daten, deren Layout und weitere Optionen wie Bearbeitbarkeit festgelegt werden

.. thumbnail:: /images/09_treestore2.png

Glade
-----

ListStore
*********

Um die Vielseitigkeit von ListStore zu skizzieren, wird im Beispiel ein *Gtk.ListStore* (zu finden in der Elementauswahl links unter *"Sonstiges > Listenverwahrung"*) erstellt und von drei Widgets verwendet.

Zunächst werden ein paar Spalten erstellt. ListStore-Daten lassen sich direkt in Glade eingeben. Dies ist allerdings nur für wenige Zeilen und Spalten praktikabel und übersichtlich. Selbst wenige Daten würde ich immer direkt im Python-Code einlesen.

Wie man sieht, werden Änderungen im ListStore (Sortierung, Inhalt) sofort in allen Widgets aktualisiert, die auf dieses Objekt zugreifen. Für verschiedene Sortierungen des selben List-/TreeStores muss man *Gtk.TreeModelSort* anwenden (Beispiel siehe `TreeStore-Artikel <link://slug/ansichtssache>`_).

.. thumbnail:: /images/09_treestore1.png

Widgets
*******

ComboBox
    Als "Baumansichtsmodell" wird wie auch bei den folgenden Widgets der ListStore ausgewählt. Über *"Edit > Hierarchie"* ein CellRendererText hinzugefügt. Im ersten Feld ("Text") stellt man ein, aus welcher Spalte das Dropdown-Menü angezeigt werden soll. Um die Auswahl zu verarbeiten, wird das Signal *changed* belegt.

TreeView #1
    Das erste TreeView-Widget wird innerhalb eines *Gtk.ScrolledWindow*-Containers angelegt. Wie bei ComboBox werden nun beliebige CellRenderer angelegt. Wird der Sortierungsanzeiger aktiviert, können die Spalten mit Klick auf den Spaltenkopf sortiert werden. In der Sortierspaltenkennung wird die Spalte angegeben, nach der sortiert werden soll, auf diese Weise kann man eine Spalte auch gemäß einer anderen Spalte sortieren (hier im Beispiel wird die mittlere Spalte nach der letzten sortiert, die Sortierung der beiden hinteren Spalten liefert also das gleiche Ergebnis.

TreeView #2
    Das zweite TreeView-Widget wird innerhalb eines Sichtfeldes (*Gtk.Viewport*) erstellt. Dieser Container bietet keine Scrollbalken, das Widget vergrößert automatisch, so dass alle Zeilen sichtbar sind. Bei größeren Tabellen ist ein ScrolledWindow also praktikabler.
    Es werden die gleichen Daten angezeigt wie zuvor, allerdings ohne Sortierungsanzeiger, dafür wird die mittlere Spalte ("Description") editierbar gemacht und erhält eine Funktion für das Signal *edited*.

Button
    Ein Klick auf den Button soll jeweils eine weitere Zeile zum ListStore hinzufügen, es wird also das *clicked*-Signal belegt.


Python
------

TreeStore
*********

Die in TreeStore vorhandenen Zeilen lassen sich einfach über ``for row in store`` abrufen. Neue Zeilen lassen sich mit ``append`` hinzufügen, andere Optionen wären ``insert`` oder ``remove``, um Zeilen an bestimmten Positionen einzufügen oder zu entfernen.

ComboBox
********

Normalerweise benötigt man für den Zugang zu einer Datenzeile einen *TreeIter*, das Objekt, das auf den Pfad im Modell zeigt (alternativ kann man diese auch über *TreePath* ansprechen).

.. code-block:: python

    iter, model = widget.get_active_iter(), widget.get_model()
    row = model[iter]
    print("Selection:", row[0])

Zellen bearbeiten
*****************

Das *edited*-Signal übergibt als Parameter die bearbeitete Zeile und den neuen Zelleninhalt. Dieser muss allerdings explizit als neuer Zelleninhalt übergeben werden, sonst zeigt die Zelle nach der Bearbeitung wieder den alten Inhalt an. Dafür kann man einfach die vom Widget übergebene Position (TreePath) statt des TreeIters verwenden.

.. code-block:: python

    def on_cellrenderer_descr_edited(self, widget, pos, edit):
        x.store[int(pos)][1] = edit

Listings
--------

Python
******

.. listing:: 09_liststore.py python

Glade
*****

.. listing:: 09_liststore.glade xml
