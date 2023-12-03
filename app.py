import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets Authentifizierungs-Scope
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Pfad zu deiner JSON-Anmeldedatei
# Stelle sicher, dass dieser Pfad auch in deinem Deployment-Umfeld gültig ist.
# Wenn du in einer Cloud-Umgebung arbeitest, solltest du diese Datei sicher speichern und
# auf die Credentials über Umgebungsvariablen oder einen anderen sicheren Weg zugreifen.
SERVICE_ACCOUNT_FILE = '/Users/Anina/Desktop/CS/Project/Anina/CS-Project-main/projekt-cs-32b2fba1e1ff.json'

# Funktion, um die Credentials zu erstellen und den Google Sheets Client zu autorisieren
def authenticate_gspread():
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    gc = gspread.authorize(credentials)
    return gc

# Funktion, um Daten von Google Sheets zu laden
def load_data_from_sheet(sheet_name, worksheet_name):
    gc = authenticate_gspread()
    worksheet = gc.open(database_A).worksheet(database_A)
    data = pd.DataFrame(worksheet.get_all_records())
    return data

# Hauptfunktion deiner Streamlit App
def main():
    st.title('Google Sheets in Streamlit')
    
    # Name deines Google Sheets und des Arbeitsblatts
    sheet_name = 'Database_A'
    worksheet_name = 'Database_A'
    
    # Lade die Daten
    data = load_data_from_sheet(sheet_name, worksheet_name)
    
    # Zeige die Daten in Streamlit an
    st.write(data)

# Führe die Hauptfunktion aus
if __name__ == "__main__":
    main()
