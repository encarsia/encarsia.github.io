.. title: Stacks und Notebooks
.. slug: stacksnotebooks
.. date: 2017-10-16 11:05:37 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Inhalte organisiert anzeigen**

*Gtk.Stack* und *Gtk.Notebook* sind Layout-Container, die ihrerseits beliebige Widgets enthalten können.

Ein Notebook stellt ein mehrseitiges Layout mit klassischer Tab-Funktionalität zur Verfügung. Stacks bieten die gleiche Grundfunktionalität, nämlich mehrere Container innerhalb eines Widgets zu enthalten, zwischen denen man hin- und herschalten kann.

Der Hauptunterschied besteht darin, dass das Bedienelement des Stacks als separates Widget verwendet werden muss (*Gtk.StackSwitcher*). Verschiedene StackSwitcher können dabei auf den selben Stack zugreifen. Weiterhin lassen sich StackSwitcher in Headerbars platzieren, außerdem werden animierte Überblenden zwischen den Stack-Seiten unterstützt.

Stacks passen sich subjektiv besser in die GNOME-Umgebung ein, bieten aber nicht ganz so große Funktionalität wie Notebooks.

Das Beispiel enhält ein Fenster mit Stack, in dessen dritter Seite ein Notebook enthalten ist, das verschiedene Webseiten anzeigt.

.. thumbnail:: /images/21_stacknotebook.png

Glade
-----

Stack
*****

Ein Stack, zu finden in der Sidebar unter "Container", und dessen Unterseiten lassen sich einfach in Glade erstellen und bearbeiten. Als Unterwidgets kommen im Beispiel *Gtk.Image*, `Vte.Terminal <link://slug/exterminate>`__ und *Gtk.Notebook* zum Einsatz.

Das StackSwitcher-Widget befindet sich unter "Steuerung und Anzeige" und wird der Headerbar hinzugefügt. Es kann aber auch in reguläre Container-Widgets wie einer Box platziert und die Unterseiten horizontal oder vertikal angezeigt werden. Unter "Allgemein > Stapel" wird der Stack ausgewählt, auf den sich das Widget beziehen soll. Die anzuzeigende Seitenbezeichnung wird im jeweiligen Stack-Unterwidget unter "Packen > Titel" festgelegt.

Notebook
********

Das Notebook findet sich ebenfalls unter "Container". Die Steuerungseinheit des Tabs ist ein bei Erstellung einer Seite generiertes Label-Child-Widget. Als Container-Widgets der Unterseiten werden hier *Gtk.ScrolledWindows* verwendet. Diese benötigt man auch z.B. für die Anzeige von (längeren) Tabellen (siehe auch Artikel zu List-/TreeStores `Nr. 1 <link://slug/uberlistet>`__ und `Nr. 2 <link://slug/ansichtssache>`__).

Die Tab-Leiste des Notebooks bietet die Möglichkeit, sowohl am Anfang als auch am Ende ein Container-Widget bereitzustellen (unter "Allgemein > Start-Aktion/End-Aktion"), in dem zum Beispiel feste Buttons untergebracht werden können. Im Beispiel wird am Anfang ein "Home"-Button eingerichtet.

Python
------

Für das Umherschalten zwischen Stack-Unterseiten und Notebook-Tabs werden keine Signale benötigt. Im Beispiel werden nur zwei Signale benötigt, einmal für das Abfangen des "exit"-Kommandos innerhalb des Terminals und für den Button in der Notebook-Tableiste.

WebKit2
*******

Die Darstellung von Webseiten wird im Beispiel von WebKit2 erledigt. Das zentrale Modul dabei ist ``WebKit2.WebView``. Ein neues WebView-Objekt selbst ist bereits ein scrollbares Gtk-Widget in einem *Gtk.Viewport*, muss also laut `API-Referenz <https://webkitgtk.org/reference/webkit2gtk/stable/WebKitWebView.html>`__ nicht mehr in ein *Gtk.ScrolledWindow* platziert werden. Dies funktionierte im Test zwar für *Gtk.Stack*, nicht aber für *Gtk.Notebook*, weshalb dort trotzdem als "Unterlage" ein ScrolledWindow-Widget verwendet wird.

Das WebView-Widget wird nach folgendem Muster erstellt:

.. code:: python

    #create new WebView widget
    webview = WebKit2.WebView()
    #send URL to widget
    webview.load_uri("http://google.com")
    #add webview to notebook
    notebook.add(webview)
    #add webview to stack
    stack.add_titled(webview, name, "StackSwitcher title")

    webview.show()

.. TEASER_END

Listings
--------

Python
******

.. listing:: 21_stacknotebook.py python

Glade
*****

.. listing:: 21_stacknotebook.glade xml

.. raw:: html

    <br>
    <a class="discuss-on-gplus" href="https://plus.google.com/105146352752269764996/posts/6ER8kNNkCx9">Kommentieren auf <i class="fa fa-google-plus"></i></a>
