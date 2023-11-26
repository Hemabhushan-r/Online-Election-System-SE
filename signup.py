import streamlit as st
import mysql.connector

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sabuj12345*",
        database="project"
    )

# Function to create the 'users' table if it doesn't exist
def create_users_table():
    connection = create_connection()
    cursor = connection.cursor()

    # Define the table schema
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50)
        )
    """

    # Execute the query
    cursor.execute(create_table_query)

    # Commit and close
    connection.commit()
    connection.close()

# Function to insert a new user into the 'users' table
def insert_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()

    # Insert user into the table
    insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    user_data = (username, password)
    cursor.execute(insert_user_query, user_data)

    # Commit and close
    connection.commit()
    connection.close()

# Streamlit UI
def signup():
    st.title("Sign Up Page")

    # Create 'users' table if not exists
    create_users_table()

    # Get user input
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Sign-up button
    if st.button("Sign Up"):
        if username and password:
            # Insert user into the database
            insert_user(username, password)
            st.success("User successfully registered!")
        else:
            st.warning("Please enter both username and password.")

# Run the app
if __name__ == "__main__":
    signup()
