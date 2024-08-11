import streamlit as st

# Define the Item and ShoppingCart classes
class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def remove_item(self, item_name):
        for item in self.cart:
            if item.name.lower() == item_name.lower():
                self.cart.remove(item)
                return True
        return False

    def view_cart(self):
        return self.cart

    def get_total(self):
        return sum(item.price for item in self.cart)

    def checkout(self):
        total = self.get_total()
        self.cart.clear()
        return total


# Initialize items and cart
items = [
    Item("T-shirt", 20.00, "Clothes"),
    Item("Jeans", 50.00, "Clothes"),
    Item("Watch", 150.00, "Accessories"),
    Item("Necklace", 75.00, "Accessories"),
    Item("Sofa", 300.00, "Furniture"),
    Item("Table", 120.00, "Furniture"),
    Item("Apples", 3.00, "Groceries"),
    Item("Milk", 2.50, "Groceries"),
]

cart = ShoppingCart()

# Streamlit app
st.title('Shopping Cart App')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select Page:', ['Home', 'View Cart', 'Checkout'])

# Home Page
if page == 'Home':
    st.header('Available Items')
    item_names = [item.name for item in items]
    selected_item = st.selectbox('Select an item to add to your cart:', item_names)

    if st.button('Add to Cart'):
        item_to_add = next((item for item in items if item.name == selected_item), None)
        if item_to_add:
            cart.add_item(item_to_add)
            st.success(f'Added {item_to_add.name} to your cart.')

    st.subheader('Items in Cart')
    cart_items = cart.view_cart()
    if cart_items:
        for item in cart_items:
            st.write(item)

# View Cart Page
elif page == 'View Cart':
    st.header('Your Cart')
    cart_items = cart.view_cart()
    if cart_items:
        for item in cart_items:
            st.write(item)
        st.write(f"Total: ${cart.get_total():.2f}")

        remove_item_name = st.text_input('Enter the name of the item to remove:')
        if st.button('Remove Item'):
            if cart.remove_item(remove_item_name):
                st.success(f'Removed {remove_item_name} from your cart.')
            else:
                st.error(f'{remove_item_name} not found in your cart.')

# Checkout Page
elif page == 'Checkout':
    st.header('Checkout')
    cart_items = cart.view_cart()
    if cart_items:
        st.write('Items in your cart:')
        for item in cart_items:
            st.write(item)
        st.write(f"Total: ${cart.get_total():.2f}")

        if st.button('Proceed to Checkout'):
            total = cart.checkout()
            st.success(f'Thank you for your purchase! Your total is ${total:.2f}.')
    else:
        st.write('Your cart is empty.')

# Footer
st.sidebar.write('Thank you for using the shopping app!')
