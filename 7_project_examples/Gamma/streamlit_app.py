import streamlit as st
import pandas as pd
from pathlib import Path
import requests

PREDICT = "http://localhost:8000/predict"
RUN = "http://localhost:8000/run"
SYNTHETIC = "http://localhost:8000/synthetic"

st.title('Aplikacja Streamlit do Uruchamiania Potoków Kedro')

if st.button('Uruchom Potok Kedro'):
    response = requests.get(RUN)
    st.success('Potok został uruchomiony!')
    if response.status_code == 200:
        st.success('Potok został wykonany!')
    else:
        st.error("Błąd podczas wykonywania uruchamiania potoku")

if st.button('Wygeneruj dane syntetyczne'):
    response = requests.get(SYNTHETIC)
    if response.status_code == 200:
        st.success('Poprawnie wygenerowano dane!')
        data = response.json()
        synthetic_data = pd.read_json(data['synthetic'])
        st.dataframe(synthetic_data)
    else:
        st.error('Nie udało się wygenerować danych!')
        st.write(response)

with st.form(key='predict_form'):
    name = st.text_input('name', value="")
    distance = st.text_input('distance', value="")
    stellar_magnitude = st.text_input('stellar_magnitude', value="")
    discovery_year = st.text_input('discovery_year', value="")
    mass_multiplier = st.text_input('mass_multiplier', value="")
    mass_wrt = st.text_input('mass_wrt', value="")
    radius_multiplier = st.text_input('radius_multiplier', value="")
    radius_wrt = st.text_input('radius_wrt', value="")
    orbital_radius = st.text_input('orbital_radius', value="")
    orbital_period = st.text_input('orbital_period', value="")
    eccentricity = st.text_input('eccentricity', value="")
    detection_method = st.text_input('detection_method', value="")
    submit_button = st.form_submit_button('Wykonaj Predykcję')

if submit_button:

    # Przygotowanie danych do predykcji
    data_to_predict = {
        'name': name,
        'distance': distance,
        'stellar_magnitude': stellar_magnitude,
        'discovery_year': discovery_year,
        'mass_multiplier': mass_multiplier,
        'mass_wrt': mass_wrt,
        'radius_multiplier': radius_multiplier,
        'radius_wrt': radius_wrt,
        'orbital_radius': orbital_radius,
        'orbital_period': orbital_period,
        'eccentricity': eccentricity,
        'detection_method': detection_method
    }
    print(data_to_predict)

    # Wysyłanie żądania do FastAPI
    response = requests.post(PREDICT, json=data_to_predict)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Wynik Predykcji: {prediction}")
    else:
        st.error("Błąd podczas wykonywania predykcji")