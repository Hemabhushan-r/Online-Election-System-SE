import streamlit as st
from vote import vote
from voter_info import voter_info
from database import create_table

def main():
    menu = ["Vote", "Voter_Info"]
    choice = st.selectbox("Menu", menu)
    create_table()
    if choice == "Vote":
        st.subheader("Enter Vote Details:")
        vote()
    elif choice == "Voter_Info":
        st.subheader("Enter Voter Details:")
        voter_info()
    else:
        st.subheader("About tasks")
if __name__ == '__main__':
    main()