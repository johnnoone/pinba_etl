import os.path
import pytest
from pinba_etl import Loader, load_config, Gauge, Query
from textwrap import dedent

gauges_data = [
    ({'name': 'foo',
      'cardinality': 'bar',
      'values': 'baz'},
     {'name': 'foo',
      'cardinality': 'bar',
      'values': 'baz'}),
    ('foo-{bar} {baz}',
     {'name': 'foo',
      'cardinality': 'bar',
      'values': 'baz'})
]

here = os.path.abspath(os.path.dirname(__file__))


@pytest.mark.parametrize('src, expected', gauges_data)
def test_gauge(src, expected):
    loader = Loader()
    provider, loaded = loader.parse_gauge(src, '-')
    assert loaded == expected


def test_config():
    loaded = load_config(os.path.join(here, 'config1.yml'))
    assert loaded.QUERIES['only_foo'].stmt == Query('-', """\
        SELECT status,
            req_per_sec
        FROM bot_foo_report_by_status
    """).stmt

    assert loaded.GAUGES['everyone'][0].cardinality == 'status'

    query = loaded.REPORTS['myreport'].union('SELECT * FROM {tablename}')
    assert set(query.split('\nUNION\n')) == {
        '(SELECT * FROM bot_foo_report_by_status)',
        '(SELECT * FROM bot_bar_report_by_status)'
    }
