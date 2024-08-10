import streamlit as st

# Initialize the student accounts dictionary
if 'students' not in st.session_state:
    st.session_state['students'] = {}

# Function to create a new student account
def create_account(student_name):
    if student_name in st.session_state['students']:
        st.warning("Account already exists!")
    else:
        st.session_state['students'][student_name] = 0
        st.success(f"Account created for {student_name}!")

# Function to deposit money
def deposit(student_name, amount):
    if student_name in st.session_state['students']:
        st.session_state['students'][student_name] += amount
        st.success(f"Deposited {amount} to {student_name}'s account!")
    else:
        st.error("Student account does not exist!")

# Function to withdraw money
def withdraw(student_name, amount):
    if student_name in st.session_state['students']:
        if st.session_state['students'][student_name] >= amount:
            st.session_state['students'][student_name] -= amount
            st.success(f"Withdrew {amount} from {student_name}'s account!")
        else:
            st.error("Insufficient funds!")
    else:
        st.error("Student account does not exist!")

# Function to view account balance
def view_balance(student_name):
    if student_name in st.session_state['students']:
        balance = st.session_state['students'][student_name]
        st.info(f"{student_name}'s account balance: {balance}")
    else:
        st.error("Student account does not exist!")

# Streamlit app UI
st.title("Student Bank App")

st.header("Create a New Student Account")
student_name_create = st.text_input("Student Name for Account Creation")
if st.button("Create Account"):
    create_account(student_name_create)

st.header("Deposit Money")
student_name_deposit = st.text_input("Student Name for Deposit")
deposit_amount = st.number_input("Deposit Amount", min_value=0, step=1)
if st.button("Deposit"):
    deposit(student_name_deposit, deposit_amount)

st.header("Withdraw Money")
student_name_withdraw = st.text_input("Student Name for Withdrawal")
withdraw_amount = st.number_input("Withdraw Amount", min_value=0, step=1)
if st.button("Withdraw"):
    withdraw(student_name_withdraw, withdraw_amount)

st.header("View Account Balance")
student_name_balance = st.text_input("Student Name for Balance Check")
if st.button("View Balance"):
    view_balance(student_name_balance)

st.header("All Student Accounts")
if st.session_state['students']:
    st.write(st.session_state['students'])
else:
    st.write("No student accounts available.")
