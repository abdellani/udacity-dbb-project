# About the program
This program is based on python and the `psycopg2` package, Its purpose is to give the user an idea about the activity on his website by running a set sql queries on the database to answer some key questions :
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
# Installation 
You can get a copy of this code by running the following command in your operating system
```
git clone git@github.com:abdellani/udacity-dbb-project.git
```
Another way is download directely archive file (but you'll not be able to get the updates): 
```
wget https://github.com/abdellani/udacity-dbb-project/archive/master.zip
```
To run this program, assert that the python package `psycopg2` is installed in your system.
```bash
pip install psycopg2
```
# Configuration 
The author supposes that you have a Postgres database server running in your localhost on the default port 5432, contaning a database called `news`, and having an account with the following credentials : username = `postgres`, password = `docker`.

If your context is different, you'll have to update the information in the `main.py` (lines 5-10)
```python
    conn = psycopg2.connect(
        database="news",
        user="postgres",
        host="127.0.0.1",
        password="docker"
    )
``` 
## Database
Before you run the program, connect to your database and execute the following script to create the `top_author_ids` view. This is required to run properly some queries properly:
```SQL
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
order by id_count desc;
```
# Run the code
To run the code, you need to get into the project folder and run the following command
```
python main.py
```
# Get updates
To receive the lastest updates, use the following command
```
git pull origin master
```
# Author
Mohamed ABDELLANI
