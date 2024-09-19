import mysql.connector
from mysql.connector import Error

def connect_database():
    try:
        conn = mysql.connector.connect(
            database = "gym_membership_db",
            user = "root",
            password = "password",
            host = "host number"
        )
        print("Connected to MySQL database successfully.")
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None
