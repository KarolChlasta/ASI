import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


def histogram(df, df_cleaned, cleaning_method):
    column = st.sidebar.selectbox('Select column to visualize', df.columns)

    # Create a single figure and axes
    fig, ax = plt.subplots()

    # Plot density of the original data
    sns.kdeplot(df[column].dropna(), ax=ax, shade=True, color='blue', label=f'Before {cleaning_method}', alpha=0.5)

    # Plot density of the cleaned data
    sns.kdeplot(df_cleaned[column].dropna(), ax=ax, shade=True, color='red', label=f'After {cleaning_method}',
                alpha=0.5)

    # Add legend, labels, and a grid for better readability
    ax.legend()
    ax.set_title(f'Density Plot of {column} before and after {cleaning_method}')
    ax.set_xlabel(column)
    ax.set_ylabel('Density')
    ax.grid(True)

    # Display the combined plot
    st.pyplot(fig)

    # ----------------------


    # column = st.sidebar.selectbox('Select column to visualize', df.columns)
    #
    # st.write(f"Histogram of {column} before cleaning")
    # fig, ax = plt.subplots()
    # df[column].hist(ax=ax, bins=20, alpha=0.5, color='blue')
    # st.pyplot(fig)
    #
    # st.write(f"Histogram of {column} after applying {cleaning_method}")
    # fig, ax = plt.subplots()
    # df_cleaned[column].hist(ax=ax, bins=20, alpha=0.5, color='red')
    # st.pyplot(fig)


def scatter_plot(df, df_cleaned, cleaning_method):
    # Let the user choose two columns to compare
    x_column = st.sidebar.selectbox('X-axis', df.columns)
    y_column = st.sidebar.selectbox('Y-axis', df.columns)

    st.write(f"Scatter plot of {x_column} vs {y_column} before cleaning")
    fig, ax = plt.subplots()
    df.plot(kind='scatter', x=x_column, y=y_column, ax=ax, alpha=0.5, color='blue')
    st.pyplot(fig)

    st.write(f"Scatter plot of {x_column} vs {y_column} after applying {cleaning_method}")
    fig, ax = plt.subplots()
    df_cleaned.plot(kind='scatter', x=x_column, y=y_column, ax=ax, alpha=0.5, color='red')
    st.pyplot(fig)


def line_plot(df, df_cleaned, cleaning_method):
    # Assuming your dataset has a 'date' or similar time-related column
    time_column = 'date'  # Replace with your actual time column
    value_column = st.sidebar.selectbox('Value column', df.columns)

    st.write(f"Line plot of {value_column} over time before cleaning")
    fig, ax = plt.subplots()
    df.plot(kind='line', x=time_column, y=value_column, ax=ax, alpha=0.5, color='blue')
    st.pyplot(fig)

    st.write(f"Line plot of {value_column} over time after applying {cleaning_method}")
    fig, ax = plt.subplots()
    df_cleaned.plot(kind='line', x=time_column, y=value_column, ax=ax, alpha=0.5, color='red')
    st.pyplot(fig)

def show_empty(df):
    # Main area
    st.title('Visualization of Empty Cells in Dataset')

    # Visualize missing data
    st.write("Heatmap of empty cells (NaN values)")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
    st.pyplot()

    # Show summary of missing values
    if df.isnull().values.any():
        st.write("Summary of missing values per column:")
        missing_counts = df.isnull().sum()
        st.write(missing_counts)
