from collections import OrderedDict
from textwrap import dedent

QUERIES = OrderedDict()


class Query:

    def __init__(self, name, stmt):
        self.name = name
        self.stmt = dedent(stmt.lstrip('\n').rstrip())
        QUERIES[name] = self

    def __str__(self):
        return self.stmt
