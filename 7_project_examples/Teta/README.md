# ASI Project - Group 1

## Overview

This project focuses on exploring capabilities of various AI tools such as creating synthetic data, AutoML, Evaluation and Deployement.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/karolpj/asi_group1.git
```

2. Set up a virtual environment (optional but recommended):

MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Weights&Biases

```bash
wandb init
```

5. FastAPI backend

```bash
cd ./fastpi & uvicorn main:app
```

6. Kedro viz

```bash
cd ./mushrooms & kedro viz
```

7. Run streamlit app

```bash
streamlit run ./streamlit_app.py
```

## Dataset

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy. [source: Kaggle]
[https://www.kaggle.com/datasets/uciml/mushroom-classification]([https://www.kaggle.com/datasets/uciml/mushroom-classification)

## Stack

- **SDV**: synthetic data
- **AutoGluon**: training and choosing best model
- **Kedro**: pipeline
- **Weights&Biases**: evaluation
- **Streamlit**: deployment
