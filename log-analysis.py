import psycopg2
DB_NAME = "news"

THREE_POP_ARTICLES = '''
SELECT
    a.title , count(l.id) as views
FROM
    articles as a LEFT JOIN log as l
    ON CONCAT('/article/',a.slug) = l.path
GROUP BY a.title
ORDER BY views DESC
LIMIT 3;
'''
MOST_POP_AUTHORS = '''
SELECT
    au.name as name, COUNT(au.id) as total_views
FROM
    authors as au LEFT JOIN articles as ar
    ON au.id = ar.author
    LEFT JOIN log as l
    ON CONCAT('/article/',ar.slug) = l.path
GROUP BY au.id
ORDER BY total_views DESC;
'''
ERROR = '''
SELECT
    to_char(errors_by_day.date,'Month DD, YYYY') as date,
    to_char(((errors_by_day.count::decimal/requests_by_day.count::decimal)*100),'9.99') || '%' as percent
FROM
    (select date(time),count(*) FROM log
        GROUP BY date(time)) as requests_by_day,
    (select date(time),count(*) FROM log WHERE status != '200 OK'
        GROUP BY date(time)) as errors_by_day
WHERE
    requests_by_day.date = errors_by_day.date
    and ((errors_by_day.count::decimal/requests_by_day.count::decimal)*100) > 1;
'''

def ConnectDB(query):
    db = psycopg2.connect(database=DB_NAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

def MOST_POP_ARTICLES():
    print "what are the most popular three articles of all time?\n"
    rows = ConnectDB(THREE_POP_ARTICLES)
    for row in rows:
        print "%s - %d views" % (row[0], row[1])

def MOST_POP_AUTHOR():
    print "who are the most popular article authors of all time?\n"
    rows = ConnectDB(MOST_POP_AUTHORS)
    for row in rows:
        print "%s - %d views" % (row[0], row[1])

def ERRORS():
    print "ON which days did more than 1% of requests lead to errors?\n"
    rows = ConnectDB(ERROR)
    for row in rows:
        print "%s - %s errors" % (row[0], row[1])

def LetItRip():
    print ""
    MOST_POP_ARTICLES()
    print "\n"
    MOST_POP_AUTHOR()
    print "\n"
    ERRORS()

LetItRip()
