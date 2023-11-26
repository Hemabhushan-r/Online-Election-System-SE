# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root"
# ) 
# c = mydb.cursor()

import streamlit as st
from create import main as create
from database import create_table
from delete import delete
from read import read
from update import update
from query import query
import subprocess

def main():
    st.title("Election Management System")
    menu = ["Create", "Read", "Update", "Delete","Query","Logout"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()
    if choice == "Create":
        st.subheader("Enter Voter Details:")
        create()
    elif choice == "Read":
        st.subheader("View created tasks")
        read()
    elif choice == "Update":
        st.subheader("Update created tasks")
        update()
    elif choice == "Delete":
        st.subheader("Delete created tasks")
        delete()
    elif choice == "Query":
        st.subheader("Add a query")
        question=st.text_input("Enter query:")
        query(question)
    elif choice == "Logout":
         subprocess.run(["streamlit", "run", "login.py"])
    else:
        st.subheader("About tasks")
if __name__ == '__main__':
    main()