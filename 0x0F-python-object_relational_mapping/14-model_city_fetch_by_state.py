#!/usr/bin/python3
"""Script that fetches all states from the table"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (session.query(State.name, City.id, City.name)
                  .filter(State.id == City.state_id)):
        print("{}: ({}) {}".format(state[0], state[1], state[2]))

    session.close()
