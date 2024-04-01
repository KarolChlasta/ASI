import streamlit as st
import pandas as pd
from tools.clean_method import *


def show_clean_page():
    # Sidebar - Cleaning options
    plot_type = st.sidebar.radio("Choose the type of plot:",
                                 ('Histogram', 'Scatter Plot'))

    st.sidebar.header('Cleaning Options')
    cleaning_method = st.sidebar.radio("Select the cleaning method:",
                                       ('avg', 'iter', 'knn', 'tidy'))  # Add more methods as needed

    df: pd.DataFrame = raw_data()
    df_cleaned: pd.DataFrame = df.copy()

    if cleaning_method == 'avg':
        df_cleaned = clean_method_avg()
    elif cleaning_method == 'iter':
        df_cleaned = clean_method_iter()
    elif cleaning_method == 'knn':
        df_cleaned = clean_method_knn()
    elif cleaning_method == 'tidy':
        df_cleaned = clean_method_tidy()

    # Main area
    st.title('Comparing Data Cleaning Methods')

    import tools.charts as charts

    if plot_type == 'Histogram':
        charts.histogram(df, df_cleaned, cleaning_method)
    elif plot_type == 'Scatter Plot':
        charts.scatter_plot(df, df_cleaned, cleaning_method)
