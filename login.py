import streamlit as st
import mysql.connector
import subprocess
from hashlib import sha256

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sabuj12345*",
        database="project"
    )

# Function to check user credentials
def authenticate_user(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    # Query to check if the username and password exist in the database
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    # Fetch the first result
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    connection.close()

    return result

def main():
    background_image_path = "ind.jpg" 

    # Specify the width of the image
    image_width = 100

    # Use st.image to display the image as a background with the specified width
    st.image(background_image_path, width=image_width, caption="")

    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Login"):
        # Check if the credentials are valid
        result = authenticate_user(username, password)

        if result:
            st.success("Login Successful!")
            # Run main1.py using subprocess
            subprocess.run(["streamlit", "run", "main1.py"])
        else:
            st.error("Invalid username or password.")

# Run the Streamlit app
if __name__ == "__main__":
    main()