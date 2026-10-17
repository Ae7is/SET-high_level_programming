#!/usr/bin/python3
"""List all City objects with the name of their State."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).options(
        joinedload(City.state)).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
