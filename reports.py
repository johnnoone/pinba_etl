import os.path
from collections import OrderedDict
from textwrap import dedent
from renderers import render_template
here = os.path.dirname(os.path.realpath(__file__))

REPORT_TYPES = OrderedDict()
REPORTS = OrderedDict()


class ReportTypeBase:

    def __init__(self, name, description, template):
        self.name = name
        self.description = description
        self.template = template
        REPORT_TYPES[name] = self

    def generate(self, tablename, conditions, percentiles, timers):
        def to_list(obj):
            if isinstance(obj, dict):
                return ','.join(['%s=%s' % (k, v) for k, v in obj.items()])
            if isinstance(obj, list):
                return ','.join([str(elt) for elt in obj])
            return obj

        return render_template(self.template, {
            'tablename': tablename,
            'conditions': conditions,
            'percentiles': percentiles,
            'timers': timers
        })


class ReportType(ReportTypeBase):

    def __init__(self, name, description):
        with open(os.path.join(here, 'templates', '%s.tpl' % name)) as file:
            template = file.read()
        super().__init__(name=name, description=description, template=template)


ReportType('info', "overall info report")
ReportType('report1', "report aggregated by script name")
ReportType('report2', "report aggregated by domain name")
ReportType('report3', "report aggregated by hostname")
ReportType('report4', "report aggregated by domain name and script name")
ReportType('report5', "report aggregated by hostname and script name")
ReportType('report6', "report aggregated by hostname and domain name")
ReportType('report7', "report aggregated by hostname, domain name and script name")
ReportType('report8', "report aggregated by HTTP status")
ReportType('report9', "report aggregated by script name and HTTP status")
ReportType('report10', "report aggregated by domain name and HTTP status")
ReportType('report11', "report aggregated by hostname and HTTP status")
ReportType('report12', "report aggregated by hostname, script name and HTTP status")
ReportType('report13', "report aggregated by schema")
ReportType('report14', "report aggregated by schema and script name")
ReportType('report15', "report aggregated by schema and domain name")
ReportType('report16', "report aggregated by schema and hostname")
ReportType('report17', "report aggregated by schema, hostname and script name")
ReportType('report18', "report aggregated by schema, hostname and HTTP status")
ReportType('tag_report', "tag report aggregated by script name and tag value")
ReportType('tag_report2', "tag report aggregated by script name, domain name, hostname and tag value")
ReportType('tag2_report', "tag report aggregated by script name and values of 2 tags")
ReportType('tag2_report2', "tag report aggregated by script name, domain name, hostname and values of 2 tags")
ReportType('tagN_report', "tag report aggregated by script name and values of N tags")
ReportType('tagN_report2', "tag report aggregated by script name, domain name, hostname and values of N tags")
ReportType('tag_info', "tag report aggregated by tag value")
ReportType('tag2_info', "tag report aggregated by values of 2 tags")
ReportType('tagN_info', "tag report aggregated by values of N tags")
ReportType('histogram', "histogram data for a report")


class Report:

    def __init__(self, type, tablename, *, min_time=None, max_time=None, tags=None, percentiles=None, timers=None):
        self.type = type
        self.tablename = tablename
        self.min_time = min_time
        self.max_time = max_time
        self.tags = tags or {}
        self.percentiles = percentiles or []
        self.timers = timers or []
        REPORTS[tablename] = self

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

    def __init__(self, type, tablename, version, **kwargs):
        raw = kwargs.pop('tags', {})
        tags, values = [], []
        for k, v in flatten_tags(raw):
            if k == version:
                values.append(v)
            else:
                tags.append((k, v))

        reports = {}
        tablenames = []
        for value in values:
            t_name = tablename.format(v1=version, v2=value)
            t_tags = tags + [(version, value)]
            reports[value] = Report(
                type=type,
                tablename=t_name,
                tags=t_tags,
                **kwargs
            )
            tablenames.append(t_name)
        self.version = version
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
        return '\nUNION\n'.join(queries) + ';'

    def __str__(self):
        return '\n'.join(self.create_tables())


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
