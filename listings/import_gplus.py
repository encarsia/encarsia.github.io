# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os
import shutil

try:
    import bs4
except ModuleNotFoundError:
    raise

from nikola.plugin_categories import Command
from nikola import utils
from nikola.utils import req_missing
from nikola.plugins.basic_import import ImportMixin
from nikola.plugins.command.init import SAMPLE_CONF, prepare_config

LOGGER = utils.get_logger('import_gplus', utils.STDERR_HANDLER)


class CommandImportGplus(Command, ImportMixin):
    """Import a Google+ dump."""

    name = "import_gplus"
    needs_config = False
    doc_usage = "[options] extracted_dump_file_folder"
    doc_purpose = "import a Google+ dump"
    cmd_options = ImportMixin.cmd_options

    def _execute(self, options, args):
        '''
            Import Google+ dump
        '''

        if not args:
            print(self.help())
            return

        options['filename'] = args[0]
        self.export_folder = options['filename']
        self.output_folder = options['output_folder']
        self.import_into_existing_site = False
        self.url_map = {}

        # Google Takeout folder structure, adapt to your language settings
        
        # Takeout/
        # ├── +1/
        # ├── Google+ stream/
        # |   ├── Posts/
        # |   ├── Photos/
        # |   |   ├── Photos of posts/
        # |   |   └── Photos of polls/
        # |   ├── Activities/
        # |   ├── Collections/
        # |   └── Events/
        # ├── Google+ Communities/
        # └── index.html
        
        gto_root = "Takeout"
        gto_plus1 = "+1"
        gto_stream = "Stream in Google+"
        gto_posts = "Beiträge"
        gto_photos = "Fotos"
        gto_photos_posts = "Fotos von Beiträgen"
        gto_photos_polls = "Umfragefotos"
        gto_activity = "Aktivitätsprotokoll"
        gto_collections = "Sammlungen"
        gto_events = "Veranstaltungen"
        gto_communities = "Google+ Communities"

        # path to HTML formatted post files
        post_path = os.path.join(self.export_folder,
                                 gto_root,
                                 gto_stream,
                                 gto_posts)
        
        # collect all files
        files = [f for f in os.listdir(os.path.join(post_path)) if os.path.isfile(os.path.join(post_path, f))]

        # filter relevant HTML files
        html_files = [f for f in files if f.endswith(".html")]
        LOGGER.info("{} posts ready for import".format(len(html_files)))
        
        # init new Nikola site "new_site", edit conf.py to your needs
        # change to this folder for the for build process
        self.context = self.populate_context(self.export_folder, html_files, post_path)
        conf_template = self.generate_base_site()
        self.write_configuration(self.get_configuration_output_path(), conf_template.render(**prepare_config(self.context)))
        self.import_posts(self.export_folder, html_files, post_path)
        
        # In the Takeout archive photos are linked to the main working
        # directory although they do not necessarily exist there (Hello
        # deadlinks!). The image files are spread to several folders.

        # All archive photos will be copied to the "images" folder.
        try:
            os.makedirs(os.path.join(self.output_folder, "images"))
            LOGGER.info("Image folder ceated.")
        except:
            pass

        for root, dirs, files in os.walk(os.path.join(self.export_folder, gto_root)):
            for f in files:
                if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg") or f.lower().endswith(".png"):
                    if not os.path.isfile(os.path.join(self.output_folder, "images",f)):
                        shutil.copy2(os.path.join(root, f), os.path.join(self.output_folder, "images"))
                        LOGGER.info("{} copied to Nikola image folder.".format(f))
        
    @staticmethod
    def populate_context(folder, names, path):
        # We don't get much data here
        context = SAMPLE_CONF.copy()
        context['DEFAULT_LANG'] = 'de'
        context['BLOG_DESCRIPTION'] = ''
        context['SITE_URL'] = 'http://localhost:8000/'
        context['BLOG_EMAIL'] = ''
        context['BLOG_TITLE'] = "Static G+ stream archive"

        # Get any random post, all have the same data
        with open(os.path.join(path, names[0])) as f:
            soup = bs4.BeautifulSoup(f, "html.parser")
            context['BLOG_AUTHOR'] = soup.find("a", "author").text

        context['POSTS'] = '''(
            ("posts/*.html", "posts", "post.tmpl"),
            ("posts/*.rst", "posts", "post.tmpl"),
        )'''
        context['COMPILERS'] = '''{
        "rest": ('.txt', '.rst'),
        "html": ('.html', '.htm')
        }
        '''
        return context

    def import_posts(self, folder, names, path):
        """Import all posts."""
        self.out_folder = 'posts'

        for name in names:
            with open(os.path.join(path, name)) as f:
                soup = bs4.BeautifulSoup(f, "html.parser")
                
                description = ""
                tags = []
                
                title_string = str(soup.title.string)
                title = self.prettify_title(title_string)
                
                # post date is the 2nd link on the page
                post_date = soup.find_all("a")[1].text
                
                # collect complete post content
                post_text = soup.find("div", "main-content")
                link_embed = soup.find("a", "link-embed")
                media_link = soup.find_all("a", "media-link")
                album = soup.find("div", "album")
                video = soup.find("div", "video-placeholder")
                visibility = soup.find("div", "visibility")
                activity = soup.find("div", "post-activity")
                comments = soup.find("div", "comments")
                
                if video is not None:
                    tags.append("video")
                
                for link in media_link:
                    # link to image in image folder if not external link
                    if not link["href"].startswith("http"):
                        filename = link["href"]
                        try:
                            link["href"] = os.path.join("..", "images", filename)
                            tags.append("photo")
                        except TypeError:
                            LOGGER.warn("No href attribute to convert link destination ({})".format(link))
                        try:
                            link.img["src"] = os.path.join("..", "images", filename)
                        except TypeError:
                            LOGGER.warn("No src attribute to convert link destination ({})".format(link))
                    # throw away redundant p tag filled with the post text
                    try:
                        link.p.decompose()
                    except AttributeError:
                        pass
                
                # multiple entries only in albums, so we only need first item
                # BeautifulSoup.find_all() always returns result, so media_link
                # is never None
                try:
                    media_link = media_link[0]
                except IndexError:
                    media_link = None
                
                if album is not None:
                    tags.append("photo_album")
                    # we don't need media_link if album is available
                    media_link = None
                
                if link_embed is not None:
                    tags.append("link")
                    # we don't need media_link if we got external link
                    media_link = None
                
                content = ""
                for part in [post_text,
                             link_embed,
                             album,
                             media_link,
                             visibility,
                             activity,
                             comments]:
                    if part is not None:
                        content = "{}\n{}\n".format(content, part)

                # receive link from post date
                link = soup.find_all("a")[1].get("href")
                
                slug = utils.slugify("{}_{}".format(post_date.split()[0], title), lang="de")
                
                if not slug:  # should never happen
                    LOGGER.error("Error converting post:", title)
                    return

                # additional metadata
                more = {"link": link, # original G+ post
                        "hidetitle": True, # doesn't work for index pages
                        }
                                
                self.write_metadata(os.path.join(self.output_folder, self.out_folder, slug + ".meta"), title, slug, post_date, description, tags, more)
                self.write_content(
                    os.path.join(self.output_folder, self.out_folder, slug + ".html"),
                    content)

    def write_metadata(self, filename, title, slug, post_date, description, tags, more):
        super(CommandImportGplus, self).write_metadata(
            filename,
            title,
            slug,
            post_date,
            description,
            tags,
            **more
            )

    def prettify_title(self, t):
        """
            Titles are generated from post text.
            Cut junk and shorten to one line
            for readability and convenience.
        """
        # reduce title string to one line
        t = t.split("<br>")[0]
        # link in title? just cut it out, ain't nobody got time for that
        t = t.split("<a ")[0]
        # same for user link
        t= t.split("span class=")[0]
        # cut trailing dots
        if t.endswith("..."):
            t = t[:-3]
        # cut html elements and fix quotation marks
        for tag in [("<b>", ""),
                     ("</b>", ""),
                     ("&quot;", "\""),
                     ("&#39;", "'"),
                     ("<b", ""),
                     ("</", ""),
                     ("<i>", ""),
                     ("</i>", ""),
                     ("<", ""),]:
            t = t.replace(tag[0], tag[1])
        
        return t
