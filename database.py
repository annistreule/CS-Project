import streamlit as st
import pandas as pd

# URL der CSV-Datei
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQZ1UK4_05AyOBEslc9fbV1zs_7PD40YNJ22847f39SIgLOiKleT70C5HQ--uTjf3-8Afh3NMCG6NsH/pub?output=csv'

@st.cache
def load_csv(url):
    # Verwende pandas, um die CSV-Datei direkt aus dem Web zu laden
    return pd.read_csv(url)

def main():
    st.title('CSV-Daten anzeigen')

    # Daten laden
    data = load_csv(CSV_URL)

    # Daten in Streamlit anzeigen
    st.write(data)

if __name__ == "__main__":
    main()
