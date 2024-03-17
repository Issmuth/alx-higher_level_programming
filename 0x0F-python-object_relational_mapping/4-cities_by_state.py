#!/usr/bin/python3
"""Script that prints all cities in a state"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    query = "SELECT cities.id, cities.name, states.name\
             FROM cities\
             INNER JOIN states\
             ON states.id = cities.state_id ORDER BY cities.id ASC"

    db = MySQLdb.connect(host="localhost", user=user, passwd=password,
                         db=database, port=3306)

    cr = db.cursor()
    cr.execute(query)
    records = cr.fetchall()
    for row in records:
        print(row)

    cr.close()
    db.close()
