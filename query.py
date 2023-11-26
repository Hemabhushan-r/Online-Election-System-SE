import pandas as pd
import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sabuj12345*",
    port=3306,
    database="project"
)
c=mydb.cursor()

def query(question):
    c.execute(question)
    data=c.fetchall()
    st.write(data)
