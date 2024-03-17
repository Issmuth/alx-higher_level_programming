#!/usr/bin/python3
"""Script that creates a State
with a city along with it.
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        cities = state.cities
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
