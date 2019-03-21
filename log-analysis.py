#!/usr/bin/env python

import psycopg2
DB_NAME = "news"

THREE_POP_ARTICLES = '''
SELECT
    articles.title , count(*) as views
FROM
    articles INNER JOIN log
    ON log.path = CONCAT('/article/',articles.slug)
GROUP BY articles.title
ORDER BY views DESC LIMIT 3;
'''
MOST_POP_AUTHORS = '''
SELECT
    authors.name , COUNT(*) as viewss
FROM
    authors INNER JOIN articles
    ON authors.id = articles.author
    INNER JOIN log
    ON CONCAT('/article/',articles.slug) = log.path
GROUP BY authors.name
ORDER BY viewss DESC;
'''
ERROR = '''
SELECT
     TO_CHAR(total_requests_grouped.a,'Mon DD, YYYY') as date,
     round((cast((total_errors) as numeric)
     /cast((total_requests) as numeric)*100),2) as percentage
FROM
    ((select date(time) as a,count(*) as total_requests FROM log
     group by a) as total_requests_grouped
     left join
    (select date(time) as a,count(*) as total_errors
     FROM log where log.status != '200 OK'
     group by a) as total_errors_grouped
    on total_errors_grouped.a = total_requests_grouped.a)
    where (round((cast((total_errors) as numeric)
    /cast((total_requests) as numeric)*100),2) > 1.0);

'''


def ConnectDB(query):
    try:
        db = psycopg2.connect(database=DB_NAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    return rows
    db.close()


def MOST_POP_ARTICLES():
    print "what are the most popular three articles of all time?\n"
    rows = ConnectDB(THREE_POP_ARTICLES)
    for i in rows:
        print (str(i[0]) + " -- " + str(i[1]))


def MOST_POP_AUTHOR():
    print "who are the most popular article authors of all time?\n"
    rows = ConnectDB(MOST_POP_AUTHORS)
    for i in rows:
        print (str(i[0]) + " -- " + str(i[1]))


def ERRORS():
    print "ON which days did more than 1% of requests lead to errors?\n"
    rows = ConnectDB(ERROR)
    for i in rows:
        print (str(i[0]) + " -- " + str(i[1]) + "%")


if __name__ == '__main__':
    MOST_POP_ARTICLES()
    print "\n"
    MOST_POP_AUTHOR()
    print "\n"
    ERRORS()
