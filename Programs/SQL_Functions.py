import psycopg2
from psycopg2 import Error

# Function to establish a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Aryan@1986",
            host="localhost",
            port="5432",
            database="TestDB"
        )
        
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

# Create operation
def create_record(connection, data):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO Records (status, description, ticket_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, data)
        connection.commit()
        print("Record inserted successfully")        
    except (Exception, Error) as error:
        print("Error while inserting a record:", error)

# Read operation
def read_records(connection, query):
    try:
        cursor = connection.cursor()
        select_query = query
        cursor.execute(select_query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except (Exception, Error) as error:
        print("Error while reading records:", error)

# Update operation
def update_record(connection, new_data):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE your_table SET name = %s, email = %s WHERE id = %s"
        cursor.execute(update_query, (new_data))
        connection.commit()
        print("Record updated successfully")
    except (Exception, Error) as error:
        print("Error while updating a record:", error)

# Delete operation
def delete_record(connection, id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_query, (id))
        connection.commit()
        print("Record deleted successfully")
    except (Exception, Error) as error:
        print("Error while deleting a record:", error)

con = create_connection()
if con != 0:
 print("DB Connection is Established")