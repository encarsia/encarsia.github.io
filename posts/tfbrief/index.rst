.. title: tfbrief - LaTeX-Briefvorlage
.. slug: tfbrief
.. date: 2018-09-14 16:12:31 UTC+02:00
.. tags: tfbrief,latex,letter
.. category: latex
.. link: 
.. description: 
.. type: text

**Manche raunen, Briefe mit LaTeX zu verfassen, wäre mit Kanonen auf Spatzen zu feuern. Die kennen die Dokumentenklasse tfbrief nicht.**

*tfbrief* fiel mir einst vor Jahren zu und begeistert ob seiner Einfachheit nutzte ich es eifrig und  verbreitete es fleißig unter Interessierten. Die Originalquelle ist inzwischen versiegt, doch ich konnte eine einsame Kopie auf GitHub ausfindig machen. Dabei stellte ich fest, dass die Dokumentenklasse quasi unverändert und weitgehend unter Ausschluss der Öffentlichkeit existierte.

Meine Änderungen:
 * obsoleten Code entfernen (fixltx2e package, tocityshort-Attribut)
 * die Option `german` lädt `ngerman`, wenn babel geladen wird
 * Typos (v.a. der Kommafehler in Abschlussformel (im Deutschen nicht vorhanden))
 * Betreffzeile serifenlos
 * eine weitere Beispieldatei
 * PDF-Outputs der Beispiele
 * ausführliche Dokumentation

Link zum Repository: `GitHub: andre-lehnert/latex-letter <https://github.com/andre-lehnert/latex-letter>`_
