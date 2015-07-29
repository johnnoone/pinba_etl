CREATE TABLE `{{ tablename }}` (
{%- for timer in timers %}
	`{{ timer }}` varchar(64) DEFAULT NULL,
{%- endfor %}
	`req_count` int(11) DEFAULT NULL,
	`req_per_sec` float DEFAULT NULL,
	`hit_count` int(11) DEFAULT NULL,
	`hit_per_sec` float DEFAULT NULL,
	`timer_value` float DEFAULT NULL,
	`timer_median` float DEFAULT NULL,
	`ru_utime_value` float DEFAULT NULL,
	`ru_stime_value` float DEFAULT NULL,
	`index_value` varchar(256) DEFAULT NULL
	{%- for perc in percentiles -%}
	,
	`p{{ perc}}` float DEFAULT NULL
	{%- endfor %}
) ENGINE=PINBA DEFAULT CHARSET=latin1 COMMENT='tag2_info:{{ timers | to_list }}:{{ conditions | to_list }}:{{ percentiles | to_list }}'
