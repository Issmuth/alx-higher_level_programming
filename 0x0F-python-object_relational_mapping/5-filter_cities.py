#!/usr/bin/python3
"""Script that prints all cities in a state"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    query = """SELECT cities.name
             FROM cities
             INNER JOIN states ON states.id = cities.state_id
             WHERE states.name=%s"""

    db = MySQLdb.connect(host="localhost", user=user, passwd=password,
                         db=database, port=3306)

    cr = db.cursor()
    cr.execute(query, (state,))
    records = cr.fetchall()
    pr = list(row[0] for row in records)
    print(*pr, sep=", ")

    cr.close()
    db.close()
