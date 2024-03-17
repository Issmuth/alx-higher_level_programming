#!/usr/bin/python3
"""Script that fetches all states from the table"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).\
        order_by(State.id.asc()).filter(State.name == (sys.argv[4]))

    if states is None:
        print('Not found')
    else:
        print(states[0].id)

    session.close()
