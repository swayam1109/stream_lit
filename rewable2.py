import streamlit as st
import pandas as pd
import os

# File path for storing listings
DATA_PATH = 'data/listings.csv'

# Create the data directory and file if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.isfile(DATA_PATH):
    df = pd.DataFrame(columns=['Title', 'Description', 'Price', 'Category', 'Location', 'Image URL'])
    df.to_csv(DATA_PATH, index=False)

def load_data():
    return pd.read_csv(DATA_PATH)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# Streamlit app
st.title('Renewable Energy Marketplace')

# Sidebar for navigation
st.sidebar.header('Navigation')
selection = st.sidebar.radio('Go to', ['Home', 'Add Listing', 'View Listings', 'Educational Content'])

# Home page
if selection == 'Home':
    st.header('Welcome to the Renewable Energy Marketplace')
    st.write('Find and offer renewable energy solutions tailored for rural areas.')
    st.image('https://www.energy.gov/sites/prod/files/styles/bio_image/public/2021/05/f/2021_us-department-of-energy.jpg', caption='Renewable Energy', use_column_width=True)

# Add Listing page
elif selection == 'Add Listing':
    st.header('Add a New Listing')
    
    with st.form(key='add_listing'):
        title = st.text_input('Title')
        description = st.text_area('Description')
        price = st.number_input('Price', min_value=0.0, format="%.2f")
        category = st.text_input('Category')
        location = st.text_input('Location')
        image_url = st.text_input('Image URL')
        
        submit_button = st.form_submit_button(label='Add Listing')
        
        if submit_button:
            df = load_data()
            new_listing = pd.DataFrame({
                'Title': [title],
                'Description': [description],
                'Price': [price],
                'Category': [category],
                'Location': [location],
                'Image URL': [image_url]
            })
            df = pd.concat([df, new_listing], ignore_index=True)
            save_data(df)
            st.success('Listing added successfully!')

# View Listings page
elif selection == 'View Listings':
    st.header('Available Renewable Energy Solutions')
    df = load_data()
    
    if not df.empty:
        st.dataframe(df)
        for index, row in df.iterrows():
            st.subheader(row['Title'])
            st.write(f"**Description:** {row['Description']}")
            st.write(f"**Price:** ${row['Price']:.2f}")
            st.write(f"**Category:** {row['Category']}")
            st.write(f"**Location:** {row['Location']}")
            if pd.notna(row['Image URL']):
                st.image(row['Image URL'], caption=row['Title'], use_column_width=True)
    else:
        st.write('No listings available.')

# Educational Content page
elif selection == 'Educational Content':
    st.header('Educational Resources')
    st.write('Here are some resources and tips for implementing renewable energy solutions in rural areas:')
    st.write('- **Understanding Solar Energy:** Learn how solar panels work and how they can be integrated into your farm operations.')
    st.write('- **Maintenance Tips:** Regular maintenance of renewable energy systems to ensure optimal performance.')
    st.write('- **Funding and Incentives:** Information on grants, subsidies, and incentives available for renewable energy projects.')
    st.write('- **Local Success Stories:** Case studies of local farmers who have successfully adopted renewable energy solutions.')

# Run the app
if __name__ == '__main__':
    st.write('Running the Renewable Energy Marketplace app.')
