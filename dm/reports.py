from reports import CardReport

report1 = CardReport(
    type='report4',
    tablename='{v1}_{v2}_report_by_server_and_script',
    tags = [
        ('site_content', (
            'fr', 'in', 'jp', 'kr', 'pk',
            'ru', 'tr', 'tw', 'us', 'vn'
        ))
    ],
    version='site_content'
)

report2 = CardReport(
    type='report4',
    tablename='{v1}_{v2}_report_by_server_and_script',
    tags= [
        ('provider', (
            'php', 'hhvm',
        ))
    ],
    version='provider',
    percentiles=['95']
)

report3 = CardReport(
    type='report4',
    tablename='{v1}_{v2}_report_by_server_and_script',
    tags= [
        ('format', (
            'atom', 'html', 'iphonerss', 'json', 'podcast',
            'rest', 'rss', 'sequence', 'swf', 'thumbnail',
            'videowall', 'videozap', 'widget'
        ))
    ],
    version='format',
    percentiles=['95']
)

report4 = CardReport(
    type='report2',
    tablename='{v1}_{v2}_report_by_server_name',
    tags = [
        ('site_content', (
            'fr', 'in', 'jp', 'kr', 'pk',
            'ru', 'tr', 'tw', 'us', 'vn'
        ))
    ],
    version='site_content'
)

report5 = CardReport(
    type='report8',
    tablename='{v1}_{v2}_report_by_status',
    tags = [
        ('bot', ('yes', 'no'))
    ],
    version='bot'
)

report6 = CardReport(
    type='report4',
    tablename='{v1}_{v2}_report_by_server_name',
    tags = [
        ('format', (
            'atom', 'html', 'iphonerss', 'json', 'podcast',
            'rest', 'rss', 'sequence', 'swf', 'thumbnail',
            'videowall', 'videozap', 'widget'
        ))
    ],
    version='format'
)

report7 = CardReport(
    type='report2',
    tablename='{v1}_{v2}_report_by_server_name',
    tags = [
        ('bot', ('yes', 'no'))
    ],
    version='bot'
)

report8 = CardReport(
    type='report4',
    tablename='{v1}_{v2}_report_by_server_and_script',
    tags = [
        ('bot', ('yes', 'no'))
    ],
    version='bot'
)
