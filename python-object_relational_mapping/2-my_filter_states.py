#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states
table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()

        # Create the SQL query using the user input
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE BINARY %s "
            "ORDER BY id ASC"
        )
        cursor.execute(query, (state_name,))

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
