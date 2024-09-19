from connect_mysql import connect_database
import connect_mysql

#ASSIGNMENT 1

# Task 1
def add_member(name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
           
            new_member = (name, age) #assigns a variable to a tuple containing name and age
            query = "INSERT INTO Members (name, age) VALUES (%s, %s)" #inserts data at %s placeholder, adds it to Members table
            
            cursor.execute(query, new_member) # executes query in MySQL
            conn.commit() #finalizes the query

            print("New member added successfully!")
        except connect_mysql.Error as db_error: 
            print(f"Database Error: {db_error}") #informs you of an error that occurred when attempting the query in MySQL
        except Exception as e:
            print(f"An Error has occurred: {e}") #handles errors in Python
        
        finally: #Must ALWAYS close the cursor and connection, to prevent overusage of resources
            cursor.close() 
            conn.close()

#Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_session = (member_id, date, duration_minutes, calories_burned) #Organizes data into a tuple
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)" 
            #inserts data at %s placeholder and adds it to WorkoutSessions table
            
            cursor.execute(query, new_session)
            conn.commit()

            print("New session data added successfully!")
        except connect_mysql.Error as db_error:
            print(f"Database Error: {db_error}") #handles MySQL errors
        except Exception as e:
            print(f"An Error has occurred: {e}") #handles Python errors
        
        finally:
            cursor.close()
            conn.close()

#Task 3
def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE Members SET age = %s WHERE id = %s" 
            #changes the age of the member in Members table who's id matches the input

            age_update = new_age, member_id 
            #sets inputs to a tuple. Constructed the tuple in the order in which they occur in the query so that they replace the correct %s placeholders.

            cursor.execute(query, age_update)
            conn.commit()
            print("Age updated successfully.")

        except connect_mysql.Error as db_error:
            print(f"Database Error: {db_error}") #handles MySQL Errors
        except Exception as e:
            print(f"An Error has occurred: {e}")#Handles Python Errors
        finally:
            cursor.close()
            conn.close()

#Task 4
def delete_workout_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s" #deletes row containing the session_id
            bad_session = session_id
            final_decision = input("Are you sure you want to delete this session? (yes/no) WARNING: This action is irreversable: ")
            #figured it would be prudent to make sure this is really what you want to do, given the permanent nature of a deletion of data

            if final_decision.lower() == 'yes':
                cursor.execute(query, bad_session)
                conn.commit()
                print("Session deleted successfully.")

        except connect_mysql.Error as db_error:
            print(f"Database Error: {db_error}")#Handles MySQL Errors
        except Exception as e:
            print(f"An Error has occurred: {e}")#Handles Python Errors
        finally:
            cursor.close()
            conn.close()

# add_member("Jane Doe", 22)
# add_workout_session(1, "2024-9-19", 30, 350)
# update_member_age(1, 36)
# delete_workout_session((1, ))