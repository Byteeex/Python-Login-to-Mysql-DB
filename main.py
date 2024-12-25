import mysql.connector
from getpass import getpass  # For secure password input

# Establish a connection to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",      # Replace with your MySQL host
        user="root",           # Replace with your MySQL username
        password="password",   # Replace with your MySQL password
        database="user_db"     # Replace with your database name
    )

# Function to validate user login
def login(cursor, username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return result

# Main program
def main():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()
        print("Connected to the database successfully!")
        
        print("\n=== Login ===")
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        if login(cursor, username, password):
            print("Login successful! Welcome,", username)
        else:
            print("Invalid username or password.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Disconnected from the database.")

if __name__ == "__main__":
    main()
