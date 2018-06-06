##!/usr/bin/python3
import psycopg2


def first():
    result = ""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
        select title, sum(numart) num from articles a
        inner join
        (select split_part(path,'/',3) as art, count(path) as numart from log
        where status = '200 OK' and path is not null group by path) b
            on a.slug = b.art
            group by title
            order by 2 desc
            limit 3;
    """)
    result_set = c.fetchall()
    result += "1. Three most popular articles\n\n"
    for row in result_set:
        result += '"%s" - %s views\n' % (row[0], row[1])
    db.close()
    return result


def second():
    result = ""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
        select name, num from authors c
        join (select author, sum(numart) num from articles a
            inner join
            (select split_part(path,'/',3) art, count(path) numart from log
                where status = '200 OK' and path is not null group by path) b
            on a.slug = b.art group by author) d
        on c.id = d.author order by 2 desc;""")
    result_set = c.fetchall()
    result += "\n2. Authors ranked by viewed articles\n\n"
    for row in result_set:
        result += '"%s" - %s views\n' % (row[0], row[1])
    db.close()
    return result


def third():
    result = ""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""
        select TO_CHAR(a.days::DATE, 'Month dd, yyyy'),
            round(100*ErrorNum/totalcount::numeric,2) perc
        from (select date(time) days, count(id) totalcount from log
            group by date(time)) a
            join (select date(time) days, count(id) ErrorNum from log
            where status = '404 NOT FOUND' group by date(time)) b
                on a.days = b.days where  100*ErrorNum/totalcount::float > 1;
        """)
    result_set = c.fetchall()
    result += "\n3. Days with more than 1 percent errors\n\n"
    for row in result_set:
        result += '%s - %s errors\n' % (row[0], row[1])
    db.close()
    return result


def writefile():
    testfile = open("testfile.txt", 'w')
    testfile.write(first())
    testfile.write(second())
    testfile.write(third())
    testfile.close()

def printResults():
    print(first())
    print(second())
    print(third())

writefile()
printResults()