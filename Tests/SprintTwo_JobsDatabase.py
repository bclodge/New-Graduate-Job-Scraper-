import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connects to db or makes new one
    cursor = db_connection.cursor()  # reads/writes data
    return db_connection, cursor


# used these columns due to the similarity it would have with other jobs sites, also use f string to add which site it
# pulls from. (i.e 794026f2-dc61-11e8-93e0-d70b82e36db1_github
def setup_db(cursor: sqlite3.Cursor):
    cursor.execute(''' CREATE TABLE IF NOT EXISTS jobs(
    job_id TEXT PRIMARY KEY,
    job_type TEXT NOT NULL,
    job_url TEXT NOT NULL,
    created_at TEXT NOT NULL,
    company_posted TEXT NOT NULL,
    company_loc TEXT NOT NULL,
    job_title TEXT NOT NULL);''')


def write_to_db(cursor: sqlite3.Cursor, data):
    for job_posted in data:  # begin inserting values into table jobs
        cursor.execute(''' INSERT INTO jobs(
            job_id, job_type, job_url, created_at, company_posted, company_loc, job_title)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (job_posted['id'], job_posted['type'], job_posted['url'],
                                                  job_posted['created_at'], job_posted['company'],
                                                  job_posted['location'],
                                                  job_posted['title'])
                       )


def close_db(connection: sqlite3.Connection):
    connection.commit()  # makes sure all changes are saved
    connection.close()
