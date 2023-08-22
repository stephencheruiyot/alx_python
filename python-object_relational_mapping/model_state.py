#!/usr/bin/python3
"""Link Class to Database Table

This script defines a State class that links to a MySQL table named 'states'.
It uses SQLAlchemy to interact with the database.

Usage:
    Usage: python script.py <username> <password> <database>
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of the declarative base
Base = declarative_base()

# Define the State class
class State(Base):
    """State Class
    
    Represents a state entity in the 'states' table.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Create an engine to connect to the database
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create the tables
        Base.metadata.create_all(engine)
