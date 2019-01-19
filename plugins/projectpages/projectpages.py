# -*- coding: utf-8 -*-

# Copyright © 2014–2016, Chris Warrick.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import unicode_literals
import os
import json

from nikola.plugin_categories import Task
from nikola import utils


class ProjectPages(Task):
    """Render project indexes."""

    name = 'projectpages'
    dates = {}
    conf_project_path = 'projects'

    def set_site(self, site):
        """Set Nikola site."""
        site.register_path_handler('project', self.project_path)
        self.conf_project_path = site.config.get('PROJECT_PATH', 'projects')
        site._GLOBAL_CONTEXT['project_path'] = self.conf_project_path
        site._GLOBAL_CONTEXT['project_index'] = {}
        for lang, tpath in site.config['TRANSLATIONS'].items():
            site._GLOBAL_CONTEXT['project_index'][lang] = '/' + os.path.join(tpath, self.conf_project_path, site.config['INDEX_FILE']).replace('\\', '/')

        # If you want to use breadcrumbs as provided by the crumbs template:

        # def project_breadcrumbs(p, lang, translations, project_path):
        #     return (('/' + os.path.join(translations[lang], project_path, 'index.html').replace('\\', '/'), "Projects"), (p.permalink(), p.title()))
        # site._GLOBAL_CONTEXT['project_breadcrumbs'] = project_breadcrumbs

        return super(ProjectPages, self).set_site(site)

    def project_path(self, name, lang):
        """Generate links to project pages."""
        return [_f for _f in self.projects[name].permalink(lang).split('/') if _f]

    def is_project(self, p):
        """Test projecthood of a page."""
        return p.destination_path(lang=self.kw['default_lang']).startswith(self.conf_project_path)

    def find_projects(self):
        """Find all projects."""
        self._projects = [p for p in self.site.timeline if self.is_project(p)]

    @property
    def projects(self):
        """Look for projects if we haven’t already."""
        try:
            return self._projects
        except AttributeError:
            self.find_projects()
            return self._projects

    def generate_json(self, jdst, lang):
        """Generate a JSON file with all project data."""
        data = {}
        for p in self.projects:
            data[p.meta[lang]['slug']] = p.meta[lang]
            del data[p.meta[lang]['slug']]['date']
            if 'tags' in data[p.meta[lang]['slug']]:
                del data[p.meta[lang]['slug']]['tags']
            if 'hyphenate' in data[p.meta[lang]['slug']]:
                del data[p.meta[lang]['slug']]['hyphenate']
            data[p.meta[lang]['slug']]['permalink'] = p.permalink(lang)
            data[p.meta[lang]['slug']]['text'] = p.text(lang)
        with open(jdst, 'w') as fh:
            json.dump(data, fh, sort_keys=True, indent=4, separators=(',', ': '))

    def gen_tasks(self):
        """Render project list."""

        self.image_ext_list = ['.jpg', '.png', '.jpeg', '.gif', '.svg', '.bmp', '.tiff']
        self.image_ext_list.extend(self.site.config.get('EXTRA_IMAGE_EXTENSIONS', []))

        self.kw = {
            'project_path': self.conf_project_path,
            'index_file': self.site.config['INDEX_FILE'],
            'strip_indexes': self.site.config['STRIP_INDEXES'],
            'output_folder': self.site.config['OUTPUT_FOLDER'],
            'cache_folder': self.site.config['CACHE_FOLDER'],
            'default_lang': self.site.config['DEFAULT_LANG'],
            'filters': self.site.config['FILTERS'],
            'translations': self.site.config['TRANSLATIONS'],
            'global_context': self.site.GLOBAL_CONTEXT,
            'tzinfo': self.site.tzinfo,
        }

        for k, v in self.site.GLOBAL_CONTEXT['template_hooks'].items():
            self.kw['||template_hooks|{0}||'.format(k)] = v._items

        yield self.group_task()

        template_name = "projects.tmpl"

        self.site.scan_posts()
        self.find_projects()

        # Create index.html for each language
        for lang in self.kw['translations']:
            # save navigation links as dependencies
            self.kw['navigation_links|{0}'.format(lang)] = self.kw['global_context']['navigation_links'](lang)

            short_tdst = os.path.join(self.kw['translations'][lang], self.kw['project_path'], self.kw['index_file'])
            short_jdst = os.path.join(self.kw['translations'][lang], self.kw['project_path'], 'projects.json')
            tdst = os.path.normpath(os.path.join(self.kw['output_folder'], short_tdst))
            jdst = os.path.normpath(os.path.join(self.kw['output_folder'], short_jdst))

            context = {}
            context["lang"] = lang

            # TODO: tranlsations?
            context["title"] = "Projects"
            context["description"] = None

            def sortf(p):
                return ((-int(p.meta('sort')) if p.meta('sort') != '' else -1), p.title())

            context["featured"] = sorted((p for p in self.projects if p.meta('status').lower() == 'featured'), key=sortf)
            context["projects"] = sorted((p for p in self.projects if p.meta('status').lower() != 'private'), key=sortf)

            link = short_tdst.replace('\\', '/')
            index_len = len(self.kw['index_file'])
            if self.kw['strip_indexes'] and link[-(1 + index_len):] == '/' + self.kw['index_file']:
                link = link[:-index_len]
            context["permalink"] = '/' + link

            context["pagekind"] = ['projectpages']

            all_meta = [(p.title(), p.meta('devstatus')) for p in self.projects]
            all_meta += [p.meta('previewimage') for p in context["featured"]]
            all_meta += [p.source_path for p in context["featured"]]

            template_dep = self.site.template_system.template_deps(template_name)
            file_dep = []

            for p in self.projects:
                file_dep += [p.translated_base_path(l) for l in self.kw['translations'] if l in p.translated_to]

            yield utils.apply_filters({
                'basename': self.name,
                'name': tdst,
                'file_dep': file_dep + template_dep,
                'targets': [tdst],
                'actions': [
                    (self.site.render_template, (template_name, tdst, context))],
                'clean': True,
                'uptodate': [utils.config_changed({
                    1: self.kw,
                    2: all_meta,
                }, 'projectpages:html:' + tdst)],
            }, self.kw['filters'])

            yield utils.apply_filters({
                'basename': self.name,
                'name': jdst,
                'file_dep': file_dep,
                'targets': [jdst],
                'actions': [(self.generate_json, (jdst, lang))],
                'clean': True,
                'uptodate': [utils.config_changed({
                    1: self.kw,
                    2: all_meta,
                }, 'projectpages:json:' + jdst)],
            }, self.kw['filters'])
