.. title: NoN: Fortschritte
.. slug: non-fortschritte
.. date: 2017-01-08 22:18:52 UTC+01:00
.. tags: nikola,python
.. category: repository
.. link: 
.. description: 
.. type: text

**Knights of Ni - Fortschritte**

Wie `bereits erwähnt <link://slug/neues-projekt-knights-of-ni>`_, bastel ich aktuell an einer GUI für `Nikola <https://getnikola.com>`_, die einige Fortschritte vorzuweisen hat:

* Titelleiste entfernt, da Headerbar benutzt wird
* Wechseln zwischen Nikola-Instanzen (zuletzt benutzte wird gespeichert)
* Bookmarkfunktion (bislang können nur Bookmarks hinzugefügt werden, bei Bedarf manuell aus der config entfernen)
* Untersützung für mehrsprachige Seiten:

 * Anzeige der Standardsprache und der konfigurierten anderen Sprachen
 * Posts/Pages-Tab zeigt Vorhandensein von Übersetzungen an
 * Tab "Translations" zeigt vorhandene Dateien an
 * per Rechtsklick können neue Übersetzungen angelegt werden, dabei wird der Ausgangsbeitrag gemäß entsprechendem Dateimuster gespeichert
 * *ich weiß noch nicht, wie sinnvoll dieser separate Tab ist (Redundanz) und ob ich ihn beibehalte*

* hat der Artikel keinen Titel, wird das interne Kürzel (slug) oder, falls ebenfalls nicht vorhanden, der Dateiname angezeigt
* gesprächiges Log, um vorzutäuschen, dass ganz viel wichtiger Kram passiert

.. thumbnail:: /images/non2.png


Das läuft aus meiner Sicht schon alles erstaunlich gut. Dummerweise habe ich bei der Verwendung von Glade (und auch Python, aber vor allem Glade) inzwischen ebenfalls einige Fortschritte gemacht, was mich ernsthaft zur Überlegung geführt hat, das GoProTool nochmal zu überarbeiten. Die Oberfläche würde ich belassen, aber viel Funktionalität könnte effizienter umgesetzt werden. Ich stelle das mal hinten an.

Geplant ist nun ein simples Nikola-unabhängiges Vorlagensystem und anschließend ist etwas Fleißarbeit bei der Lokalisation erforderlich.