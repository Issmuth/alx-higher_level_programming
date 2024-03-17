#!/usr/bin/python3
"""Script that fetches all states from the table"""
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
