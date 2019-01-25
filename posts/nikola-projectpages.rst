.. title: Use Nikola's Project Pages plugin without Bootstrap theme
.. slug: nikola-projectpages
.. date: 2019-01-24 09:35:17 UTC+01:00
.. tags: nikola
.. category: 
.. link: 
.. description: 
.. type: text

**Nikola is a great static site generator with lots of available plugins to extend its functionality.**

One of these plugins is the `Project Pages plugin <https://plugins.getnikola.com/v8/projectpages/>`_. The principle of it is that you create source files with (meta) information in a determined 'projects' folder and Nikola generates an index site and one page per project. You can see what it looks like on the `developer's website <https://chriswarrick.com/projects>`_ or `here at my site <../../projects/index.html>`_.

The plugins' templates are based on using a Boostrap theme. If you are using other themes you will run into two problems:

 * table and other formatting
 * carousel of the featured projects

CSS
***

Adding/Altering style parameter of a theme is easy: go to ``/themes/CURRENT_THEME/asstes/css/`` and edit the ``custom.css``. If you want to use a separate file put it in this very folder and add the filename to ``/themes/CURRENT_THEME/bundles``.

First I had to find the missing CSS assignments in the Bootstrap theme's CSS file. You can download the resulting file so you don't have to do this again.

Carousel
********

The `Bootstrap carousel <https://www.w3schools.com/bootstrap/bootstrap_carousel.asp>`_ is a plugin to create nifty and automatic slideshows.

The plugin generates a carousel on the index page for every project that is tagged as

.. code::

    .. status: featured

I decided that a pure CSS slider may not be animated but still an acceptable JS-free solution. To realize this you have to edit the ``project.tmpl`` which is located in ``plugins/projectpages/templates/TEMPLATE_ENGINE/``.

If you go with `this simple slider <https://codepen.io/paulnoble/pen/ZYOzLG>`_ you will need just a few lines above the "All projects" section:

.. code:: html

    % if featured:
    <div class="carousel">
      % for p in featured:
      <input type="checkbox" class="faux-ui-facia">
      <div class="slide" annot="${p.title()}">
        <img src="${p.meta('previewimage')}" alt="${p.title()}">
      </div>
      % endfor
    </div>
    % endif

Next step is adding the slider's CSS assignments to your custom CSS (see above).

On the project's summary page I considered it better to put the description into the detail's box so I also altered the ``project.tmpl``.

Files
*****

* CSS file to add to your theme

    * `projectfiles.css`__

__ /files/projectpages/projectpages.css


* Mako templates

    * `projects.tmpl`__
    * `project.tmpl`__

__ /files/projectpages/mako/projects.tmpl
__ /files/projectpages/mako/project.tmpl

* Jinja templates

    * `projects.tmpl`__
    * `project.tmpl`__

__ /files/projectpages/jinja/projects.tmpl
__ /files/projectpages/jinja/project.tmpl
