import os.path
import yaml
from .renderers import render_from_string
from collections import OrderedDict
from textwrap import dedent

__all__ = ['CardReport', 'Report']

here = os.path.dirname(os.path.realpath(__file__))

REPORT_TYPES = OrderedDict()


class ReportTypeBase:

    def __init__(self, type, description, template):
        self.type = type
        self.description = description
        self.template = template
        REPORT_TYPES[type] = self

    def generate(self, tablename, conditions, percentiles, timers):
        def to_list(obj):
            if isinstance(obj, dict):
                return ','.join(['%s=%s' % (k, v) for k, v in obj.items()])
            if isinstance(obj, list):
                return ','.join([str(elt) for elt in obj])
            return obj

        return render_from_string(self.template, {
            'tablename': tablename,
            'conditions': conditions,
            'percentiles': percentiles,
            'timers': timers
        })


class ReportType(ReportTypeBase):

    def __init__(self, type, description):
        with open(os.path.join(here, 'templates', '%s.sql.j2' % type)) as file:
            template = file.read()
        super().__init__(type=type, description=description, template=template)


class Report:

    def __init__(self, type, tablename, **kwargs):
        self.type = type
        self.tablename = tablename
        self.min_time = kwargs.pop('min_time', None)
        self.max_time = kwargs.pop('max_time', None)
        self.tags = kwargs.pop('tags', {})
        self.percentiles = kwargs.pop('percentiles', [])
        self.timers = kwargs.pop('timers', [])

    @property
    def conditions(self):
        if self.min_time is not None:
            yield 'min_time', '%.3f' % self.min_time
        if self.max_time is not None:
            yield 'max_time', '%.3f' % self.max_time
        for k, v in flatten_tags(self.tags):
            yield 'tag.%s' % k, v

    def create_table(self):
        report_type = REPORT_TYPES[self.type]
        return 'DROP TABLE IF EXISTS `%s`;\n%s' % (
            self.tablename,
            report_type.generate(
                self.tablename,
                OrderedDict(self.conditions),
                self.percentiles,
                self.timers
            ))

    def query(self, template, **opts):
        opts.setdefault('tablename', self.tablename)
        return dedent(template.format(**opts).lstrip('\n').rstrip())

    def __str__(self):
        return self.create_table()


class CardReport:

    def __init__(self, type, tablename, cardinality, **kwargs):
        raw = kwargs.pop('tags', {})
        tags, values = [], []
        for k, v in flatten_tags(raw):
            if k == cardinality:
                values.append(v)
            else:
                tags.append((k, v))

        reports = {}
        tablenames = []
        for value in values:
            t_name = tablename.format(v1=cardinality, v2=value)
            t_tags = tags + [(cardinality, value)]
            reports[value] = Report(
                type=type,
                tablename=t_name,
                tags=t_tags,
                **kwargs
            )
            tablenames.append(t_name)
        self.cardinality = cardinality
        self.versions = values
        self.reports = reports
        self.tablenames = tablenames

    def create_tables(self):
        for report in self.reports.values():
            yield report.create_table()

    def union(self, template):
        queries = []
        for version, report in self.reports.items():
            query = report.query(template, version=version).rstrip(';')
            queries.append('(%s)' % query)
        return '\nUNION\n'.join(queries)

    def __str__(self):
        return '\n\n'.join(self.create_tables())


def flatten_tags(obj):
    if not obj:
        raise StopIteration
    if isinstance(obj, dict):
        obj = obj.items()
    for k, v in obj:
        if isinstance(v, (list, set, tuple)):
            for w in v:
                yield k, w
        else:
            yield k, v

with open(os.path.join(here, 'reports.yml')) as file:
    data = yaml.load(file)
    for report in data['reports']:
        ReportType(**report)
