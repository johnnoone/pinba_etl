import os.path
import yaml
from .collectd import Gauge, Collector
from .queries import Query
from .reports import CardReport, Report
from collections import defaultdict, OrderedDict

DEFAULT_FILENAME = '~/pinba-ref.yml'


class Loader:

    def __init__(self):
        self.REPORTS = OrderedDict()
        self.QUERIES = OrderedDict()
        self.GAUGES = defaultdict(list)
        self.COLLECTORS = OrderedDict()

    def load(self, config):

        for report in config.get('reports', []):
            self.load_report(**report)

        for query in config.get('queries', []):
            self.load_query(**query)

        for collector in config.get('collectd', []):
            self.load_collector(**collector)

        for gauge in config.get('gauges', []):
            self.load_gauge(gauge)

        self.finalize()
        return self

    def load_report(self, id, **opts):
        if 'tablename' in opts:
            opts['tablename'] = opts['tablename'].strip()
        if 'percentiles' in opts:
            percs = opts.pop('percentiles')
            if not isinstance(percs, list):
                percs = [percs]
            opts['percentiles'] = [str(p) for p in percs]

        if 'cardinality' in opts:
            attrs = {
                'type', 'tablename', 'min_time', 'max_time',
                'tags', 'percentiles', 'timers', 'cardinality'
            }
            Class = CardReport
        else:
            attrs = {
                'type', 'tablename', 'min_time', 'max_time',
                'tags', 'percentiles', 'timers'
            }
            Class = Report
        opts = {k: v for k, v in opts.items() if k in attrs}
        report = Class(**opts)
        self.REPORTS[str(id)] = report
        return report

    def load_query(self, **opts):
        name = opts['name']
        if 'provider' in opts:
            provider_id = str(opts.pop('provider'))
            if ':' in provider_id:
                provider_id, scope = provider_id.split(':', 1)
                provider = self.REPORTS[str(provider_id)]
                if hasattr(provider, scope):
                    stmt = getattr(provider, scope)(opts['stmt'])
                elif isinstance(provider, CardReport):
                    stmt = provider.reports[scope].query(opts['stmt'])
            else:
                provider = self.REPORTS[provider_id]
                stmt = provider.query(stmt)
            opts['stmt'] = stmt
        attrs = {'name', 'stmt'}
        opts = {k: v for k, v in opts.items() if k in attrs}
        query = Query(**opts)
        self.QUERIES[name] = query
        return query

    def load_collector(self, **opts):
        query = self.load_query(**opts)
        name = opts['name']
        for gauge in opts.get('gauges', []):
            gauge.setdefault('provider', name)
            self.load_gauge(**gauge)
        collector = Collector(name=name, query=query)
        self.COLLECTORS[name] = collector
        return collector

    def load_gauge(self, provider, **opts):
        gauge = Gauge(**opts)
        self.GAUGES[provider].append(gauge)
        return gauge

    def finalize(self):
        for name, gauges in self.GAUGES.items():
            collector = self.COLLECTORS[name]
            for gauge in gauges:
                if gauge not in collector.gauges:
                    collector.gauges.append(gauge)


def load_config(filename):
    filename = os.path.expanduser(filename)
    with open(filename) as file:
        config = yaml.load(file)

    loader = Loader()
    return loader.load(config)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
    parser.add_argument('--report', action='append', dest='reports')
    parser.add_argument('--collectd', action='append', dest='queries')

    args = parser.parse_args()
    loader = load_config(args.filename)

    whole = (not args.reports) and (not args.queries)
    if whole:
        args.reports = args.reports or loader.REPORTS.keys()
        args.queries = args.queries or loader.QUERIES.keys()

    for name, report in loader.REPORTS.items():
        if name in args.reports:
            print('-- %s' % name)
            print(report)

    for name, query in loader.QUERIES.items():
        if name in args.queries:
            print('-- %s' % name)
            print(query)
