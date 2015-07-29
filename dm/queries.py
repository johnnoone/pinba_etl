from .reports import *
from queries import Query, QUERIES

Query('pinba_global',
      stmt='''
          SELECT server_name,
              1 * req_per_sec rps,
              req_time_total / req_count as tpr,
              req_time_median as mtpr,
              ru_utime_total / req_count as utpr
          FROM report_by_server_name
          WHERE server_name in (
              'www.dailymotion.com',
              'api.dailymotion.com'
          )
      ''')
Query('pinba_status_bot',
      stmt=report5.reports['yes'].query('''
              SELECT status,
                  req_per_sec
              FROM {tablename}
      '''))

Query('pinba_status_nobot',
      stmt=report5.reports['no'].query('''
          SELECT status,
              req_per_sec
          FROM {tablename}
      '''))

Query('pinba_status',
      stmt='''\
    SELECT status,
        SUM(req_per_sec) AS rps
    FROM report_by_hostname_and_status
    WHERE hostname LIKE 'web%'
    GROUP BY status
''')

Query('pinba_output',
      stmt=report6.union("""
    SELECT '{version}' AS format,
        SUM(req_per_sec) AS rps,
        SUM(req_time_total) / SUM(req_count) AS tpr,
        SUM(req_time_median) / SUM(req_count) AS mtpr,
        SUM(ru_utime_total) / SUM(req_count) AS utpr
    FROM {tablename}
    WHERE server_name IN ('www.dailymotion.com')
    GROUP BY format
"""))

Query('pinba_db_output',
      stmt='''\
    SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 2), '.', -1) AS format,
        SUM(hit_per_sec) AS hit,
        SUM(timer_value) / SUM(req_count) AS tph
    FROM tag_report_group
    WHERE hit_count > 0
      AND script_name LIKE '%.%.%'
      AND `group` = 'db'
    GROUP BY format
''')

Query('pinba_country',
      stmt=report4.union("""
    SELECT '{version}' AS country,
        req_per_sec AS rps,
        req_time_total / req_count AS tpr,
        req_time_median AS mtpr,
        ru_utime_total / req_count AS utpr
    FROM {tablename}
    WHERE server_name IN ('www.dailymotion.com')
"""))

Query('pinba_page_type',
      stmt='''\
    SELECT
        IF(
            REPLACE(script_name, '[PROD]', '') IN ('home','video_list','video_item','cdn_director','embed_player','widget_dispatch_v3','widget_dispatch_v1','history_management','video_sequence','autocomplete_list','notfound','video_views_stats','family_filter','user_home','thrift','encoder_next','jukebox_widget','crossdomain','playlist_list','rest_api','register','login','channel_home','user_widget','activity_list','advanced_api','user_list','group_home','oembed','channel_list','hub_item'),
            REPLACE(script_name, '[PROD]', ''),
            'other'
        ) AS page_type,
        SUM(req_per_sec) as rps,
        SUM(req_time_total) / SUM(req_count) AS tpr,
        AVG(req_time_median) AS mtpr,
        SUM(ru_utime_total) / SUM(req_count) AS utpr
    FROM report_by_server_and_script
    WHERE server_name = 'www.dailymotion.com'
    GROUP BY page_type;
''')

Query('pinba_main_page_no_bot',
      stmt=report8.reports['no'].query('''
    SELECT
        SUM(req_per_sec) rps,
        SUM(req_time_total) / SUM(req_count) tpr,
        AVG(req_time_median) AS mtpr,
        SUM(ru_utime_total) / SUM(req_count) AS utpr
    FROM {tablename}
    WHERE server_name = 'www.dailymotion.com'
      AND script_name REGEXP '[PROD*?]([a-z_-]+_list|video_item|home|channel_home|embed_player)'
'''))

Query('pinba_main_page',
      stmt='''\
    SELECT
        SUM(req_per_sec) rps,
        SUM(req_time_total) / SUM(req_count) tpr,
        AVG(req_time_median) AS mtpr,
        SUM(ru_utime_total) / SUM(req_count) utpr
    FROM report_by_server_and_script
    WHERE server_name = 'www.dailymotion.com'
      AND script_name REGEXP '[PROD*?]([a-z_-]+_list|video_item|home|channel_home|embed_player)'
''')

Query('pinba_related',
      stmt='''\
    SELECT
        counter,
        SUM(hit_per_sec) AS hps
    FROM tag_report_counter
    WHERE counter LIKE 'related.%'
      AND script_name NOT LIKE 'bot.%'
    GROUP BY counter
''')

Query('pinba_related2',
      stmt='''\
    SELECT
        CONCAT(counter, '_time') AS tag_value,
        SUM(timer_value) / SUM(hit_count) AS tpr
    FROM tag_report_counter
    WHERE counter in ( 'related.meta2.get', 'related.get' )
      AND script_name NOT LIKE 'bot.%'
    GROUP BY tag_value
''')

# ha ha ha with tag.bot tag.site_content

Query('pinba_related_country',
      stmt='''\
    SELECT
        CONCAT(counter, '-', IF(
            SUBSTRING_INDEX(script_name, '.', 1) IN ('fr', 'us', 'tr', 'de', 'gb', 'jp', 'it', 'ca', 'au', 'ch', 'ru'),
            SUBSTRING_INDEX(script_name, '.', 1),
            'other'
        )) AS countrytag,
        SUM(hit_per_sec) AS hps
    FROM tag_report_counter
    WHERE counter LIKE 'related.page.%' /* '[PROD]related%' */
      AND counter NOT LIKE 'related.%metadata%'
      AND script_name NOT LIKE 'bot.%'
    GROUP BY countrytag
''')

Query('pinba_webapp1',
      stmt='''\
    SELECT
        1 * SUM(req_per_sec) AS req_per_sec,
        SUM(req_time_total) / SUM(req_count) AS tpr
    FROM report_by_server_and_script
    WHERE script_name LIKE '%.ad.%'
      AND server_name='touch.dailymotion.com'
''')

Query('pinba_video_list',
      stmt='''\
    SELECT
        SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 4), '.', -1) AS format,
        SUM(req_time_total) / (
        SELECT
            SUM(req_time_total) AS time
        FROM report_by_server_and_script
        WHERE server_name = 'www.dailymotion.com'
          AND script_name LIKE '%.%.video_list%') * 100 AS percent
    FROM report_by_server_and_script
    WHERE server_name = 'www.dailymotion.com'
      AND script_name LIKE '%.%.video_list%'
    GROUP BY format ORDER BY percent DESC LIMIT 10
''')

Query('pinba_playertab',
      stmt='''\
    SELECT
        concat(counter, '_rps') AS tag_value,
        SUM(req_per_sec) AS rps
    FROM tag_report_counter
    WHERE counter LIKE 'player.tabs.%'
      AND script_name NOT LIKE 'bot.%'
    GROUP BY tag_value
''')

Query('pinba_searchctr',
      stmt='''\
    SELECT
        SUBSTRING_INDEX(counter, '.', -1) AS tag,
        0 + req_per_sec AS rps
    FROM tag_info_counter
    WHERE counter IN ('search.page.click', 'search.page.show')
''')

Query('pinba_es_search',
      stmt='''\
    SELECT
        counter AS tv,
        SUM(hit_per_sec) * (SUM(timer_value) / SUM(hit_count)) AS tps,
        SUM(hit_per_sec) AS hps,
        SUM(timer_value)/SUM(hit_count) AS tpr
    FROM tag_report_counter
    WHERE counter LIKE 'es%.search_time%'
       OR counter LIKE 'search.%'
    GROUP BY counter
''')

Query('pinba_web_perf',
      stmt='''\
    SELECT
        hostname,
        req_per_sec AS rps,
        SUM(req_time_total) / SUM(req_count) AS tpr,
        AVG(req_time_median) AS mtpr
    FROM report_by_hostname_server_and_script
    WHERE server_name = 'www.dailymotion.com'
      AND hostname LIKE 'web-%'
    GROUP BY hostname
''')

Query('pinba_apimethod_country',
      stmt='''\
    SELECT
        SUBSTRING_INDEX(script_name, '.', 1) AS country,
        SUM(req_per_sec)*1 AS rps
    FROM tag_report_group_apimethod
    WHERE `group` = 'api'
      AND script_name NOT LIKE '/data/web%'
    GROUP BY country
''')

Query('pinba_apimethod_object',
      stmt='''\
    SELECT
        SUBSTRING_INDEX(apimethod, '.', 1) AS object,
        SUM(req_per_sec)*1 AS rps
    FROM tag_report_group_apimethod
    WHERE `group` = 'api'
      AND script_name NOT LIKE '/data/web%'
     GROUP BY object
''')

Query('pinba_apimethod_object',
      stmt='''\
    SELECT
        SUBSTRING_INDEX(apimethod, '.', 1) AS object,
        SUM(req_per_sec) * 1 AS rps
    FROM tag_report_group_apimethod
    WHERE `group` = 'api'
      AND script_name NOT LIKE '/data/web%'
     GROUP BY object
''')

Query('pinba_apimethod_method',
      stmt='''\
    SELECT
        apimethod,
        SUM(req_per_sec) AS rps,
        SUM(timer_value) / SUM(req_count) AS tpr
    FROM tag_report_group_apimethod
    WHERE `group` = 'api'
      AND script_name NOT LIKE '/data/web%'
    GROUP BY apimethod
''')

Query('pinba_apimethod_type',
      stmt='''\
    SELECT
        SUM(req_per_sec) AS rps,
        SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 2), '.', -1) AS type
    FROM tag_report_group_apimethod
    WHERE `group` = 'api'
      AND script_name NOT LIKE '/data/web%'
    GROUP BY type
''')

Query('pinba_memcache',
      stmt='''\
    SELECT
        SUBSTR(counter FROM INSTR(counter, '.') + 1) AS clef,
        1.0 * req_per_sec AS rps,
        timer_value / req_count AS tpr
    FROM tag_info_counter
    WHERE counter LIKE 'memcache.%'
''')

Query('pinba_playlist',
      stmt='''\
    SELECT
        SUM(req_time_total) / SUM(req_count) AS average_time
    FROM report_by_script_name
    WHERE script_name LIKE '%.html.playlist_list%'
    ORDER BY script_name
''')

Query('oauth_backend',
      stmt='''\
    SELECT
        concat(`group`, '.', method) AS backend,
        SUM(req_count),
        SUM(hit_count),
        SUM(timer_value) / SUM(hit_count) AS time_per_hit
    FROM tag_report_group_method
    WHERE (script_name LIKE '%oauth_token%'
            OR script_name LIKE '%oauth_authorize%')
      AND `group` != 'localcache'
    GROUP BY backend
''')

Query('oauth_token_activity',
      stmt='''\
    SELECT
        'oauth',
        SUM(req_count) AS req_count,
        SUM(req_per_sec) AS req_per_sec,
        SUM(req_time_median) / COUNT(1) AS time_median
    FROM report_by_script_name
    WHERE script_name LIKE '%oauth_token%'
''')

Query('oauth_authorize_activity',
      stmt='''\
    SELECT
        'oauth',
        SUM(req_count) AS req_count,
        SUM(req_per_sec) AS req_per_sec,
        SUM(req_time_median) / count(1) AS time_median
    FROM report_by_script_name
    WHERE script_name LIKE '%oauth_authorize%'
''')

Query('pinba_facebook_api_calls',
      stmt='''\
    SELECT
        'facebook',
        SUM(hit_count) AS total_hit,
        SUM(timer_value) / SUM(hit_count) AS response_time
    FROM tag_report_group_method
    WHERE `group` = 'facebook'
''')

Query('pinba_googleplus_api_calls',
      stmt='''\
    SELECT
        'googleplus',
        SUM(hit_count) AS total_hit,
        SUM(timer_value) / SUM(hit_count) AS response_time
    FROM tag_report_group_method
    WHERE `group` = 'google_plus'
''')

Query('pinba_cleeng_api_calls',
      stmt='''\
    SELECT
        'cleeng',
        SUM(hit_count) AS total_hit,
        SUM(timer_value) / SUM(hit_count) AS response_time,
        SUM(hit_count) / SUM(req_count) AS hit_per_req
    FROM tag_report_group_method
    WHERE `group` = 'cleeng'
''')

Query('pinba_mandrill',
      stmt='''\
    SELECT
        'mandrill',
        SUM(hit_count) AS total_hit,
        SUM(timer_value) / SUM(hit_count) AS response_time
    FROM tag_report_group_method
    WHERE `group` = 'mandrill'
''')

Query('pinba_akismet',
      stmt='''\
         SELECT
             'akismet',
             SUM(hit_count) AS total_hit,
             SUM(timer_value) / SUM(hit_count) AS response_time
         FROM tag_report_group_method
         WHERE `group` = 'akismet'
     ''')

Query('pinba_spam',
      stmt='''\
          SELECT
              counter,
              SUM(hit_per_sec) as hps
          FROM tag_report_counter
          WHERE counter LIKE 'spam.%'
          GROUP BY counter
      ''')

Query('pinba_advertising',
      stmt='''\
          SELECT
              'advertising',
              SUM(req_count) AS total_req,
              SUM(hit_count) AS total_hit,
              SUM(timer_value) / SUM(hit_count) AS time_per_hit
          FROM tag_report_group_apimethod
          WHERE apimethod = 'video.advertising'
      ''')
