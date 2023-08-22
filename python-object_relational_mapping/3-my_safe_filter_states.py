#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="Folio9470m",
        db="hbtn_0e_0_usa"

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
