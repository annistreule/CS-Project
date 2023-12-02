import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ... (Der Teil mit den Credentials und dem Öffnen des Sheets bleibt gleich)

# Dekorator für Caching
@st.experimental_memo(ttl=60)  # Zeit in Sekunden, nach der der Cache erneuert wird
def load_data():
    # Holen Sie sich alle Daten aus dem ersten Blatt Ihrer Tabelle als DataFrame
    sheet = client.open('Database_a').sheet1
    data = pd.DataFrame(sheet.get_all_records())
    return data

data = load_data()

# Zeigt die Daten in der Streamlit-App an
st.write(data)

# ... (Der Teil mit der Eingabe und den Schaltflächen bleibt gleich)

# Anstelle von 'sheet.append_row([...])' und 'sheet.delete_row(row_count)'
# werden Sie Ihren Code mit 'data = load_data()' nach jeder Änderung aktualisieren

if st.button('Add Product'):
    # ... (Überprüfungslogik bleibt gleich)
    sheet.append_row([product_name, expire_date])
    data = load_data()  # Daten neu laden
    st.write(data)  # Daten anzeigen

if st.button('Remove Last Product'):
    # ... (Logik zum Entfernen bleibt gleich)
    sheet.delete_row(row_count)
    data = load_data()  # Daten neu laden
    st.write(data)  # Daten anzeigen
