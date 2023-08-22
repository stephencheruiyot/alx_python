#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 9-model_state_filter_a.py <username> <password> <database>")
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

        # Retrieve State objects containing the letter 'a'
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

        # Print the results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

        # Close the session
        session.close()
