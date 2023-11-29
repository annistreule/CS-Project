#Import relevant libraries
import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from collections import defaultdict

# Initialize inventory list in session state to save data entries
if "inventory_list" not in st.session_state:
    st.session_state.inventory_list = []

# Read the Product file
df = pd.read_csv('products.csv')

# Initialize classes & subclasses 
class Product:
    def __init__(self, name, product_code, calories, expiry_days, quantity=1, owner=None):
        self.name = name
        self.product_code = product_code
        self.calories = calories
        self.expiry_days = expiry_days
        self.quantity = quantity
        self.owner = owner  # Added owner attribute

class ApartmentFridge:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.owner not in self.products:
            self.products[product.owner] = []
        if len(self.products[product.owner]) < 10:  # Assuming each fridge can hold up to 10 products
            self.products[product.owner].append(product)
            print(f"{product.name} added to the {product.owner}'s fridge.")
        else:
            print(f"The {product.owner}'s fridge is full!")

    def display_fridge_contents(self):
        for owner, products in self.products.items():
            print(f"Owner: {owner}")
            for product in products:
                print(f" - {product.name} ({product.quantity} pieces)")

# ... [Rest of your existing code up to the end of streamlit buttons]

# Save data to an Excel file
def save_to_excel(data, file_name='inventory.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)

# End of Streamlit app - call save_to_excel with inventory_list or other data
save_to_excel(st.session_state.inventory_list)

# ... [Rest of your existing code]

# Note: This code assumes that the rest of your Streamlit app and logic is correctly implemented.
