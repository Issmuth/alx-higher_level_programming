#!/usr/bin/python3
"""Script that prints all cities in a state"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    query = "SELECT cities.name\
             FROM cities\
             INNER JOIN (SELECT * FROM states WHERE states.name = %s) s\
             ON s.id = cities.state_id ORDER BY cities.id ASC"

    db = MySQLdb.connect(host="localhost", user=user, passwd=password,
                         db=database, port=3306)

    cr = db.cursor()
    cr.execute(query, (state,))
    records = cr.fetchall()
    for i in range(len(records)):
        print(records[i][0].strip('()').strip('\'"'), end="")
        if i + 1 != len(records):
            print('', end=", ")
        else:
            print()

    cr.close()
    db.close()
