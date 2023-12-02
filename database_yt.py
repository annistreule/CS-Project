import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

key=AIzaSyCBWuNZ0lgRSw-bHFBh9-UIn3WazAkWrvA

# Stellen Sie den Umfang der API ein
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# Pfad zu Ihrer JSON-Anmeldedatei
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials.json', scope)

# Autorisieren Sie sich mit den Anmeldedaten
client = gspread.authorize(creds)

# Öffnen Sie das Google Sheet mit seinem Namen oder seiner ID
sheet = client.open('https://docs.google.com/spreadsheets/d/e/2PACX-1vQZ1UK4_05AyOBEslc9fbV1zs_7PD40YNJ22847f39SIgLOiKleT70C5HQ--uTjf3-8Afh3NMCG6NsH/pub?output=csv').sheet1

# New decorator for caching
@st.experimental_memo
def load_data(sheet):
    # Holen Sie sich alle Daten aus dem ersten Blatt Ihrer Tabelle als DataFrame
    data = pd.DataFrame(sheet.get_all_records())
    return data

# Lädt die Daten
data = load_data(sheet)

# Zeigt die Daten in der Streamlit-App an
st.write(data)

# Beispiel zum Hinzufügen neuer Daten zu Ihrem Google Sheet
def add_data_to_sheet(new_data):
    # Fügt eine neue Zeile am Ende des Sheets hinzu
    sheet.append_row(new_data)

# Beispiel zum Entfernen von Daten aus Ihrem Google Sheet
def remove_data_from_sheet(row_number):
    # Entfernt eine Zeile aus dem Sheet
    sheet.delete_row(row_number)

# Beispielhafte Nutzung der Funktionen
if st.button('Add new data'):
    add_data_to_sheet(['New Data', 'More Data', 'Another One'])
    
if st.button('Remove last row'):
    all_data = sheet.get_all_values()
    remove_data_from_sheet(len(all_data))

