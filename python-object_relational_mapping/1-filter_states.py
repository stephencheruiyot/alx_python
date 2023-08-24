#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(host="localhost", 
                             port=3306, 
                             user=username, 
                             passwd=password, 
                             db=database_name)
        cursor = db.cursor()

        # Create the SQL query to fetch states starting with "N"
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
