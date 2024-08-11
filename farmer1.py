import streamlit as st
import pandas as pd
import os

# File path for storing solutions
DATA_PATH = 'data/solutions.csv'

# Create the data directory and file if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.isfile(DATA_PATH):
    df = pd.DataFrame(columns=['Issue', 'Details', 'Solution'])
    df.to_csv(DATA_PATH, index=False)

def load_data():
    return pd.read_csv(DATA_PATH)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# Streamlit app
st.title('Farmer Assistant App')

# Sidebar for navigation
st.sidebar.header('Navigation')
selection = st.sidebar.radio('Go to', ['Home', 'Submit Issues', 'View Solutions'])

# Home page
if selection == 'Home':
    st.header('Welcome to the Farmer Assistant App')
    st.write('Use this app to manage and resolve agricultural issues related to soil, land texture, leaf diseases, water problems, climatic conditions, and pesticide usage.')
    st.image('https://www.welcometothejungle.com/en/articles/wp-content/uploads/2021/03/importance-of-farming.jpeg', caption='Farming', use_column_width=True)

# Submit Issues page
elif selection == 'Submit Issues':
    st.header('Submit Your Agricultural Issues')
    
    with st.form(key='submit_issues'):
        soil_type = st.text_input('Soil Type')
        land_texture = st.text_input('Land Texture')
        leaf_diseases = st.text_area('Leaf Diseases')
        water_problems = st.text_area('Water Problems')
        climatic_conditions = st.text_input('Climatic Conditions')
        pesticide_usage = st.text_area('Pesticide Usage')
        
        submit_button = st.form_submit_button(label='Submit Issues')
        
        if submit_button:
            # For simplicity, assume that solutions are predefined
            df = load_data()
            new_entry = pd.DataFrame({
                'Issue': ['Soil Type', 'Land Texture', 'Leaf Diseases', 'Water Problems', 'Climatic Conditions', 'Pesticide Usage'],
                'Details': [soil_type, land_texture, leaf_diseases, water_problems, climatic_conditions, pesticide_usage],
                'Solution': ['Solution for ' + soil_type, 'Solution for ' + land_texture, 'Solution for ' + leaf_diseases, 
                             'Solution for ' + water_problems, 'Solution for ' + climatic_conditions, 'Solution for ' + pesticide_usage]
            })
            df = pd.concat([df, new_entry], ignore_index=True)
            save_data(df)
            st.success('Your issues have been submitted and solutions are being generated.')

# View Solutions page
elif selection == 'View Solutions':
    st.header('View Solutions for Submitted Issues')
    df = load_data()
    
    if not df.empty:
        st.dataframe(df)
        for index, row in df.iterrows():
            st.subheader(f"Issue: {row['Issue']}")
            st.write(f"**Details:** {row['Details']}")
            st.write(f"**Solution:** {row['Solution']}")
    else:
        st.write('No solutions available. Please submit your issues first.')

# Run the app
if __name__ == '__main__':
    st.write('Running the Farmer Assistant App.')
