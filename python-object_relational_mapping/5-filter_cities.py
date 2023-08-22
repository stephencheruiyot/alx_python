
import MySQLdb

if __name__ == "__main__":

 def filter_cities(username, password, database, state_name):
    
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="Folio9470m",
            db="hbtn_0e_4_usa"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Define the prepared statement to retrieve cities of the specified state
        cities_query = """
        SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        # Execute the prepared statement with the state name
        cursor.execute(cities_query, (state_name,))

        # Commit changes to the database
        database.commit()

        # Fetch all the rows from the result set
        results = cursor.fetchall()

        # Display the results
        city_names = [row[0] for row in results]
        print(", ".join(city_names))

        # Close the cursor and the database connection
        cursor.close()
        db.close()
        

