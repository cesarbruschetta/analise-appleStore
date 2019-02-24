""" module to utils methods """

import csv
import sqlite3

REPORT_HEAD_LIST = (
    "id",
    "track_name",
    "n_citacoes",
    "size_bytes",
    "price",
    "prime_genre",
)


def parcer_file(filename):
    """ parcer file csv to dict """
    data = []
    with open(filename) as f:
        records = csv.DictReader(f)
        for row in records:
            data.append(row)
    return data


def generate_csv(data, filename):
    """ Generete output file csv  """

    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(REPORT_HEAD_LIST)

        for row in data:
            writer.writerow([row.get(k, "") for k in REPORT_HEAD_LIST])


def initialization_database(db_file):
    """ initialization connection and configuration to data base """

    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS report_analyze (
        id int primary key, 
        track_name varchar, 
        n_citacoes varchar, 
        size_bytes varchar, 
        price varchar, 
        prime_genre varchar)"""
    )
    cur.close()

    return conn


def insert_report_data(conn, data):
    """ insert result to analyze data """

    sql = """INSERT INTO report_analyze (id, track_name, n_citacoes, size_bytes, price, prime_genre) 
            VALUES (?, ?, ?, ?, ?, ?)"""
    cur = conn.cursor()

    for row in data:
        cur.execute(sql, tuple(row.get(k, "") for k in REPORT_HEAD_LIST))

    cur.close()


def select_report_data(conn):
    """ select report data to DB  """

    cur = conn.cursor()
    cur.execute("SELECT * FROM report_analyze")

    report = cur.fetchall()
    cur.close()

    return report
