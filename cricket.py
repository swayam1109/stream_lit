import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize a list to store the cricket match entries
if "matches" not in st.session_state:
    st.session_state["matches"] = []

# Function to add a new match entry
def add_match():
    match = {
        "Date": match_date,
        "Team 1": team1,
        "Team 2": team2,
        "Team 1 Score": team1_score,
        "Team 2 Score": team2_score,
    }
    st.session_state["matches"].append(match)
    st.success("Match added successfully!")

# Title of the app
st.title("Cricket Match Entry App")

# Input fields for match details
st.header("Add a New Match")

match_date = st.date_input("Match Date", datetime.today())
team1 = st.text_input("Team 1 Name")
team2 = st.text_input("Team 2 Name")
team1_score = st.number_input("Team 1 Score", min_value=0, step=1)
team2_score = st.number_input("Team 2 Score", min_value=0, step=1)

# Button to add the match entry
if st.button("Add Match"):
    if team1 and team2:
        add_match()
    else:
        st.error("Please enter both team names.")

# Display the match entries
st.header("Match Entries")

if st.session_state["matches"]:
    df = pd.DataFrame(st.session_state["matches"])
    st.dataframe(df)
else:
    st.write("No match entries yet.")
