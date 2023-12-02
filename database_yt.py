import streamlit as st
import pandas as pd

# The URL of your public Google Sheet, make sure it's shared as "Anyone with the link can view"
sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZ1UK4_05AyOBEslc9fbV1zs_7PD40YNJ22847f39SIgLOiKleT70C5HQ--uTjf3-8Afh3NMCG6NsH/pub?output=csv'

# Use the pandas library to read the csv data from the Google Sheet
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(sheet_url)

# Display the dataframe in the Streamlit app
st.write(data)



