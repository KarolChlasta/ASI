# ASI_Grupa3
## Dataset Banck Churn

![diagram](https://github.com/BrunoKedzierski/MLOPS-Project/assets/40804691/08b0b1bb-37f1-4a1e-b7c0-26231a8f3bde)


1. Install conda fromhttps://docs.conda.io/projects/miniconda/en/latest/

2. Open cmd and go to the catalog with this project inside.
conda env create -f environment.yml

3. run python launcher.py script from command line

4. Streamlit app will be open in browser on URL http://localhost:8001/ and you will be able to manage software from this web panel.




Technologies:
- Python : all informations are in environment.yml file for conda. Below are also some of the most important python packages.
	- fastapi - exchanging informations with server
	- kedro - way of managing machine learning model. https://kedro.org/
	- kedro-viz - It visualises the pipelines in a Kedro project by showing data, nodes, and the connections between them.
	- sdv -python framework created to generate synthetic data.
	- streamlit for web panel to change learning parameters and to test results.
	- pandas - managing dataframes
	- fastAPI - web framework for building APIs with Python 3.8+ based on standard Python type hints.

- Wandb : website for creating and managing machine learning models. We use it also as database. The URL of our project is https://wandb.ai/asi_grupa_3
	  ask your supervisor to get added to team or to access the token.
 
