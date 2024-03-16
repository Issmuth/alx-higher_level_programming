#!/usr/bin/python3
"""Script that lists all states from the
   database hbtn_0e_0_usa."""
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
name = sys.argv[4]
query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"

db = MySQLdb.connect(host="localhost", user=user, passwd=password,
                     db=database, port=3306)
cr = db.cursor()
cr.execute(query, (name,))
records = cr.fetchall()

for row in records:
    print(row)

cr.close()
db.close()

if __name__ == "__main__":
    pass
