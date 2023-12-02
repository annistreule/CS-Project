streamlit as st
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

# Dekorator für Caching
@st.experimental_memo
def load_data(sheet):
    # Holen Sie sich alle Daten aus dem ersten Blatt Ihrer Tabelle als DataFrame
    data = pd.DataFrame(sheet.get_all_records())
    return data

# Lädt die Daten
data = load_data(sheet)

# Zeigt die Daten in der Streamlit-App an
st.write(data)

# Felder für die Eingabe neuer Produktinformationen
product_name = st.text_input('Product Name')
expire_date = st.text_input('Expire Date')

# Schaltfläche zum Hinzufügen neuer Daten
if st.button('Add Product'):
    # Überprüfen Sie, ob die Felder ausgefüllt sind
    if product_name and expire_date:
        # Fügt die neuen Daten am Ende des Sheets hinzu
        sheet.append_row([product_name, expire_date])
        st.experimental_memo.clear() # Cache löschen, damit die Daten neu geladen werden
        st.success('Product added successfully!')
        data = load_data(sheet) # Daten neu laden
        st.write(data) # Daten anzeigen
    else:
        st.error('Please fill out all fields')

# Schaltfläche zum Entfernen des letzten Produkts
if st.button('Remove Last Product'):
    # Anzahl der Zeilen im Sheet
    row_count = len(data.index) + 1  # +1, weil sheet.get_all_records() die Kopfzeile nicht zählt
    # Entfernt die letzte Zeile aus dem Sheet
    if row_count > 1:  # Verhindert das Löschen der Kopfzeile
        sheet.delete_row(row_count)
        st.experimental_memo.clear() # Cache löschen, damit die Daten neu geladen werden
        st.success('Last product removed successfully!')
        data = load_data(sheet) # Daten neu laden
        st.write(data) # Daten anzeigen
    else:
        st.error('No products to remove')
