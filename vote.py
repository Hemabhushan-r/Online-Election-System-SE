import streamlit as st
from database import add_vote


def vote():
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        BallotID = st.text_input("BallotID:")
        ElectionID = st.text_input("ElectionID:")
    with col2:
        CandidateID = st.text_input("CandidateID:")
        PartyID = st.text_input("PartyID:")
    with col3:
        PrecinctID = st.text_input("PrecinctID")
        VoteStatus = st.text_input("VoteStatus:")
    if st.button("Add Vote"):
        add_vote(BallotID,ElectionID,CandidateID,PartyID,PrecinctID,VoteStatus)
        st.success("Successfully added Voter: {}".format(BallotID, ElectionID, CandidateID, PartyID, PrecinctID, VoteStatus))
