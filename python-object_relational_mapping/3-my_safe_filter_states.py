import MySQLdb
import sys


def search_states_safe(username, password, database, state_name):
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

    # Execute the SQL query to fetch matching states
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    cursor.execute(query, (state_name,))

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    