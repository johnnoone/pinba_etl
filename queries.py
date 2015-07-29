from collections import OrderedDict
from textwrap import dedent
from xml.sax.saxutils import escape

QUERIES = OrderedDict()

class Query:

    def __init__(self, name, stmt, gauges=None):
        self.name = name
        self.stmt = dedent(stmt.lstrip('\n').rstrip())
        self.gauges = gauges or []
        QUERIES[name] = self

    @property
    def xml(self):
        obj = ' '.join(line.strip().strip() for line in self.stmt.split('\n'))
        return escape(obj.rstrip(';'))

    def __str__(self):
        return self.stmt
