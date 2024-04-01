import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from tools.clean_method import raw_data

def show_none_value_page():
    df = raw_data()
    df = df.drop(columns=['Potability'])
    # Main area
    st.title('Visualization of Empty Cells in Dataset')

    # Count the number of empty cells (NaN values) in each column
    missing_values = df.isnull().sum()
    total_rows = df.shape[0]

    # Create a bar chart if there are columns in the dataset
    if len(df.columns) > 0:
        st.write("Bar chart of missing values in each column:")
        fig, ax = plt.subplots()
        bars = missing_values.plot(kind='bar', color='skyblue', ax=ax)
        plt.ylabel('Number of Missing Values')
        plt.xlabel('Columns')
        plt.title('Number of Missing Values in Each Column')

        # Annotate the bar chart with exact counts
        for bar in bars.patches:
            ax.annotate(format(bar.get_height(), '.0f'),
                        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha='center', va='center',
                        xytext=(0, 5),
                        textcoords='offset points')

        st.pyplot(fig)

        st.write("Number of all columns: ", df.shape[0])

        # Calculate the percentage of missing values
        missing_percentage = (missing_values / total_rows) * 100

        # Create a bar chart and summary if there are columns in the dataset
        if len(df.columns) > 0:
            # ... [previous bar chart code] ...

            # Show summary of missing values with percentage
            st.write("Summary of missing values per column:")

            # Create a summary DataFrame
            summary_df = pd.DataFrame({
                'Missing Values': missing_values,
                'Percentage': missing_percentage
            })

            # Formatting the 'Percentage' column to show up to 2 decimal places
            summary_df['Percentage'] = summary_df['Percentage'].map('{:,.2f}%'.format)

            # Display the summary DataFrame
            st.write(summary_df)
        else:
            st.write("The dataset has no columns.")

        # Show information about all columns
        st.write("Information about all columns:")
        st.write(df.describe(include='all'))
    else:
        st.write("The dataset has no columns.")
