import streamlit as st
import pandas as pd

# New decorator for caching
@st.experimental_memo
def load_data(url):
    return pd.read_csv(url)

# Your public Google Sheet URL here
sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZ1UK4_05AyOBEslc9fbV1zs_7PD40YNJ22847f39SIgLOiKleT70C5HQ--uTjf3-8Afh3NMCG6NsH/pub?output=csv'

# Load the data
data = load_data(sheet_url)

# Display the data in the Streamlit app
st.write(data)
