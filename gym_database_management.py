from connect_mysql import connect_database

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
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

#Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    pass

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
            
            final_decision = input("Are you sure you want to delete this session? (yes/no) WARNING: This action is irreversable: ")
            if final_decision.lower() == 'yes':
                cursor.execute(query, session_id)
                print("Session deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

add_member()
add_workout_session()
update_member_age()
delete_workout_session()