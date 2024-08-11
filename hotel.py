import streamlit as st
import pandas as pd

# Sample data for rooms
rooms = [
    {"Room ID": 1, "Type": "Single", "Price per Night (₹)": 2000, "Availability": "Available"},
    {"Room ID": 2, "Type": "Double", "Price per Night (₹)": 3500, "Availability": "Available"},
    {"Room ID": 3, "Type": "Suite", "Price per Night (₹)": 6000, "Availability": "Booked"},
    {"Room ID": 4, "Type": "Deluxe", "Price per Night (₹)": 5000, "Availability": "Available"}
]

# Convert the list of dictionaries to a DataFrame
df_rooms = pd.DataFrame(rooms)

# Function to display room list
def display_room_list():
    st.write("### Available Rooms")
    st.dataframe(df_rooms[df_rooms["Availability"] == "Available"])

# Function to book a room
def book_room(room_id, customer_name, check_in_date, check_out_date):
    global df_rooms
    if room_id in df_rooms["Room ID"].values:
        room = df_rooms[df_rooms["Room ID"] == room_id]
        if room["Availability"].values[0] == "Available":
            df_rooms.loc[df_rooms["Room ID"] == room_id, "Availability"] = "Booked"
            st.success(f"Room {room_id} has been booked successfully for {customer_name}.")
            st.write(f"**Room Type:** {room['Type'].values[0]}")
            st.write(f"**Price per Night:** ₹{room['Price per Night (₹)'].values[0]}")
            st.write(f"**Check-in Date:** {check_in_date}")
            st.write(f"**Check-out Date:** {check_out_date}")
        else:
            st.error("Sorry, this room is already booked.")
    else:
        st.error("Invalid Room ID.")

# Streamlit app
st.title('Hotel Booking System')

# Sidebar for user inputs
st.sidebar.header('Booking Details')
customer_name = st.sidebar.text_input('Customer Name')
room_id = st.sidebar.number_input('Room ID', min_value=1, step=1)
check_in_date = st.sidebar.date_input('Check-in Date')
check_out_date = st.sidebar.date_input('Check-out Date')

# Display room list
display_room_list()

# Booking button
if st.sidebar.button('Book Room'):
    if customer_name and check_in_date and check_out_date:
        book_room(room_id, customer_name, check_in_date, check_out_date)
    else:
        st.error("Please fill in all the details before booking.")

# Display current room availability
st.write("### Current Room Availability")
st.dataframe(df_rooms)

