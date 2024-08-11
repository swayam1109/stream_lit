import streamlit as st

# Define the Item class
class Item:
    def __init__(self, item_id, name, category, image):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.image = image

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Category: {self.category}"


# Initialize items
clothing_items = [
    Item(1, "T-Shirt", "Clothing", "https://via.placeholder.com/150?text=T-Shirt"),
    Item(2, "Jeans", "Clothing", "https://via.placeholder.com/150?text=Jeans"),
    Item(3, "Dress", "Clothing", "https://via.placeholder.com/150?text=Dress"),
]

furniture_items = [
    Item(4, "Chair", "Furniture", "https://via.placeholder.com/150?text=Chair"),
    Item(5, "Table", "Furniture", "https://via.placeholder.com/150?text=Table"),
    Item(6, "Sofa", "Furniture", "https://via.placeholder.com/150?text=Sofa"),
]

# Streamlit app
st.title('Virtual Shopping App')

# Sidebar for navigation
st.sidebar.title('Navigation')
category = st.sidebar.selectbox('Select Category', ['Clothing', 'Furniture'])

# Display items based on the selected category
if category == 'Clothing':
    st.header('Clothing Items')
    for item in clothing_items:
        st.image(item.image, caption=item.name, use_column_width=True)
        if st.button(f"Select {item.name}", key=item.item_id):
            st.write(f"You selected: {item.name}")
            st.image(item.image, caption=f"Visualizing {item.name}", use_column_width=True)

elif category == 'Furniture':
    st.header('Furniture Items')
    for item in furniture_items:
        st.image(item.image, caption=item.name, use_column_width=True)
        if st.button(f"Select {item.name}", key=item.item_id):
            st.write(f"You selected: {item.name}")
            st.image(item.image, caption=f"Visualizing {item.name}", use_column_width=True)
