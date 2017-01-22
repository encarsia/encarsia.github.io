.. title: Ansichtssache
.. slug: ansichtssache
.. date: 2016-12-22 00:02:20 UTC+01:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: warning pull-right

.. contents::

**Daten anzeigen mit TreeStore**

(Fortsetzung zum `ListStore-Artikel <link://slug/uberlistet>`_)

.. thumbnail:: /images/12_treestore.png
    :width: 480

TreeStore vs. ListStore
-----------------------

Im Gegensatz zum ListStore können Zeilen eines TreeStores ihrerseits Kind-Elemente besitzen, die ``append``-Funktion benötigt demzufolge ein weiteren Parameter, der einen Bezug zu einer anderen Datenzeile anzeigt:

.. code-block:: python

    #append row to liststore
    store.append([value1,value2,value3])
    
    #append row to treestore
    store.append(parent,[value1,value2,value3])

Der Wert der Variable *parent* ist entweder

* **None**, wenn die Zeile keine übergeordnete Zeile besitzt, oder
* **TreeIter**, der zur übergeordneten Zeile zeigt

Der TreeIter wird beim Erstellen einer Zeile erzeugt, untergeordnete Zeilen werden nach folgendem Schema angelegt:

.. code-block:: python

    row1 = store.append(None,[value1,value2,value3])
    row2 = store.append(row1,[value1,value2,value3])

Man erhält den *TreeIter*-Wert einer Zeile am einfachsten über die ``get_selection``-Funktion des *GtkTreeSelection*-Widgets von TreeView (wird automatisch angelegt).

Glade
-----

Im Beispiel werden zwei TreeStores und die jeweils enthaltenen Spalten angelegt, dazu die TreeView-Widgets zur Anzeige.

TreeModelSort
*************

Spalten lassen sich mit der Funktion ``set_sort_column_id`` einfach sortieren. Wendet man diese Funktion direkt auf TreeStore an, werden logischerweise alle TreeView-Widgets, die darauf zurückgreifen, sortiert.

Für diese Fälle muss man *TreeModelSort*-Elemente "zwischenschalten", d.h. man erstellt aus der Widget-Seitenleiste unter *"Sonstiges > Sortierung für Baumansichtsmodell"* (4. Eintrag) ein Widget und weist ihm den gewünschten TreeStore zu (einzige Option unter "Allgemein"). Anschließend ersetzt man im TreeView das Modell mit dem eben erstellten TreeModelSort.

Die Sortierungsfunktion führt man wie zuvor, nur auf das TreeModelSort-Objekt, aus.

TreeModelFilter
***************

*TreeModelFilter* ermöglicht die Darstellung bestimmter Zeilen, in Glade wird wie bei TreeModelSort verfahren, zuerst das Element anlegen (3. Eintrag unter "Sonstige"), anschließend erfolgen die Zuweisungen zum Modell und TreeView.

Im gewählten Beispiel sollen Sorten nach der Fruchtfarbe sortiert werden, es wird also noch ein Container für Buttons benötigt, also eine *GtkButtonBox*.


Formatierung aus dem Modell laden
*********************************

Neben den anzuzeigenden Spalten gibt es im ersten TreeStore eine Spalte "weight". Der Wert in dieser Spalte wird dazu verwendet, die Zelle in Fettschrift darzustellen. Dazu wird in den Eigenschaften des CellRenderers unter *Schriftgewicht* die entsprechende Spalte angegeben (der Wert für normale Schrift ist 400). Analog dazu können beispielsweise auch Zellen eingefärbt oder weitere Schriftformatierungen vorgenommen werden.

Python
------

TreeModelSort
*************

Durch die Positionsabfrage von ``GtkTreeSelection.get_selected()`` erhält man ein Tupel (model,pos), *pos* von *model* zeigt dabei auf TreeModelSort (bzw. analog auf TreeModelFilter), nicht auf TreeStore und erfordert eine Konvertierung:

.. code-block:: python

    model,pos = selection.get_selected()
    converted_iter = treesort.convert_iter_to_child_iter(pos)
    store.set_value(converted_iter,column,value)


TreeModelFilter
***************

Zunächst muss eine Filterfunktion erstellt werden, in der die Sichtbarkeit von Zeilen definiert wird, im Beispiel also die Variable *self.color*:

.. code-block:: python

    def color_filter_func(self,model,iter,data):
        if model[iter][2] == self.color:
            return True
        else:
            return False

Die Funktion wird zunächst nach dem Schema

.. code-block:: python

    treefilter.set_visible_func(filter_func)

zugewiesen, jede Filterung wird dann per ``refilter()`` ausgelöst, also wenn das Button-Signal ausgelöst wird:

.. code-block:: python

    def on_button_clicked(self,widget):
        x.color = widget.get_label()
        x.obj("treefilter").refilter()

.. TEASER_END

Listings
--------

Glade
*****

.. listing:: 12_treestore.glade xml

Python
******

.. listing:: 12_treestore.py python

