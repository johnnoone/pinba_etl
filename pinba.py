import textwrap
from bases import Bundle


name_1 = 'site_content_{version}_report_by_server_and_script'
template_1 = """
CREATE TABLE `{name}` (
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
	`server_name` varchar(64) DEFAULT NULL,
	`script_name` varchar(128) DEFAULT NULL,
	`memory_footprint_total` float DEFAULT NULL,
	`memory_footprint_percent` float DEFAULT NULL,
	`req_time_median` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report4::tag.site_content={version}';
"""

versions_1 = (
    'fr', 'in', 'jp',
    'kr', 'pk', 'ru',
    'tr', 'tw', 'us',
    'vn',
)

for version in versions_1:
    name = name_1.format(version=version)
    print(template_1.format(version=version, name=name))



name_2 = 'provider_{version}_report_by_server_and_script'
template_2 = """
CREATE TABLE `{name}` (
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
	`server_name` varchar(64) DEFAULT NULL,
	`script_name` varchar(128) DEFAULT NULL,
	`memory_footprint_total` float DEFAULT NULL,
	`memory_footprint_percent` float DEFAULT NULL,
	`req_time_median` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL,
	`p95` float DEFAULT NULL
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report4::tag.provider={version}:95';
"""

versions_2 = (
    'php', 'hhvm',
)

for version in versions_2:
    name = name_2.format(version=version)
    print(template_2.format(version=version, name=name))


versions_3 = (
    'atom', 'html', 'iphonerss',
    'json', 'podcast', 'rest',
    'rss', 'sequence', 'swf',
    'thumbnail', 'videowall', 'videozap',
    'widget'
)

name_3 = 'format_{version}_report_by_server_and_script'
template_3 = """
CREATE TABLE `{name}` (
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
	`server_name` varchar(64) DEFAULT NULL,
	`script_name` varchar(128) DEFAULT NULL,
	`memory_footprint_total` float DEFAULT NULL,
	`memory_footprint_percent` float DEFAULT NULL,
	`req_time_median` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL,
	`p95` float DEFAULT NULL
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report4::tag.format={version}:95';
"""

for version in versions_3:
    name = name_3.format(version=version)
    print(template_3.format(version=version, name=name))


name_4 = 'site_content_{version}_report_by_server_name'

template_4 = """
CREATE TABLE `{name}` (
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
	`server_name` varchar(64) DEFAULT NULL,
	`memory_footprint_total` float DEFAULT NULL,
	`memory_footprint_percent` float DEFAULT NULL,
	`req_time_median` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report2::tag.site_content={version}';
"""


versions_4 = (
    'fr', 'in', 'jp',
    'kr', 'pk', 'ru',
    'tr', 'tw', 'us',
    'vn',
)

for version in versions_4:
    name = name_4.format(version=version)
    print(template_4.format(version=version, name=name))

# --- report_by_status

name_5 = 'bot_{version}_report_by_status'
template_5 = """
CREATE TABLE `{name}` (
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
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report8::tag.bot={version}:';
"""
versions_5 = ('yes', 'no')

for version in versions_5:
    name = name_5.format(version=version)
    print(template_5.format(version=version, name=name))




versions_6 = (
    'atom', 'html', 'iphonerss',
    'json', 'podcast', 'rest',
    'rss', 'sequence', 'swf',
    'thumbnail', 'videowall', 'videozap',
    'widget'
)

name_6 = 'format_{version}_report_by_server_name'
template_6 = """
CREATE TABLE `{name}` (
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
	`server_name` varchar(64) DEFAULT NULL,
	`memory_footprint_total` float DEFAULT NULL,
	`memory_footprint_percent` float DEFAULT NULL,
	`req_time_median` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='report4::tag.format={version}';
"""

for version in versions_6:
    name = name_6.format(version=version)
    print(template_6.format(version=version, name=name))

# ----

print('-- pinba_global')


# -- pinba_status_bot
print('-- pinba_status_bot')

print("""
SELECT status,
    req_per_sec
FROM bot_yes_report_by_status
""")

# -- pinba_status_bot
print('-- pinba_status_nobot')
print("""
SELECT status,
    req_per_sec
FROM bot_no_report_by_status
""")


print('-- pinba_output')
query = []
for version in versions_6:
    name = name_6.format(version=version)
    part = textwrap.dedent("""\
        SELECT "{version}" AS format,
            req_per_sec AS rps,
            req_time_total / req_count AS tpr,
            req_time_median AS mtpr,
            ru_utime_total / req_count AS utpr
        FROM {name}
        WHERE server_name IN ('www.dailymotion.com')
        """.format(name=name, version=version)).strip()
    query.append(part)
print('\n\nUNION\n\n'.join(query) + ';')

print('-- pinba_country')

query = []
for version in versions_4:
    name = name_4.format(version=version)
    part = textwrap.dedent("""\
        SELECT "{version}" AS country,
            req_per_sec AS rps,
            req_time_total / req_count AS tpr,
            req_time_median AS mtpr,
            ru_utime_total / req_count AS utpr
        FROM {name}
        WHERE server_name IN ('www.dailymotion.com')
        """.format(name=name, version=version)).strip()
    query.append(part)
print('\n\nUNION\n\n'.join(query) + ';')
