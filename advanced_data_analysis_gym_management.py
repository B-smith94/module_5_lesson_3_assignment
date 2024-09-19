from connect_mysql import connect_database
import connect_mysql

#ASSIGNMENT 2

#Task 1
def get_members_in_age_range(start_age, end_age):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                if start_age < end_age: 
                    #Used the If Then statement to account for times when the start_age value entered is greater than the end_age value
                    
                    query = "SELECT * FROM Members WHERE age > %s AND age < %s"
                    #displays all information for members whose ages fall within the given range
                    age_range = (start_age, end_age)
                    #sets the age range to a variable
                    cursor.execute(query, age_range)
                    
                    for row in cursor.fetchall(): 
                        print(row) 
                        #Iterates through each row in the Members table according to the query and prints out the information into a tuple
                else:
                    print("There was a problem with the range of ages selected.")

            except connect_mysql.Error as db_error:
                print(f"Database Error: {db_error}") #Handles MySQL Errors
            except Exception as e:
                print(f"An Error has occurred: {e}") #Handles Python Errors
            finally: 
                cursor.close() #closes the cursor connection
                conn.close() #Closes connection to Database
                
get_members_in_age_range(25, 30)