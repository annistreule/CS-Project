import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the connection to Google Sheets
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("your_google_sheet_name").sheet1

# Get all the records of the data
records = sheet.get_all_records()

# Display the records in the Streamlit app
st.write(records)


