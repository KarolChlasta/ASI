import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tools.datasource import get_training_data
from tools.analyze_data import analyze_factors, get_model_insights

def load_data():
    return pd.DataFrame(get_training_data())

def exec():
    data = load_data()

    if st.sidebar.checkbox('Show Class Distribution', key='class_distribution'):
        potable = data[data['Potability'] == 1]
        non_potable = data[data['Potability'] == 0]
        st.bar_chart({'Potable': len(potable), 'Non-Potable': len(non_potable)})

    if st.sidebar.checkbox('Show Class Distribution', key='factors_analysis'):
        potable = data[data['Potability'] == 1]
        non_potable = data[data['Potability'] == 0]
        st.bar_chart({'Potable': len(potable), 'Non-Potable': len(non_potable)})

    if st.sidebar.checkbox('Show Factors Analysis', key='correlation_matrix'):
        # Assuming you have a function to perform the analysis
        important_factors = analyze_factors(data)
        st.bar_chart(important_factors)

    if st.sidebar.checkbox('Show Correlation Matrix', key='model_insights'):
        corr_matrix = data.corr()
        plt.figure(figsize=(10, 10))
        sns.heatmap(corr_matrix, annot=True)
        st.pyplot(plt)

    # if st.sidebar.checkbox('Show Model Insights', key='missing_data'):
    #     # Assuming you have a model and a function to interpret its decisions
    #     model_insights = get_model_insights(data)
    #     st.write(model_insights)

    if st.sidebar.checkbox('Show Missing Data', ):
        missing_data = data.isnull().sum()
        st.bar_chart(missing_data)

