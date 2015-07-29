<Plugin dbi>

    <Query "pinba_global">
        Statement "{pinba_global.xml}"
        <Result>
            Type "gauge"
            InstancePrefix "rps"
            InstancesFROM "server_name"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "tpr"
            InstancesFROM "server_name"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "mtpr"
            InstancesFROM "server_name"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "utpr"
            InstancesFROM "server_name"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_status_bot">
        Statement {pinba_status_bot.xml}"
        <Result>
            Type "gauge"
            InstancePrefix "status_bot"
            InstancesFROM "status"
            ValuesFrom "req_per_sec"
        </Result>
    </Query>

    <Query "pinba_status_nobot">
        Statement "SELECT status, req_per_sec FROM bot_no_report_by_status"
        <Result>
            Type "gauge"
            InstancePrefix "status_nobot"
            InstancesFROM "status"
            ValuesFrom "req_per_sec"
        </Result>
    </Query>

    <Query "pinba_status">
        Statement "SELECT status, SUM(req_per_sec) AS rps FROM report_by_hostname_and_status WHERE hostname LIKE 'web%' GROUP BY status"
        <Result>
            Type "gauge"
            InstancePrefix "status"
            InstancesFROM "status"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_output">
        Statement "(SELECT 'iphonerss' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_iphonerss_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'json' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_json_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'thumbnail' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_thumbnail_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'html' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_html_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'rest' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_rest_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'sequence' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_sequence_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'widget' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_widget_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'videowall' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_videowall_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'videozap' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_videozap_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'swf' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_swf_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'atom' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_atom_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'rss' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_rss_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format) UNION (SELECT 'podcast' AS format, SUM(req_per_sec) AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, SUM(req_time_median) / SUM(req_count) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM format_podcast_report_by_server_name WHERE server_name IN ('www.dailymotion.com') GROUP BY format)"
        <Result>
            Type "gauge"
            InstancePrefix "outputformat_rps"
            InstancesFROM "format"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "outputformat_tpr"
            InstancesFROM "format"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "outputformat_mtpr"
            InstancesFROM "format"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "outputformat_utpr"
            InstancesFROM "format"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_db_output">
        Statement "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 2), '.', -1) AS format, SUM(hit_per_sec) AS hit, SUM(timer_value) / SUM(req_count) AS tph FROM tag_report_group WHERE hit_count > 0 AND script_name LIKE '%.%.%' AND `group` = 'db' GROUP BY format"
        <Result>
            Type "gauge"
            InstancePrefix "outputdbformat_hit"
            InstancesFROM "format"
            ValuesFrom "hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "outputdbformat_tph"
            InstancesFROM "format"
            ValuesFrom "tph"
        </Result>
    </Query>

    <Query "pinba_country">
        Statement "(SELECT 'us' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_us_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'vn' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_vn_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'fr' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_fr_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'jp' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_jp_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'in' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_in_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'tr' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_tr_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'ru' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_ru_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'kr' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_kr_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'pk' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_pk_report_by_server_name WHERE server_name IN ('www.dailymotion.com')) UNION (SELECT 'tw' AS country, req_per_sec AS rps, req_time_total / req_count AS tpr, req_time_median AS mtpr, ru_utime_total / req_count AS utpr FROM site_content_tw_report_by_server_name WHERE server_name IN ('www.dailymotion.com'))"
        <Result>
            Type "gauge"
            InstancePrefix "country_rps"
            InstancesFROM "country"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "country_tpr"
            InstancesFROM "country"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "country_mtpr"
            InstancesFROM "country"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "country_utpr"
            InstancesFROM "country"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_page_type">
        Statement "SELECT IF( SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 3), '.', -1) IN ('home','video_list','video_item','cdn_director','embed_player','widget_dispatch_v3','widget_dispatch_v1','history_management','video_sequence','autocomplete_list','notfound','video_views_stats','family_filter','user_home','thrift','encoder_next','jukebox_widget','crossdomain','playlist_list','rest_api','register','login','channel_home','user_widget','activity_list','advanced_api','user_list','group_home','oembed','channel_list','hub_item'), SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 3), '.', -1), 'other' ) AS page_type, SUM(req_per_sec) as rps, SUM(req_time_total) / SUM(req_count) AS tpr, AVG(req_time_median) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM report_by_server_and_script WHERE server_name = 'www.dailymotion.com' AND (SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 3), '.', -1) IN ('video_list','video_item','playlist_list','activity_list','user_list','channel_list','hub_item') AND script_name like '%.html.%' OR SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 3), '.', -1) NOT IN ('video_list','video_item','playlist_list','activity_list','user_list','channel_list','hub_item')) AND SUBSTRING_INDEX(script_name, '.', 1) != 'bot' GROUP BY page_type"
        <Result>
            Type "gauge"
            InstancePrefix "page_type_rps"
            InstancesFROM "page_type"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "page_type_tpr"
            InstancesFROM "page_type"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "page_type_mtpr"
            InstancesFROM "page_type"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "page_type_utpr"
            InstancesFROM "page_type"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_main_page_no_bot">
        Statement "SELECT SUM(req_per_sec) rps, SUM(req_time_total) / SUM(req_count) tpr, AVG(req_time_median) AS mtpr, SUM(ru_utime_total) / SUM(req_count) AS utpr FROM report_by_server_and_script WHERE server_name = 'www.dailymotion.com' AND script_name REGEXP '\.html\.([a-z_-]+_list|video_item|home|channel_home)|\.swf\.embed_player' AND NOT script_name REGEXP '^bot\.'"
        <Result>
            Type "gauge"
            InstancePrefix "main_page_no_bot_rps"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_no_bot_tpr"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_no_bot_mtpr"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_no_bot_utpr"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_main_page">
        Statement "SELECT SUM(req_per_sec) rps, SUM(req_time_total) / SUM(req_count) tpr, AVG(req_time_median) AS mtpr, SUM(ru_utime_total) / SUM(req_count) utpr FROM report_by_server_and_script WHERE server_name = 'www.dailymotion.com' AND script_name REGEXP '\.html\.([a-z_-]+_list|video_item|home|channel_home)|\.swf\.embed_player'"
        <Result>
            Type "gauge"
            InstancePrefix "main_page_rps"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_tpr"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_mtpr"
            ValuesFrom "mtpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "main_page_utpr"
            ValuesFrom "utpr"
        </Result>
    </Query>

    <Query "pinba_related">
        Statement "SELECT counter, SUM(hit_per_sec) AS hps FROM tag_report_counter WHERE counter LIKE 'related.%' AND script_name NOT LIKE 'bot.%' GROUP BY counter"
        <Result>
            Type "gauge"
            InstancesFROM "tag_value"
            ValuesFrom "hps"
        </Result>
    </Query>

    <Query "pinba_related2">
        Statement "SELECT CONCAT(counter, '_time') AS tag_value, SUM(timer_value) / SUM(hit_count) AS tpr FROM tag_report_counter WHERE counter in ( 'related.meta2.get', 'related.get' ) AND script_name NOT LIKE 'bot.%' GROUP BY tag_value"
        <Result>
            Type "gauge"
            InstancesFROM "tag_value"
            ValuesFrom "tpr"
        </Result>
    </Query>

    <Query "pinba_related_country">
        Statement "SELECT CONCAT(counter, '-', IF( SUBSTRING_INDEX(script_name, '.', 1) IN ('fr', 'us', 'tr', 'de', 'gb', 'jp', 'it', 'ca', 'au', 'ch', 'ru'), SUBSTRING_INDEX(script_name, '.', 1), 'other' )) AS countrytag, SUM(hit_per_sec) AS hps FROM tag_report_counter WHERE counter LIKE 'related.page.%' AND counter NOT LIKE 'related.%metadata%' AND script_name NOT LIKE 'bot.%' GROUP BY countrytag"
        <Result>
            Type "gauge"
            InstancesFROM "countrytag"
            ValuesFrom "hps"
        </Result>
    </Query>

    <Query "pinba_webapp1">
        Statement "SELECT 1 * SUM(req_per_sec) AS req_per_sec, SUM(req_time_total) / SUM(req_count) AS tpr FROM report_by_server_and_script WHERE script_name LIKE '%.ad.%' AND server_name='touch.dailymotion.com'"
        <Result>
            Type "gauge"
            InstancePrefix "webapp.ad.call_rps"
            ValuesFrom "req_per_sec"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "webapp.ad.call_tpr"
            ValuesFrom "tpr"
        </Result>
    </Query>

    <Query "pinba_video_list">
        Statement "SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 4), '.', -1) AS format, SUM(req_time_total) / ( SELECT SUM(req_time_total) AS time FROM report_by_server_and_script WHERE server_name = 'www.dailymotion.com' AND script_name LIKE '%.%.video_list%') * 100 AS percent FROM report_by_server_and_script WHERE server_name = 'www.dailymotion.com' AND script_name LIKE '%.%.video_list%' GROUP BY format ORDER BY percent DESC LIMIT 10"
        <Result>
            Type "gauge"
            InstancePrefix "video_list_contrib"
            InstancesFROM "format"
            ValuesFrom "percent"
        </Result>
    </Query>

    <Query "pinba_playertab">
        Statement "SELECT concat(counter, '_rps') AS tag_value, SUM(req_per_sec) AS rps FROM tag_report_counter WHERE counter LIKE 'player.tabs.%' AND script_name NOT LIKE 'bot.%' GROUP BY tag_value"
        <Result>
            Type "gauge"
            InstancesFROM "tag_value"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_searchctr">
        Statement "SELECT SUBSTRING_INDEX(counter, '.', -1) AS tag, 0 + req_per_sec AS rps FROM tag_info_counter WHERE counter IN ('search.page.click', 'search.page.show')"
        <Result>
            Type "gauge"
            InstancePrefix "search_ctr"
            InstancesFROM "tag"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_es_search">
        Statement "SELECT counter AS tv, SUM(hit_per_sec) * (SUM(timer_value) / SUM(hit_count)) AS tps, SUM(hit_per_sec) AS hps, SUM(timer_value)/SUM(hit_count) AS tpr FROM tag_report_counter WHERE counter LIKE 'es%.search_time%' OR counter LIKE 'search.%' GROUP BY counter"
        <Result>
            Type "gauge"
            InstancePrefix "hps"
            InstancesFROM "tv"
            ValuesFrom "hps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "tpr"
            InstancesFROM "tv"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "tps"
            InstancesFROM "tv"
            ValuesFrom "tps"
        </Result>
    </Query>

    <Query "pinba_web_perf">
        Statement "SELECT hostname, req_per_sec AS rps, SUM(req_time_total) / SUM(req_count) AS tpr, AVG(req_time_median) AS mtpr FROM report_by_hostname_server_and_script WHERE server_name = 'www.dailymotion.com' AND hostname LIKE 'web-%' GROUP BY hostname"
        <Result>
            Type "gauge"
            InstancePrefix "rps-web"
            InstancesFROM "hostname"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "tpr-web"
            InstancesFROM "hostname"
            ValuesFrom "tpr"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "mtpr-web"
            InstancesFROM "hostname"
            ValuesFrom "mtpr"
        </Result>
    </Query>

    <Query "pinba_apimethod_country">
        Statement "SELECT SUBSTRING_INDEX(script_name, '.', 1) AS country, SUM(req_per_sec)*1 AS rps FROM tag_report_group_apimethod WHERE `group` = 'api' AND script_name NOT LIKE '/data/web%' GROUP BY country"
        <Result>
            Type "gauge"
            InstancePrefix "rps-apimethod-country"
            InstancesFROM "country"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_apimethod_object">
        Statement "SELECT SUBSTRING_INDEX(apimethod, '.', 1) AS object, SUM(req_per_sec) * 1 AS rps FROM tag_report_group_apimethod WHERE `group` = 'api' AND script_name NOT LIKE '/data/web%' GROUP BY object"
        <Result>
            Type "gauge"
            InstancePrefix "rps-apimethod-object"
            InstancesFROM "object"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_apimethod_method">
        Statement "SELECT apimethod, SUM(req_per_sec) AS rps, SUM(timer_value) / SUM(req_count) AS tpr FROM tag_report_group_apimethod WHERE `group` = 'api' AND script_name NOT LIKE '/data/web%' GROUP BY apimethod"
        <Result>
            Type "gauge"
            InstancePrefix "rps-apimethod-method"
            InstancesFROM "apimethod"
            ValuesFrom "rps"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "tpr-apimethod-method"
            InstancesFROM "method_value"
            ValuesFrom "tpr"
        </Result>
    </Query>

    <Query "pinba_apimethod_type">
        Statement "SELECT SUM(req_per_sec) AS rps, SUBSTRING_INDEX(SUBSTRING_INDEX(script_name, '.', 2), '.', -1) AS type FROM tag_report_group_apimethod WHERE `group` = 'api' AND script_name NOT LIKE '/data/web%' GROUP BY type"
        <Result>
            Type "gauge"
            InstancePrefix "rps-apimethod-type"
            InstancesFROM "type"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_memcache">
        Statement "SELECT SUBSTR(counter FROM INSTR(counter, '.') + 1) AS clef, 1.0 * req_per_sec AS rps, timer_value / req_count AS tpr FROM tag_info_counter WHERE counter LIKE 'memcache.%'"
        <Result>
            Type "gauge"
            InstancePrefix "rps-memcache"
            InstancesFROM "clef"
            ValuesFrom "rps"
        </Result>
    </Query>

    <Query "pinba_playlist">
        Statement "SELECT SUM(req_time_total) / SUM(req_count) AS average_time FROM report_by_script_name WHERE script_name LIKE '%.html.playlist_list%' ORDER BY script_name"
        <Result>
            Type "gauge"
            InstancePrefix "playlist_rta"
            ValuesFrom "average_time"
        </Result>
    </Query>

    <Query "oauth_backend">
        Statement "SELECT concat(`group`, '.', method) AS backend, SUM(req_count), SUM(hit_count), SUM(timer_value) / SUM(hit_count) AS time_per_hit FROM tag_report_group_method WHERE (script_name LIKE '%oauth_token%' OR script_name LIKE '%oauth_authorize%') AND `group` != 'localcache' GROUP BY backend"
        <Result>
            Type "gauge"
            InstancePrefix "oauth_backend_req"
            InstancesFROM "backend"
            ValuesFrom "SUM(req_count)"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_backend_hit"
            InstancesFROM "backend"
            ValuesFrom "SUM(hit_count)"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_backend_tph"
            InstancesFROM "backend"
            ValuesFrom "time_per_hit"
        </Result>
    </Query>

    <Query "oauth_token_activity">
        Statement "SELECT 'oauth', SUM(req_count) AS req_count, SUM(req_per_sec) AS req_per_sec, SUM(req_time_median) / COUNT(1) AS time_median FROM report_by_script_name WHERE script_name LIKE '%oauth_token%'"
        <Result>
            Type "gauge"
            InstancePrefix "oauth_token_req_count"
            InstancesFROM "oauth"
            ValuesFrom "req_count"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_token_req_per_sec"
            InstancesFROM "oauth"
            ValuesFrom "req_per_sec"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_token_time_median"
            InstancesFROM "oauth"
            ValuesFrom "time_median"
        </Result>
    </Query>

    <Query "oauth_authorize_activity">
        Statement "SELECT 'oauth', SUM(req_count) AS req_count, SUM(req_per_sec) AS req_per_sec, SUM(req_time_median) / count(1) AS time_median FROM report_by_script_name WHERE script_name LIKE '%oauth_authorize%'"
        <Result>
            Type "gauge"
            InstancePrefix "oauth_authorize_req_count"
            InstancesFROM "oauth"
            ValuesFrom "req_count"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_authorize_req_per_sec"
            InstancesFROM "oauth"
            ValuesFrom "req_per_sec"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "oauth_authorize_time_median"
            InstancesFROM "oauth"
            ValuesFrom "time_median"
        </Result>
    </Query>

    <Query "pinba_facebook_api_calls">
        Statement "SELECT 'facebook', SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS response_time FROM tag_report_group_method WHERE `group` = 'facebook'"
        <Result>
            Type "gauge"
            InstancePrefix "facebook_hits"
            InstancesFROM "facebook"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "facebook_response_time"
            InstancesFROM "facebook"
            ValuesFrom "response_time"
        </Result>
    </Query>

    <Query "pinba_googleplus_api_calls">
        Statement "SELECT 'googleplus', SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS response_time FROM tag_report_group_method WHERE `group` = 'google_plus'"
        <Result>
            Type "gauge"
            InstancePrefix "googleplus_hits"
            InstancesFROM "googleplus"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "googleplus_response_time"
            InstancesFROM "googleplus"
            ValuesFrom "response_time"
        </Result>
    </Query>

    <Query "pinba_cleeng_api_calls">
        Statement "SELECT 'cleeng', SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS response_time, SUM(hit_count) / SUM(req_count) AS hit_per_req FROM tag_report_group_method WHERE `group` = 'cleeng'"
        <Result>
            Type "gauge"
            InstancePrefix "cleeng_hits"
            InstancesFROM "cleeng"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "cleeng_response_time"
            InstancesFROM "cleeng"
            ValuesFrom "response_time"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "cleeng_hpr"
            InstancesFROM "cleeng"
            ValuesFrom "hit_per_req"
        </Result>
    </Query>

    <Query "pinba_mandrill">
        Statement "SELECT 'mandrill', SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS response_time FROM tag_report_group_method WHERE `group` = 'mandrill'"
        <Result>
            Type "gauge"
            InstancePrefix "mandrill_total_hits"
            InstancesFROM "mandrill"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "mandrill_response_time"
            InstancesFROM "mandrill"
            ValuesFrom "response_time"
        </Result>
    </Query>

    <Query "pinba_akismet">
        Statement "SELECT 'akismet', SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS response_time FROM tag_report_group_method WHERE `group` = 'akismet'"
        <Result>
            Type "gauge"
            InstancePrefix "akismet_total_hits"
            InstancesFROM "akismet"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "akismet_response_time"
            InstancesFROM "akismet"
            ValuesFrom "response_time"
        </Result>
    </Query>

    <Query "pinba_spam">
        Statement "SELECT counter, SUM(hit_per_sec) as hps FROM tag_report_counter WHERE counter LIKE 'spam.%' GROUP BY counter"
        <Result>
            Type "gauge"
            InstancePrefix "spam_hps"
            InstancesFROM "counter"
            ValuesFrom "hps"
        </Result>
    </Query>

    <Query "pinba_advertising">
        Statement "SELECT 'advertising', SUM(req_count) AS total_req, SUM(hit_count) AS total_hit, SUM(timer_value) / SUM(hit_count) AS time_per_hit FROM tag_report_group_apimethod WHERE apimethod = 'video.advertising'"
        <Result>
            Type "gauge"
            InstancePrefix "advertising_total_req"
            InstancesFROM "advertising"
            ValuesFrom "total_req"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "advertising_total_hit"
            InstancesFROM "advertising"
            ValuesFrom "total_hit"
        </Result>
        <Result>
            Type "gauge"
            InstancePrefix "advertising_tph"
            InstancesFROM "advertising"
            ValuesFrom "time_per_hit"
        </Result>
    </Query>

    <Database "pinba">
        Driver "mysql"
        DriverOption "host" "localhost"
        DriverOption "username" "root"
        DriverOption "password" ""
        DriverOption "dbname" "pinba"
        SelectDB "pinba"
        Query "pinba_global"
        Query "pinba_output"
        Query "pinba_db_output"
        Query "pinba_country"
        Query "pinba_page_type"
        Query "pinba_main_page"
        Query "pinba_main_page_no_bot"
        Query "pinba_related"
        Query "pinba_related2"
        Query "pinba_related_country"
        Query "pinba_webapp1"
        Query "pinba_video_list"
        Query "pinba_playertab"
        Query "pinba_es_search"
        Query "pinba_web_perf"
        Query "pinba_apimethod_country"
        Query "pinba_apimethod_object"
        Query "pinba_apimethod_method"
        Query "pinba_apimethod_type"
        Query "pinba_memcache"
        Query "pinba_status"
        Query "pinba_status_nobot"
        Query "pinba_status_bot"
        Query "pinba_playlist"
        Query "oauth_backend"
        Query "oauth_authorize_activity"
        Query "oauth_token_activity"
        Query "pinba_facebook_api_calls"
        Query "pinba_googleplus_api_calls"
        Query "pinba_cleeng_api_calls"
        Query "pinba_mandrill"
        Query "pinba_akismet"
        Query "pinba_spam"
        Query "pinba_advertising"
#       Query "pinba_searchctr"
#       Query "..."
    </Database>
</Plugin>