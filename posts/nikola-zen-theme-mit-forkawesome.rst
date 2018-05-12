.. title: Nikola: everything zen
.. slug: nikola-zen-forkawesome
.. date: 2018-05-11 09:57:21 UTC+02:00
.. tags: nikola
.. category: 
.. link: 
.. description: 
.. type: text

*[UPDATE] Artikel wurde aktualisiert, keine manuelle Installation mehr notwendig*

**Aktualisiertes zen-Thema für Nikola**

Ein Nachteil von `Nikola <https://getnikola.com/>`_ ist meiner Meinung nach die stiefmütterliche Behandlung der `Themes <https://themes.getnikola.com/>`_. Das von mir genutzte *zen*-Thema hatte ich bereits vor einiger Zeit auf Font Awesome 4-Icons geupdated und hier als Archiv zum Download bereitgestellt.

Inzwischen gibt es nicht nur Version 5 von `Font Awesome <https://fontawesome.com/>`_, sondern auch einen Fork des Projektes namens `Fork Awesome <https://forkawesome.github.io>`_ mit ein paar neuen Icons.

Dank eines Kommentars einer der Nikola-Devs hier habe ich mich nun durchgerungen, meine Änderungen offiziell per Pull Request einzureichen. Die *zen*-Familie ist nun auch im offiziellen Repository auf Font Awesome v4.7.0 geupdatet. Außerdem gibt es eine neue Variante, die die Fork Awesome-Icons nutzt. Eine manuelle Installation erübrigt sich also, sie kann direkt im Nikola-Projektordner erfolgen:

.. code:: console

    $ nikola theme -i zen-forkawesome

Anschließend muss das Thema nur noch in der ``conf.py`` aktiviert werden:

.. code::

    THEME = "zen-forkawesome"

Desweiteren werden die Icons nun mit "fa fa-iconname" angesprochen statt zuvor mit "icon-iconname". Dies ist auch in ``conf.py.sample`` vermerkt und wird bei der Installation des Themas angezeigt.

Die Änderungen werden natürlich erst nach dem nächsten ``nikola build`` wirksam. Da *zen-forkawesome* auf *zen* basiert, wird dieses Thema automatisch mit installiert.


