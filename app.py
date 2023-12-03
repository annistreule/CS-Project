import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets Authentifizierungs-Scope
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Pfad zu deiner JSON-Anmeldedatei in der Cloud-Umgebung
# Dieser Pfad muss für deine Cloud-Umgebung gültig sein.
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
    worksheet = gc.open(sheet_name).worksheet(worksheet_name)
    data = pd.DataFrame(worksheet.get_all_records())
    return data

# Hauptfunktion deiner Streamlit App
def main():
    st.title('Google Sheets in Streamlit')
    
    # Name deines Google Sheets und des Arbeitsblatts
    sheet_name = 'Database_A'  # Ersetze dies mit dem tatsächlichen Namen deines Sheets
    worksheet_name = 'Sheet1'  # Ersetze dies mit dem tatsächlichen Namen deines Arbeitsblatts
    
    # Lade die Daten
    data = load_data_from_sheet(sheet_name, worksheet_name)
    
    # Zeige die Daten in Streamlit an
    st.write(data)

# Führe die Hauptfunktion aus
if __name__ == "__main__":
    main()
