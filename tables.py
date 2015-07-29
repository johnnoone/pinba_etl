from bases import Bundle

bundle1 = Bundle(
    name='site_content_{version}_report_by_server_and_script',
    definition="""\
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
    """,
    versions = (
        'fr', 'in', 'jp',
        'kr', 'pk', 'ru',
        'tr', 'tw', 'us',
        'vn',
    )
)

## ---

bundle2 = Bundle(
    name='provider_{version}_report_by_server_and_script',
    definition="""\
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
    """,
    versions=('php', 'hhvm')
)

bundle3 = Bundle(
    name='format_{version}_report_by_server_and_script',
    definition = """\
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
    versions=(
        'atom', 'html', 'iphonerss',
        'json', 'podcast', 'rest',
        'rss', 'sequence', 'swf',
        'thumbnail', 'videowall', 'videozap',
        'widget'
    )
)


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



for table in bundle1.create_table():
    print(table)
