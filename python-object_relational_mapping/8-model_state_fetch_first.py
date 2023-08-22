#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 8-model_state_fetch_first.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Create an engine and bind it to the base
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve the first State object
        first_state = session.query(State).order_by(State.id).first()

        # Print the result or "Nothing" if the table is empty
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

        # Close the session
        session.close()
