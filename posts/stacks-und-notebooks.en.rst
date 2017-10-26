.. title: Stacks and notebooks
.. slug: stacksnotebooks
.. date: 2017-10-16 11:05:37 UTC+02:00
.. tags: glade,python
.. category: tutorial
.. link: 
.. description: 
.. type: text

.. class:: pull-right

.. contents::

**Organize contents on screen**

*Gtk.Stack* and *Gtk.Notebook* are layout containers that can hold any widgets.

A notebook provides a multipage layout including a classic tab functionality. A stack also provides this basic functionality and you will able to switch between different layout pages.

The main difference is the control widget of the stack is a separate widget (*Gtk.StackSwitcher*). Several stack switcher widgets can be assigned to one stack. A stack switcher can be placed into the headerbar and animated transitions between stack pages are supported.

Stack subjectively fit better into the GNOME environment but notebooks provide more customization/functionality options.

In the example there is a window containing a stack including a notebook on the third page showing different websites.

.. thumbnail:: /images/21_stacknotebook.png

Glade
-----

Stack
*****

Stacks can be found in the sidebar's 'Container' section. Pages are easily created and edited via Glade. Sub-widgets in the example file are *Gtk.Image*, `Vte.Terminal <link://slug/exterminate>`__ and *Gtk.Notebook*.

The stack switcher widget can be obtained from 'Controls and Display' and is placed to the headerbar. It's also possible to put it into a regular container widget like boxes. Pages can be shown in vertical or horizontal order. In *"General > Stack"* a stack element must be assigned to the widget. The page name shown by the stack switcher widget can be edited via *"Packing > Title"* of the sub-widget. This sub-widget has to be created in the first place, a new created stack has empty pages.

Notebook
********

Notebook can also be found in the 'Container' section. The tab's control unit is an integrated label child widget automatically generated on page creation. *Gtk.ScrolledWindows* are used here as the pages' container widgets. These are also required for displaying (long) tables (see also List-/TreeStore articles `No. 1 <link://slug/uberlistet>`__ und `No. 2 <link://slug/ansichtssache>`__).

The tab bar of a notebook provides reserved space for additional widgets like fixed buttons (*"General > Start/End Action"*). In the example there will be created a "Home" button in the start area.

Python
------

There are no signals required for switching between stack pages and notebook tabs. In the example only two signals are assigned, one for catching the "exit" command within the terminal and one for the button in the notebook tab bar.

WebKit2
*******

The webpages in the example are rendered by WebKit2. The essential module to use is ``WebKit2.WebView``. A new WebView object itself already is a scrollable Gtk+ widget within a *Gtk.Viewport* element. According to the `API reference <https://webkitgtk.org/reference/webkit2gtk/stable/WebKitWebView.html>`__ it does not have to be placed in a *Gtk.ScrolledWindow* container widget. Having tested this that works for *Gtk.Stack* but not for *Gtk.Notebook*. That's why in the example there is used a ScrolledWindow as underlying container widget.

The following pattern is used to create a WebView widget:

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
    <a class="discuss-on-gplus" href="https://plus.google.com/105146352752269764996/posts/hMeC12mMhKJ">Comment on <i class="fa fa-google-plus"></i></a>
