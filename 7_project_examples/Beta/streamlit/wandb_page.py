def execute():
    import streamlit as st
    import wandb

    # Authenticate (this will require you to log in once if you haven't)
    wandb.login(key="1b0161175b83d48975e0ba2c1b7a024965423bd4")

    # Use the Wandb API to pull data
    api = wandb.Api()

    # Streamlit interface
    st.title('Streamlit + Wandb Integration')

    # User inputs for project and entity
    entity = st.text_input('Enter Wandb Entity', value='bartek09797')
    project = st.text_input('Enter Wandb Project Name', value='Kedro-ASI-Test-Autogluon')

    if entity and project:
        # Fetch runs from the specified project
        api = wandb.Api()
        runs = api.runs(f"{entity}/{project}")

        # Iterate over each run and display information
        for run in runs:
            with st.expander(f"Run: {run.name}"):
                st.write("Description:", run.description)
                st.write("Tags:", run.tags)
                st.write("URL:", run.url)
                st.write("ID:", run.id)
                st.write("State:", run.state)
                st.write("Created at:", run.created_at)

                # System metrics
                st.subheader("System Metrics")
                st.json(run.system_metrics)

                # Summary metrics
                st.subheader("Summary Metrics")
                st.json(run.summary)

                # Configuration details
                st.subheader("Configuration")
                st.json(run.config)

                # Add any other desired run details here

