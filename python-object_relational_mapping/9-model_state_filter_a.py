#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_a(username, password, database):
    # Create the MySQL connection
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_a(username, password, database)
