import fnmatch
import re
from .loaders import load_config, DEFAULT_FILENAME
from .renderers import render_from_template


def compile_patterns(names):
    if not names:
        return re.compile('.*')
    elif len(names) == 1:
        return re.compile(fnmatch.translate(names[0]))
    else:
        patterns = [fnmatch.translate(n).lstrip('^').rstrip('$') for n in names]
    return re.compile('^(' + '|'.join(patterns) + ')$')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.set_defaults(action='reports', name=[])
    parser.add_argument('--configuration', default=DEFAULT_FILENAME)
    parser.add_argument('--name', action='append', help='filter by name')

    subp = parser.add_subparsers()

    parser_a = subp.add_parser('reports', help='generate sql reports tables')
    parser_a.set_defaults(action='reports')
    parser_a.add_argument('--name', action='append', help='filter by name')

    parser_b = subp.add_parser('queries', help='generate sql queries')
    parser_b.set_defaults(action='queries')
    parser_b.add_argument('--name', action='append', help='filter by name')

    parser_b = subp.add_parser('collectd', help='generate xml for collectd')
    parser_b.set_defaults(action='collectd')
    parser_b.add_argument('--name', action='append', help='filter by name')

    group = parser_b.add_argument_group('pinba credentials')
    group.add_argument('--host', default='localhost')
    group.add_argument('--username', default='root')
    group.add_argument('--password', default='')
    group.add_argument('--dbname', default='pinba')

    args = parser.parse_args()

    loader = load_config(args.configuration)

    if args.action == 'reports':
        pattern = compile_patterns(args.name)
        args.name = getattr(args, 'name', []) or ['*']
        for name, report in loader.REPORTS.items():
            if pattern.match(name):
                print('\n-- %s\n' % name)
                print(report)

    if args.action == 'queries':
        pattern = compile_patterns(args.name)
        args.name = getattr(args, 'name', []) or ['*']
        for name, query in loader.QUERIES.items():
            if pattern.match(name):
                print('\n-- %s\n\n%s;' % (name, query))

    if args.action == 'collectd':
        pattern = compile_patterns(args.name)
        args.name = getattr(args, 'name', []) or ['*']

        collectors = []
        for name, collector in loader.COLLECTORS.items():
            if collector.gauges and pattern.match(collector.name):
                collectors.append(collector)
        params = {
            'queries': collectors,
            'driver': {
                'host': args.host,
                'username': args.username,
                'password': args.password,
                'dbname': args.dbname,
            }
        }
        response = render_from_template('mysql.conf.j2', params)
        print(response)
