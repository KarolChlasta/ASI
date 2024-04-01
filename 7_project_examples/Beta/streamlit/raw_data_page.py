import streamlit as st
import requests
import pandas as pd

def execute():
    response = requests.get("http://localhost:8000/raw_data")

    if response.status_code == 200:
        table_data = response.json()
        df = pd.DataFrame(table_data)
        st.dataframe(df)
    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")