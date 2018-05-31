This plugin does a rough import of a Google+ stream as provided by [Google Takeout](http://google.com/takeout/)

Videos work, content in general works, attached images may or may not work depending on source.

The output is html, and there's little to no configuration done in the resulting site.

**Edit**

As of today (May 2018) this mostly rewritten plugin works until Google plays around again.

*Notes:*

 * Download Google Takeout as zip file if you use umlauts. There may be encoding issues.
 * Extract the dump file, merge parts if you have multiple files.
 * Additional Python package requirement: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).
 * Open `plugins/import_gplus.py` and adapt folder names to your language settings.
 * Run `nikola import_gplus takeout_folder`.
 * The plugin inits a new Nikola site called `new_site` (no shit, Sherlock), you will have to change into that directory to run build commands.
 * Building the site can take long and possibly wake up your fans. You may want to test the output with a fraction of the available data.
 * Although the output should work with any theme, it looks quite nice with [hyde](https://themes.getnikola.com/v7/hyde/); hpstr is okay, too. Consider to copy the included `custom.css` into the `themes/THEME_NAME/assets/css` directory for an even better experience.
 * Tweaking `conf.py`
  * disable comments:  `COMMENT_SYSTEM = ""`
  * link to your G+ profile in `NAVIGATION_LINKS`, disable link to RSS feed
  
***IMPORTANT***

If you consider to release this into the wilderness, keep in mind that the import includes not only public but also private and community shares.

Enjoy.