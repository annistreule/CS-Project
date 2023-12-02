import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Stellen Sie den Umfang der API ein
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

# Pfad zu Ihrer JSON-Anmeldedatei
creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/Anina/Desktop/CS/Project/Anina/CS-Project-main/projekt-cs-32b2fba1e1ff.json', scope)

# Autorisieren Sie sich mit den Anmeldedaten
client = gspread.authorize(creds)

# Öffnen Sie das Google Sheet mit seinem Namen oder seiner ID
sheet = client.open('Database_a').sheet1

# Dekorator für Caching mit einem Zeitlimit (ttl)
@st.experimental_memo(ttl=300)  # Daten alle 5 Minuten aktualisieren
def load_data():
    # Holen Sie sich alle Daten aus dem ersten Blatt Ihrer Tabelle als DataFrame
    sheet = client.open('Database_a').sheet1
    data = pd.DataFrame(sheet.get_all_records())
    return data

# Lädt die Daten und zeigt sie an
data = load_data()
st.write(data)

# Felder für die Eingabe neuer Produktinformationen
product_name = st.text_input('Product Name')
expire_date = st.text_input('Expire Date')

# Schaltfläche zum Hinzufügen neuer Daten
if st.button('Add Product'):
    if product_name and expire_date:
        sheet.append_row([product_name, expire_date])
        st.experimental_memo.clear()  # Cache löschen, damit die Daten neu geladen werden
        st.success('Product added successfully!')
        data = load_data()  # Daten neu laden
        st.write(data)  # Daten anzeigen
    else:
        st.error('Please fill out all fields')

# Schaltfläche zum Entfernen des letzten Produkts
if st.button('Remove Last Product'):
    row_count = len(data.index) + 1
    if row_count > 1:
        sheet.delete_row(row_count)
        st.experimental_memo.clear()  # Cache löschen, damit die Daten neu geladen werden
        st.success('Last product removed successfully!')
        data = load_data()  # Daten neu laden
        st.write(data)  # Daten anzeigen
    else:
        st.error('No products to remove')
