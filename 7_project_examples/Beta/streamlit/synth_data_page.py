import streamlit as st
import requests
import pandas as pd

from sdv.evaluation.single_table import run_diagnostic, evaluate_quality, get_column_plot
from sdv.metadata import SingleTableMetadata

def execute():
    response_synth = requests.get("http://localhost:8000/synth_data")
    response_raw = requests.get("http://localhost:8000/raw_data")

    if response_synth.status_code == 200 and response_raw.status_code == 200:
        raw_data_json = response_raw.json()
        synth_data_json = response_synth.json()
        raw_data = pd.DataFrame(raw_data_json)
        synth_data = pd.DataFrame(synth_data_json)

        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(raw_data)
        columns_dict = metadata.to_dict()['columns']

        diagnostic = run_diagnostic(raw_data, synth_data, metadata)
        quality_report = evaluate_quality(raw_data, synth_data, metadata)

        st.subheader('Data Validity')
        st.write(diagnostic.get_details(property_name='Data Validity'))
        st.subheader('Column Shapes')
        st.write(quality_report.get_details(property_name='Column Shapes'))
        st.subheader('Column Pair Trends')
        st.write(quality_report.get_details(property_name='Column Pair Trends'))
        with st.expander('Column plots'):
            if st.button('Draw plots'):
                for key in columns_dict.keys():
                    if key is not None and key != 'Potability':
                        fig = get_column_plot(
                            real_data=raw_data,
                            synthetic_data=synth_data,
                            metadata=metadata,
                            column_name=key
                        )
                        fig.update_layout(
                            plot_bgcolor='black' 
                        )
                        if fig is not None:
                            st.plotly_chart(fig)

    else:
        st.error(f"Error fetching data. Status code: {response_raw.status_code}")
        st.error(f"Error fetching data. Status code: {response_synth.status_code}")
