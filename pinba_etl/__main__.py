from .loaders import load_config, DEFAULT_FILENAME
from .renderers import render_from_template

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.set_defaults(action='reports')
    parser.add_argument('--configuration', default=DEFAULT_FILENAME)

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
        args.name = getattr(args, 'name', []) or list(loader.REPORTS.keys())
        for name, report in loader.REPORTS.items():
            if name in args.name:
                print('\n-- %s\n' % name)
                print(report)

    if args.action == 'queries':
        args.name = getattr(args, 'name', []) or list(loader.QUERIES.keys())
        for k, v in loader.QUERIES.items():
            if k in args.name:
                print('\n-- %s\n\n%s;' % (k, v))

    if args.action == 'collectd':
        params = {
            'queries': [c for c in loader.COLLECTORS.values() if c.gauges],
            'driver': {
                'host': args.host,
                'username': args.username,
                'password': args.password,
                'dbname': args.dbname,
            }
        }
        response = render_from_template('mysql.conf.j2', params)
        print(response)
