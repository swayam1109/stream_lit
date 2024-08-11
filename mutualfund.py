import streamlit as st

# Define the SavingFund class
class SavingFund:
    def __init__(self, fund_id, name, category, return_rate):
        self.fund_id = fund_id
        self.name = name
        self.category = category
        self.return_rate = return_rate

    def __str__(self):
        return f"ID: {self.fund_id}, Name: {self.name}, Category: {self.category}, Return Rate: {self.return_rate}%"

# Initialize saving funds
funds = [
    SavingFund(1, "High Growth Fund", "Growth", 12.5),
    SavingFund(2, "Balanced Fund", "Balanced", 8.0),
    SavingFund(3, "Stable Income Fund", "Income", 5.0),
]

# User's portfolio
portfolio = {}

# Streamlit app
st.title('Saving Funds App')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select Page:', ['View Funds', 'My Portfolio', 'Investment Performance'])

# View Funds Page
if page == 'View Funds':
    st.header('Available Saving Funds')
    for fund in funds:
        st.write(f"**{fund.name}**")
        st.write(f"Category: {fund.category}")
        st.write(f"Return Rate: {fund.return_rate}%")
        st.write("---")

        if st.button(f"Add {fund.name} to Portfolio", key=fund.fund_id):
            if fund.fund_id in portfolio:
                st.write(f"{fund.name} is already in your portfolio.")
            else:
                portfolio[fund.fund_id] = fund
                st.success(f"Added {fund.name} to your portfolio.")

# My Portfolio Page
elif page == 'My Portfolio':
    st.header('Your Portfolio')
    if portfolio:
        for fund_id, fund in portfolio.items():
            st.write(f"**{fund.name}**")
            st.write(f"Category: {fund.category}")
            st.write(f"Return Rate: {fund.return_rate}%")
            st.write("---")
    else:
        st.write("Your portfolio is empty.")

# Investment Performance Page
elif page == 'Investment Performance':
    st.header('Investment Performance')
    if portfolio:
        st.write("Investment performance based on return rates:")
        for fund_id, fund in portfolio.items():
            st.write(f"**{fund.name}**: {fund.return_rate}% annual return")
            st.write("---")
    else:
        st.write("Your portfolio is empty. Add funds to your portfolio to see performance.")

# Footer
st.sidebar.write('Thank you for using the Saving Funds app!')
