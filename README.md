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

# Installation 
To run this program, assert that the python package `psycopg2` is installed in your system.
```bash
pip install psycopg2
```
# Author
Mohamed ABDELLANI
