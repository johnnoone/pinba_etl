from textwrap import dedent

__all__ = ['Query']


class Query:

    def __init__(self, name, stmt):
        self.name = name
        self.stmt = dedent(stmt.lstrip('\n').rstrip())

    def __str__(self):
        return self.stmt
