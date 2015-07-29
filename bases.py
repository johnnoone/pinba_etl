from textwrap import dedent


class Bundle:

    def __init__(self, name, definition, versions):
        self.name = name
        self.definition = dedent(definition.rstrip())
        self.versions = versions

    def create_table(self):
        definition = self.definition
        for version in self.versions:
            name = self.name.format(version=version)
            yield definition.format(version=version, name=name)

    @property
    def names(self):
        for version in self.versions:
            yield self.name.format(version=version)

    @property
    def bundle(arg):
        for version in self.versions:
            yield self.name.format(version=version), version
