/*
  Top visited articles
*/
select articles.title,count(l.id) as id_count
from  
  articles 
left join 
  (select  substring(path from 10) as slug,id  from log where method='GET') as l 
on 
  articles.slug=l.slug 
group by 
  articles.title
order by id_count desc
;

/*
--results
               title                | id_count 
------------------------------------+----------
 Candidate is jerk, alleges rival   |   338647
 Bears love berries, alleges bear   |   253801
 Bad things gone, say good people   |   170098
 Goats eat Google's lawn            |    84906
 Trouble for troubled troublemakers |    84810
 Balloon goons doomed               |    84557
 There are a lot of bears           |    84504
 Media obsessed with bears          |    84383
(8 rows)
*/
/**
  most popular authors
*/

create view top_author_ids
as 
select articles.author as id,count(l.id) as id_count
from  
  articles 
left join 
  (select  substring(path from 10) as slug,id  from log where method='GET') as l 
on 
  articles.slug=l.slug 
group by 
  articles.author
order by id_count desc
;
select authors.name,id_count from authors left join top_author_ids on  authors.id= top_author_ids.id;

/**
          name          | id_count 
------------------------+----------
 Ursula La Multa        |   507594
 Rudolf von Treppenwitz |   423457
 Anonymous Contributor  |   170098
 Markoff Chaney         |    84557
*/
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
/**
     d      | errors_percentage  
------------+--------------------
 2016-07-17 | 2.2626862468027260
(1 row)
*/