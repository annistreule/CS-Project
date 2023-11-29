import os
import pandas as pd
import streamlit as st
from collections import defaultdict

# Check if products.csv exists locally, otherwise download it from GitHub
if not os.path.exists('products.csv'):
    # Here you would put the code to download the file from GitHub
    pass

# Read the products.csv into a DataFrame
products_df = pd.read_csv('products.csv')

# Initialize session state variables
if "inventory_list" not in st.session_state:
    st.session_state.inventory_list = []
if 'decoded_info_dict' not in st.session_state:
    st.session_state.decoded_info_dict = {}

# Class definitions
class Product:
    def __init__(self, name, product_code, calories, expiry_days, quantity=1, owner=None):
        self.name = name
        self.product_code = product_code
        self.calories = calories
        self.expiry_days = expiry_days
        self.quantity = quantity
        self.owner = owner

class ApartmentFridge:
    def __init__(self):
        self.products = defaultdict(list)

    def add_product(self, product):
        if len(self.products[product.owner]) < 10:  # Max 10 products per owner
            self.products[product.owner].append(product)
            st.success(f"{product.name} added to {product.owner}'s fridge.")
        else:
            st.error(f"{product.owner}'s fridge is full!")

    def remove_product(self, product):
        if product in self.products[product.owner]:
            self.products[product.owner].remove(product)
            st.success(f"{product.name} removed from {product.owner}'s fridge.")

# Function to generate product code
def generate_product_code(article, owner):
    # [Your existing generate_product_code logic]
    pass  # Placeholder

# Function to decode product code
def decode_product_code(product_code):
    # [Your existing decode_product_code logic]
    pass  # Placeholder

# Function to save inventory to CSV file
def save_inventory_to_csv(inventory_list, file_name='products.csv'):
    inventory_df = pd.DataFrame(inventory_list)
    inventory_df.to_csv(file_name, index=False)
    st.success(f'Inventory saved to {file_name}')

# Streamlit UI components
st.title("Smart Refrigerator Management System")

# File uploader for the Product file
uploaded_file = st.sidebar.file_uploader("Upload your product file (CSV format)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['product_df'] = df
else:
    st.sidebar.write("Please upload a CSV file.")

# Product management section
with st.form("product_management"):
    st.write("### Manage Your Products")
    col1, col2 = st.columns(2)
    with col1:
        article = st.selectbox("Select Product", st.session_state['product_df']['name'].tolist())
        owner = st.selectbox("Select Owner", ["A", "B", "C", "D"])
    with col2:
        quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
        add_product = st.form_submit_button("Add Product")
        remove_product = st.form_submit_button("Remove Product")

# Add or remove products
fridge = ApartmentFridge()
if add_product:
    product_code = generate_product_code(article, owner)
    product = Product(article, product_code, 'calories', 'expiry_days', quantity, owner)
    fridge.add_product(product)
    st.session_state.inventory_list.append(product_code)
elif remove_product:
    # Logic to remove product
    # [You need to define how you identify which product to remove]

# Display current inventory
if st.button("Show Inventory"):
    for owner, products in fridge.products.items():
        st.write(f"Owner: {owner}")
        for product in products:
            st.write(f" - {product.name} ({product.quantity} pieces)")

# Save inventory to Excel
if st.button('Save Inventory to Excel'):
    save_to_excel(st.session_state.inventory_list)
    st.success('Inventory saved to Excel file.')

# Function to save data to an Excel file
def save_to_excel(data, file_name='inventory.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)

# When adding a product, update products_df and save to CSV
if add_product:
    # Logic to add product to products_df
    products_df.to_csv('products.csv', index=False)

# When removing a product, update products_df and save to CSV
if remove_product:
    # Logic to remove product from products_df
    products_df.to_csv('products.csv', index=False)
