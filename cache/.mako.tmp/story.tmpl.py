# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1541940440.5346038
_enable_loop = True
_template_filename = 'themes/zen/templates/story.tmpl'
_template_uri = 'story.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n')
        if post.description():
            __M_writer('        <meta name="description" itemprop="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        arusahni = _mako_get_namespace(context, 'arusahni')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context)
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        ')
        __M_writer(str(arusahni.html_title()))
        __M_writer('\n        ')
        __M_writer(str(arusahni.html_translations(post)))
        __M_writer('\n    </header>\n    <div itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer('        <section class="comments">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/zen/templates/story.tmpl", "uri": "story.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "54": 2, "55": 3, "56": 4, "57": 5, "62": 19, "67": 37, "73": 7, "84": 7, "85": 8, "86": 8, "87": 9, "88": 10, "89": 10, "90": 10, "91": 12, "92": 12, "93": 12, "94": 13, "95": 13, "96": 14, "97": 14, "98": 15, "99": 15, "100": 16, "101": 17, "102": 17, "103": 17, "109": 21, "123": 21, "124": 24, "125": 24, "126": 25, "127": 25, "128": 28, "129": 28, "130": 30, "131": 31, "132": 32, "133": 32, "134": 33, "135": 33, "136": 36, "142": 136}}
__M_END_METADATA
"""
