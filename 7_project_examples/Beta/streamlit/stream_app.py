import streamlit as st

pages = st.sidebar.radio("Choose pages:", ('Synth Data', 'None value', 'Clean Page', 'Wandb Page', 'Raw Data'))

if pages == 'None value':
    import none_value_page
    none_value_page.show_none_value_page()
elif pages == 'Wandb Page':
    import wandb_page
    wandb_page.execute()
elif pages == 'Raw Data':
    import raw_data_page
    raw_data_page.execute()
elif pages == 'Synth Data':
    import synth_data_page
    synth_data_page.execute()