import os.path
from jinja2 import Environment, FileSystemLoader
from xml.sax.saxutils import quoteattr

here = os.path.dirname(os.path.abspath(__file__))


def render_from_string(template, params=None):
    params = params or {}

    tpl = env.from_string(template)
    return tpl.render(**params)


def render_from_template(template, params=None):
    params = params or {}

    tpl = env.get_template(template)
    return tpl.render(**params)


def to_list(obj):
    if isinstance(obj, dict):
        return ','.join(['%s=%s' % (k, v) for k, v in obj.items()])
    if isinstance(obj, list):
        return ','.join([str(elt) for elt in obj])
    return obj


def to_attr(obj):
    return quoteattr(obj)

env = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(here, 'templates'))
)
env.filters['to_list'] = to_list
env.filters['to_attr'] = to_attr
