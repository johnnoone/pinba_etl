Pinba ETL
=========

This tools aims to simplify Pinba_ maintenance.
It allows to generate pinba reports, control queries and CollectD_ items.

Installation
------------

::

  pip install pinba_etl


Usage
-----

Create a definitions file '~/pinba-ref.yml' and write some data in it::

    reports:
      - id: myreport
        type: report8
        tablename: >
          {v1}_{v2}_report_by_status
        tags:
          bot: [foo, bar]
        cardinality: bot
    collectd:
      - name: only_foo
        stmt: |
          SELECT status,
              req_per_sec
          FROM {tablename}
        provider: myreport:foo
        gauges:
          - prefix: myprefix1
            instances_from: status
            values_from: req_per_sec
      - name: everyone
        stmt: |
          SELECT status,
              req_per_sec
          FROM {tablename}
        provider: myreport:union
        gauges:
          - name: myprefix2
            cardinality: status
            values: req_per_sec


Now generate report creating queries::

    $ python -m pinba_etl reports

It will create these queries::

    -- bot_foo_report_by_status

    DROP TABLE IF EXISTS `bot_foo_report_by_status`;
    CREATE TABLE `bot_foo_report_by_status` (
      `req_count` int(11) DEFAULT NULL,
      `req_per_sec` float DEFAULT NULL,
      `req_time_total` float DEFAULT NULL,
      `req_time_percent` float DEFAULT NULL,
      `req_time_per_sec` float DEFAULT NULL,
      `ru_utime_total` float DEFAULT NULL,
      `ru_utime_percent` float DEFAULT NULL,
      `ru_utime_per_sec` float DEFAULT NULL,
      `ru_stime_total` float DEFAULT NULL,
      `ru_stime_percent` float DEFAULT NULL,
      `ru_stime_per_sec` float DEFAULT NULL,
      `traffic_total` float DEFAULT NULL,
      `traffic_percent` float DEFAULT NULL,
      `traffic_per_sec` float DEFAULT NULL,
      `status` int(11) DEFAULT NULL,
      `memory_footprint_total` float DEFAULT NULL,
      `memory_footprint_percent` float DEFAULT NULL,
      `req_time_median` float DEFAULT NULL,
      `index_value` varchar(256) DEFAULT NULL
    ) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report8::tag.bot=foo:';

    -- bot_bar_report_by_status

    DROP TABLE IF EXISTS `bot_bar_report_by_status`;
    CREATE TABLE `bot_bar_report_by_status` (
      `req_count` int(11) DEFAULT NULL,
      `req_per_sec` float DEFAULT NULL,
      `req_time_total` float DEFAULT NULL,
      `req_time_percent` float DEFAULT NULL,
      `req_time_per_sec` float DEFAULT NULL,
      `ru_utime_total` float DEFAULT NULL,
      `ru_utime_percent` float DEFAULT NULL,
      `ru_utime_per_sec` float DEFAULT NULL,
      `ru_stime_total` float DEFAULT NULL,
      `ru_stime_percent` float DEFAULT NULL,
      `ru_stime_per_sec` float DEFAULT NULL,
      `traffic_total` float DEFAULT NULL,
      `traffic_percent` float DEFAULT NULL,
      `traffic_per_sec` float DEFAULT NULL,
      `status` int(11) DEFAULT NULL,
      `memory_footprint_total` float DEFAULT NULL,
      `memory_footprint_percent` float DEFAULT NULL,
      `req_time_median` float DEFAULT NULL,
      `index_value` varchar(256) DEFAULT NULL
    ) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report8::tag.bot=bar:';

Now generate control queries::

    $ python -m pinba_etl queries

It will generate::

    -- only_foo

    SELECT status,
        req_per_sec
    FROM bot_foo_report_by_status;

    -- everyone

    (SELECT status,
        req_per_sec
    FROM bot_bar_report_by_status)
    UNION
    (SELECT status,
        req_per_sec
    FROM bot_foo_report_by_status);


And at least, if you need to convert them to collectd::

    $ python -m pinba_etl collectd

It will generate::

    <Plugin dbi>

        <Query "only_foo">
            Statement "SELECT status, req_per_sec FROM bot_foo_report_by_status"
            <Result>
                Type "gauge"
                InstancePrefix "myprefix1"
                InstancesFROM "status"
                ValuesFrom "req_per_sec"
            </Result>
        </Query>
        <Query "everyone">
            Statement "(SELECT status, req_per_sec FROM bot_foo_report_by_status)
                       UNION
                       (SELECT status, req_per_sec FROM bot_bar_report_by_status)"
            <Result>
                Type "gauge"
                InstancePrefix "myprefix2"
                InstancesFROM "status"
                ValuesFrom "req_per_sec"
            </Result>
        </Query>

        <Database "pinba">
            Driver "mysql"
            DriverOption "host" "localhost"
            DriverOption "username" "root"
            DriverOption "password" ""
            DriverOption "dbname" "pinba"
            SelectDB "pinba"
            Query "only_foo"
            Query "everyone"
        </Database>
    </Plugin>


License
-------

This package is release under the BSD Licence.
Please see LICENSE document for a full description.


Credits
-------

- Pinba_
- CollectD_

.. _Pinba: http://pinba.org
.. _CollectD: https://collectd.org
