import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    # Connect to the MySQL server
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        return

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Execute the SQL query to fetch cities of the given state
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    city_names = ', '.join([row[0] for row in results])
    print(city_names)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_by_state(username, password, database, state_name)
