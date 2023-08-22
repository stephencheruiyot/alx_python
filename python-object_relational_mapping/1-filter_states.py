#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
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

    # Execute the query to select states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
