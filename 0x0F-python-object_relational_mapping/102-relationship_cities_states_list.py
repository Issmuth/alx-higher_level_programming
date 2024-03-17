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
    cities = session.query(City).order_by(City.id.asc()).all()
    for city in cities:
        state = city.state
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
