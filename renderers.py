from jinja2 import Environment


def render_template(template, params=None):
    params = params or {}

    tpl = env.from_string(template)
    return tpl.render(**params)


def to_list(obj):
    if isinstance(obj, dict):
        return ','.join(['%s=%s' % (k, v) for k, v in obj.items()])
    if isinstance(obj, list):
        return ','.join([str(elt) for elt in obj])
    return obj


env = Environment(
    autoescape=False,
)
env.filters['to_list'] = to_list
