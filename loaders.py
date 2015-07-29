import os.path
import yaml
from reports import CardReport, Report, REPORTS
from queries import Query, QUERIES

LOCAL_REPORTS = {}

DEFAULT_FILENAME = '~/pinba-ref.yml'


def load_config(filename):
    filename = os.path.expanduser(filename)
    with open(filename) as file:
        config = yaml.load(file)

    for report in config.get('reports', []):
        if 'tablename' in report:
            report['tablename'] = report['tablename'].strip()
        if 'percentiles' in report:
            percs = report.pop('percentiles')
            if not isinstance(percs, list):
                percs = [percs]
            report['percentiles'] = [str(p) for p in percs]
        if 'version' in report:
            load_cart_report(report)
        else:
            load_report(report)

    for query in config.get('collectd', []):
        load_query(query)


def load_cart_report(report):
    attrs = 'type tablename version min_time max_time tags percentiles timers'.split()
    opts = {k: v for k, v in report.items() if k in attrs}
    result = CardReport(**opts)
    if 'id' in report:
        if report['id'] == 'report5':
            print(report, result.reports, 'er')
            print(report, result.reports, 'er')
        LOCAL_REPORTS[str(report['id'])] = result
    return result


def load_report(report):
    attrs = 'type tablename min_time max_time tags percentiles timers'.split()
    opts = {k: v for k, v in report.items() if k in attrs}
    result = Report(**opts)
    if 'id' in report:
        LOCAL_REPORTS[str(report['id'])] = result
    return result


def load_query(query):
    if 'provider' in query:
        provider_id = str(query.pop('provider'))
        if ':' in provider_id:
            provider_id, scope = provider_id.split(':', 1)
            provider = LOCAL_REPORTS[str(provider_id)]
            if hasattr(provider, scope):
                stmt = getattr(provider, scope)(query['stmt'])
            elif isinstance(provider, CardReport):
                stmt = provider.reports[scope].query(query['stmt'])
        else:
            provider = LOCAL_REPORTS[provider_id]
            stmt = provider.query(stmt)
        query['stmt'] = stmt
    return Query(**query)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=DEFAULT_FILENAME)
    parser.add_argument('--report', action='append', dest='reports', default=[])
    parser.add_argument('--collectd', action='append', dest='queries', default=[])

    args = parser.parse_args()
    load_config(args.filename)

    whole = (not args.reports) and (not args.queries)
    if whole:
        args.reports = args.reports or REPORTS.keys()
        args.queries = args.queries or QUERIES.keys()

    for name, report in LOCAL_REPORTS.items():
        if name in args.reports:
            print('-- %s' % name)
            print(report)

    for name, query in QUERIES.items():
        if name in args.queries:
            print('-- %s' % name)
            print(query)
