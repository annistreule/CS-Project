import streamlit as st
import pandas as pd

# The URL of your public Google Sheet, make sure it's shared as "Anyone with the link can view"
sheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZ1UK4_05AyOBEslc9fbV1zs_7PD40YNJ22847f39SIgLOiKleT70C5HQ--uTjf3-8Afh3NMCG6NsH/pub?output=csv'

# Use the pandas library to read the csv data from the Google Sheet
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(sheet_url)


import time
import streamlit as st 

def load_data(url):
    return pd.read_csv(url)

# Rerun the app every 30 seconds to update the data
st.write(load_data(sheet_url))

# Use Streamlit's session state to store the last rerun time
if 'last_rerun' not in st.session_state or time.time() - st.session_state.last_rerun > 30:
    st.experimental_rerun()
    st.session_state.last_rerun = time.time()



