from connect_mysql import connect_database
import mysql.connector
from mysql.connector import Error

#Task 1
def add_member(name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
           
            new_member = (name, age)
            query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
            
            cursor.execute(query, new_member)
            conn.commit()

            print("New member added successfully!")
        except mysql.connector.Error as db_error:
            print(f"Database Error: {db_error}")
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

#Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_session = (member_id, date, duration_minutes, calories_burned)
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            
            cursor.execute(query, new_session)
            conn.commit()

            print("New session data added successfully!")
        except mysql.connector.Error as db_error:
            print(f"Database Error: {db_error}")
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

#Task 3
def update_member_age(member_id, new_age):
    pass

#Task 4
def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            bad_session = session_id
            final_decision = input("Are you sure you want to delete this session? (yes/no) WARNING: This action is irreversable: ")
            if final_decision.lower() == 'yes':
                cursor.execute(query, bad_session)
                conn.commit()
                print("Session deleted successfully.")
        except mysql.connector.Error as db_error:
            print(f"Database Error: {db_error}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# add_member()
# add_workout_session(1, "2024-9-19", 30, 350)
# update_member_age()
delete_workout_session((16, ))