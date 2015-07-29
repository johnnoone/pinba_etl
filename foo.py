from reports import REPORTS
from queries import QUERIES
from loaders import load_config, DEFAULT_FILENAME

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.set_defaults(action='full')
    parser.add_argument('--configuration', default=DEFAULT_FILENAME)

    subp = parser.add_subparsers()

    parser_a = subp.add_parser('reports')
    parser_a.set_defaults(action='reports')

    parser_b = subp.add_parser('queries')
    parser_b.set_defaults(action='queries')
    parser_b.add_argument('--name', action='append')

    parser_b = subp.add_parser('xml')
    parser_b.set_defaults(action='xml')
    parser_b.add_argument('--name', action='append')
    args = parser.parse_args()

    load_config(args.configuration)

    if args.action in ('reports', 'full'):
        for report in REPORTS.values():
            print(report)

    if args.action in ('queries', 'full'):
        args.name = getattr(args, 'name', []) or list(QUERIES.keys())
        c = 0
        for k, v in QUERIES.items():
            if k in args.name:
                c = c + 1
                print('\n-- %s\n\n%s;' % (k, v))
        print('\n-- count: %s' % c)

    if args.action in ('available', 'full'):
        print('--\n-- available queries (%i)\n--\n' % len(QUERIES))
        for k in QUERIES.keys():
            if k in args.name:
                print('-- %s' % k)

    if args.action in ('xml', 'full'):
        args.name = getattr(args, 'name', []) or list(QUERIES.keys())
        print('<!-- XML -->')
        for k, v in QUERIES.items():
            if k in args.name:
                print('    <Query "%s">' % k)
                print('        Statement "%s"' % v.xml)
                print('')
