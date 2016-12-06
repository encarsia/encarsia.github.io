# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481059529.15099
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_stylesheets', 'html_navigation_links', 'html_title', 'html_tags', 'html_headstart', 'html_translations', 'html_sourcelink', 'late_load_js', 'html_feedlinks']


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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
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
        lang = context.get('lang', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        title = context.get('title', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        favicons = context.get('favicons', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        description = context.get('description', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 58, "22": 86, "23": 106, "24": 120, "25": 130, "26": 144, "27": 151, "28": 162, "29": 169, "35": 60, "45": 60, "46": 61, "47": 62, "48": 63, "49": 65, "50": 66, "51": 68, "52": 69, "53": 70, "54": 71, "55": 72, "56": 74, "57": 77, "58": 78, "59": 81, "60": 82, "61": 82, "62": 82, "63": 83, "64": 84, "65": 84, "66": 84, "72": 122, "80": 122, "81": 123, "82": 124, "83": 125, "84": 125, "85": 125, "86": 125, "87": 125, "88": 125, "89": 125, "90": 126, "91": 127, "92": 127, "93": 127, "94": 127, "95": 127, "96": 127, "97": 127, "103": 147, "109": 147, "110": 148, "111": 149, "112": 149, "113": 149, "119": 133, "125": 133, "126": 134, "127": 135, "128": 137, "129": 137, "130": 138, "131": 139, "132": 139, "133": 139, "134": 139, "135": 139, "136": 141, "142": 3, "166": 3, "167": 7, "168": 8, "169": 9, "170": 10, "171": 12, "172": 13, "173": 15, "174": 16, "175": 18, "176": 21, "177": 22, "178": 25, "179": 25, "180": 25, "181": 28, "182": 29, "183": 29, "184": 29, "185": 31, "186": 32, "187": 32, "188": 32, "189": 32, "190": 34, "191": 34, "192": 35, "193": 35, "194": 36, "195": 37, "196": 37, "197": 37, "198": 39, "199": 40, "200": 41, "201": 42, "202": 42, "203": 42, "204": 42, "205": 42, "206": 42, "207": 42, "208": 45, "209": 46, "210": 47, "211": 47, "212": 47, "213": 49, "214": 50, "215": 50, "216": 51, "217": 52, "218": 53, "219": 54, "220": 56, "221": 57, "222": 57, "228": 153, "236": 153, "237": 154, "238": 155, "239": 156, "240": 157, "241": 157, "242": 157, "243": 157, "244": 157, "245": 158, "246": 158, "252": 164, "259": 164, "260": 165, "261": 166, "262": 167, "263": 167, "264": 167, "265": 167, "271": 88, "278": 88, "279": 89, "280": 90, "281": 91, "282": 93, "283": 94, "284": 96, "285": 97, "286": 98, "287": 100, "288": 101, "289": 105, "290": 105, "291": 105, "297": 108, "306": 108, "307": 109, "308": 110, "309": 110, "310": 110, "311": 111, "312": 112, "313": 113, "314": 114, "315": 114, "316": 114, "317": 114, "318": 114, "319": 116, "320": 117, "321": 117, "322": 117, "328": 322}, "source_encoding": "utf-8", "uri": "arusahni_helper.tmpl", "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
