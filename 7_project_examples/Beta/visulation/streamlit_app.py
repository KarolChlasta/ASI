import time

import streamlit as st
import evaluation_page
from tools.datasource import *
from training_data_page import exec as training_data_page_exce


def raw_data_page():
    st.title("Raw Data")


def evaluation_metrics_page():
    cm = get_confusion_matrix()
    em = get_evaluation_metrics()
    evaluation_page.execute(em, cm)


st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Evaluation Metrics", 'Training Data', "Raw Data"])

if st.sidebar.button("Refresh Data"):
    st.sidebar.success("Data refreshed!")
    time.sleep(0.1)
    st.experimental_rerun()

if page == "Raw Data":
    raw_data_page()
elif page == "Evaluation Metrics":
    evaluation_metrics_page()
elif page == "Training Data":
    training_data_page_exce()

