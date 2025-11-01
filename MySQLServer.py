import mysql.connector 
from mysql.connector import Error
def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="DaintyLaira1234"
            
        )
        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection safely
        try:
            if  connection.is_connected():
                cursor.close()
                connection.close()
            # print("MySQL connection is closed")
        except NameError:
            # connection variable might not exist if connection failed
            pass

if __name__ == "__main__":
    create_database()