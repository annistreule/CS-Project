import streamlit as st
import pandas as pd

# The URL of your public Google Sheet, make sure it's shared as "Anyone with the link can view"
sheet_url = 'https://docs.google.com/spreadsheets/d/1CLDAFhtriXEMnylxTfOqF27-GH5S9hXELq0WCl-8kb4/edit?usp=sharing'

# Use the pandas library to read the csv data from the Google Sheet
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(sheet_url)

# Display the dataframe in the Streamlit app
st.write(data)



