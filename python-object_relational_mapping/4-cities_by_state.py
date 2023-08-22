#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb

if __name__ == "__main__":
    
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="Folio9470m",
        db="hbtn_0e_0_usa"
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a single query to retrieve cities with their corresponding states
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)

    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
