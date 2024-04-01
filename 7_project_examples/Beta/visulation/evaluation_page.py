import pandas as pd

import streamlit as st

def execute(
        # accuracy,
        # precision,
        # recall,
        # f1,
        evaluation_metrics: dict,
        confusion_matrix: dict
):
    print(confusion_matrix, evaluation_metrics)
    st.title("Evaluation Metrics")

    # Display Evaluation Data
    st.write("### Evaluation Data")
    st.markdown(pd.DataFrame(confusion_matrix).style.hide(axis="index").to_html(), unsafe_allow_html=True)

    metrics_df = pd.DataFrame(evaluation_metrics)

    st.write("### Evaluation Metrics")
    st.markdown(pd.DataFrame(metrics_df).style.hide(axis="index").to_html(), unsafe_allow_html=True)
