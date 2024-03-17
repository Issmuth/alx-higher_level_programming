#!/usr/bin/python3
"""Script that fetches all states from the table"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State.id, City.id, City.name)\
        .order_by(City.id).filter(State.id == City.id)
    if states is not None:
        for state in states:
            print("{}: ({}) {}".format(state[0], state[1], state[2]))

    session.close()
