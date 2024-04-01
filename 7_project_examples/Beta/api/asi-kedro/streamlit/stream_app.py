import streamlit as st

pages = st.sidebar.radio("Choose pages:", ('None value', 'Clean Page', 'Wandb Page'))

if pages == 'None value':
    import none_value_page
    none_value_page.show_none_value_page()
elif pages == 'Clean Page':
    import clean_page
    clean_page.show_clean_page()
elif pages == 'Wandb Page':
    import wandb_page
    wandb_page.execute()