import streamlit as st
import numpy as np
import pandas as pd

# Function to calculate future value of the investment
def calculate_future_value(principal, monthly_contribution, annual_return_rate, years):
    months = years * 12
    monthly_return_rate = annual_return_rate / 12 / 100
    future_value = 0
    
    for month in range(1, months + 1):
        future_value = (future_value + monthly_contribution) * (1 + monthly_return_rate)
        
    future_value += principal * (1 + monthly_return_rate) ** months
    return future_value

# Streamlit app
st.title('Mutual Fund Calculator (INR)')

# Sidebar for input
st.sidebar.header('Investment Details')
principal = st.sidebar.number_input('Initial Investment Amount (₹)', min_value=0.0, step=100.0, format="%.2f")
monthly_contribution = st.sidebar.number_input('Monthly Contribution (₹)', min_value=0.0, step=50.0, format="%.2f")
annual_return_rate = st.sidebar.slider('Expected Annual Return Rate (%)', min_value=0.0, max_value=20.0, step=0.1, format="%.2f")
years = st.sidebar.number_input('Investment Duration (Years)', min_value=1, step=1)

# Calculate future value
future_value = calculate_future_value(principal, monthly_contribution, annual_return_rate, years)

# Display results
st.header('Investment Projection')
st.write(f"**Initial Investment:** ₹{principal:.2f}")
st.write(f"**Monthly Contribution:** ₹{monthly_contribution:.2f}")
st.write(f"**Annual Return Rate:** {annual_return_rate:.2f}%")
st.write(f"**Investment Duration:** {years} years")

st.write(f"**Projected Future Value:** ₹{future_value:.2f}")

# Visualization
months = np.arange(1, years * 12 + 1)
values = [calculate_future_value(principal, monthly_contribution, annual_return_rate, month / 12) for month in months]

st.line_chart(values, use_container_width=True, 
               title='Investment Growth Over Time')

# Detailed table
investment_data = {
    'Month': months,
    'Future Value (₹)': values
}
df = pd.DataFrame(investment_data)
st.write("**Detailed Investment Growth Table:**")
st.dataframe(df)

# Footer
st.sidebar.write('Thank you for using the Mutual Fund Calculator (INR)!')
