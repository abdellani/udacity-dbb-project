import psycopg2


def run_sql(col1, col2, cmd):
    conn = psycopg2.connect(
        database="news",
        user="postgres",
        host="127.0.0.1",
        password="docker"
    )
    cur = conn.cursor()
    cur.execute(cmd)
    results = cur.fetchall()
    print "|{:50}|{:20}|".format(col1, col2)
    print "-" * 51 + "+" + "-" * 21
    i = 0
    while (i < len(results)):
        print "|{:50}|{:20}|".format(
            results[i][0].strftime("%d-%b-%Y")
            if (results[i][0].__class__.__name__ == 'date')
            else results[i][0],
            results[i][1])
        i += 1
    cur.close()
    conn.close()


topVisitArticlesSql = '''
select articles.title,count(l.id) as id_count
from
  articles
left join
  (select  substring(path from 10) as slug,id
  from log where method='GET') as l
on
  articles.slug=l.slug
group by
  articles.title
order by id_count desc
;
'''
mostPopularAuthorsSql = '''
drop view if exists top_author_ids;
create view top_author_ids
as
select articles.author as id,count(l.id) as id_count
from
  articles
left join
  (select  substring(path from 10) as slug,id
  from log where method='GET') as l
on
  articles.slug=l.slug
group by
  articles.author
order by id_count desc
;
select authors.name,id_count
from authors left join top_author_ids on  authors.id= top_author_ids.id;
'''
errorRatesSql = '''
select t1.d, 100.0 * t2.errors /t1.total as errors_percentage
from
(
  select date(time) as d, count(*) as total
  from log
  group by date(time)
) as t1 join (
  select date(time) as d, count(*) as errors
  from log
  where  status = '404 NOT FOUND'
  group by date(time)
) as t2
on t1.d = t2.d
where
100.0 * t2.errors /t1.total >1
order by t2.d;
'''
print("Welcome !")
while True:
    print("------------------------------------------------------------")
    print("Please select a question to get an anwser from the database:")
    print("[1] What are the most popular three articles of all time? ")
    print("[2] Who are the most popular article authors of all time? ")
    print("[3] On which days did more than 1% of requests lead to errors?  ")
    print("[4] Quit the program  ")
    user_inputs = raw_input()
    if(user_inputs == "1"):
        run_sql("Title", "Visits", topVisitArticlesSql)
        raw_input("\n\npress any key!\n")
    elif (user_inputs == "2"):
        run_sql("Author", "Visits", mostPopularAuthorsSql)
        raw_input("\n\npress any key!\n")
    elif (user_inputs == "3"):
        run_sql("Date", "Errors", errorRatesSql)
        raw_input("\n\npress any key!\n")
    elif (user_inputs == "4"):
        print "Good bye!"
        break
    else:
        print "Wrong value given !"
