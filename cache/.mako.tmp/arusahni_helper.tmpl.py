# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1480344632.769038
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_sourcelink', 'html_tags', 'html_feedlinks', 'html_stylesheets', 'html_navigation_links', 'html_translations', 'late_load_js', 'html_title']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_feedlinks():
            return render_html_feedlinks(context)
        description = context.get('description', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        permalink = context.get('permalink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <div itemprop="keywords" class="tags">\n        <ul>\n        ')
            __M_writer(str(messages("Tags")))
            __M_writer('&nbsp;:&nbsp;\n')
            for tag in post.tags:
                __M_writer('           <li><a class="tag p-category" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('" rel="tag">')
                __M_writer(str(tag))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        post = context.get('post', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href=\'//fonts.googleapis.com/css?family=Bitter:400,400italic,700\' rel=\'stylesheet\' type=\'text/css\'>\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer("            <link href='//fonts.googleapis.com/css?family=Bitter:400,400italic,700' rel='stylesheet' type='text/css'>\n")
            else:
                __M_writer('            <link href="/assets/css/bitter.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rel_link = context.get('rel_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text, icon in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 58, "22": 86, "23": 106, "24": 120, "25": 130, "26": 144, "27": 151, "28": 162, "29": 169, "35": 3, "59": 3, "60": 7, "61": 8, "62": 9, "63": 10, "64": 12, "65": 13, "66": 15, "67": 16, "68": 18, "69": 21, "70": 22, "71": 25, "72": 25, "73": 25, "74": 28, "75": 29, "76": 29, "77": 29, "78": 31, "79": 32, "80": 32, "81": 32, "82": 32, "83": 34, "84": 34, "85": 35, "86": 35, "87": 36, "88": 37, "89": 37, "90": 37, "91": 39, "92": 40, "93": 41, "94": 42, "95": 42, "96": 42, "97": 42, "98": 42, "99": 42, "100": 42, "101": 45, "102": 46, "103": 47, "104": 47, "105": 47, "106": 49, "107": 50, "108": 50, "109": 51, "110": 52, "111": 53, "112": 54, "113": 56, "114": 57, "115": 57, "121": 164, "128": 164, "129": 165, "130": 166, "131": 167, "132": 167, "133": 167, "134": 167, "140": 133, "146": 133, "147": 134, "148": 135, "149": 137, "150": 137, "151": 138, "152": 139, "153": 139, "154": 139, "155": 139, "156": 139, "157": 141, "163": 108, "172": 108, "173": 109, "174": 110, "175": 110, "176": 110, "177": 111, "178": 112, "179": 113, "180": 114, "181": 114, "182": 114, "183": 114, "184": 114, "185": 116, "186": 117, "187": 117, "188": 117, "194": 60, "204": 60, "205": 61, "206": 62, "207": 63, "208": 65, "209": 66, "210": 68, "211": 69, "212": 70, "213": 71, "214": 72, "215": 74, "216": 77, "217": 78, "218": 81, "219": 82, "220": 82, "221": 82, "222": 83, "223": 84, "224": 84, "225": 84, "231": 122, "239": 122, "240": 123, "241": 124, "242": 125, "243": 125, "244": 125, "245": 125, "246": 125, "247": 125, "248": 125, "249": 126, "250": 127, "251": 127, "252": 127, "253": 127, "254": 127, "255": 127, "256": 127, "262": 153, "270": 153, "271": 154, "272": 155, "273": 156, "274": 157, "275": 157, "276": 157, "277": 157, "278": 157, "279": 158, "280": 158, "286": 88, "293": 88, "294": 89, "295": 90, "296": 91, "297": 93, "298": 94, "299": 96, "300": 97, "301": 98, "302": 100, "303": 101, "304": 105, "305": 105, "306": 105, "312": 147, "318": 147, "319": 148, "320": 149, "321": 149, "322": 149, "328": 322}, "uri": "arusahni_helper.tmpl", "source_encoding": "utf-8", "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
