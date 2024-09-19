import mysql.connector
from mysql.connector import Error

def connect_database():
    try:
        conn = mysql.connector.connect(
            database = "fitness_center_db",
            user = "root",
            password = "Umbr3ll@4850",
            host = "127.0.0.1"
        )
        print("Connected to MySQL database successfully.")
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None
