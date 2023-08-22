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

    # Create the "states" table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS states (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
    )
    """
    cursor.execute(create_table_query)
    
    # Commit changes to the database
    db.commit()


    # Insert data into the "states" table
    insert_data_query = """
    INSERT INTO states (name) VALUES
        ('California'),
        ('Arizona'),
        ('Texas'),
        ('New York'),
        ('Nevada')
    """
    cursor.execute(insert_data_query)

    # Execute the query to select states in ascending order by states.id
    select_query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(select_query)
    
      # Commit changes to the database
    db.commit()

    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
