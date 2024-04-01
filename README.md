# Sample MLOps pipeline

Train a simple genre classification model to recognize a song genre basing on it's characteristics. 



## Requirements

1. Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/
2. Weights&Biases: https://docs.wandb.ai/quickstart
   1. Sign-up: https://wandb.ai/login?signup=true
   2. Install: `pip install wandb`
   3. Login from CLI: `wandb login`
3. Mlflow: `pip install mlflow`
   1. in case CLI command  `mlflow run .`  can't find it, install from conda forge as part of `conda.yml`
4. I suggest to:
   1. set-up a dedicated conda environment with e.g.:
      `conda create --name mlops python=3.8 mlflow jupyter pandas matplotlib requests -c conda-forge`
   2. Then, activate it with `conda activate mlops`



## Sample runs

1. To perform a simple, complete run, in terminal (CLI) type
   `mlflow run .`

2. This sample pipeline consists of the following steps (see `config.yaml`, which stores all the Hydra options):

       - 1_download
       - 2_preprocess
       - 3_check_data
       - 4_segregate
       - 5_random_forest
       - 6_evaluate

   To run a specific pipeline phase, type e.g.

   `mlflow run . -P hydra_options="main.execute_steps='1_download,2_preprocess'"`

   That will run only first 2 of these steps.

3. To specify model (random_forest) hyper-parameters from CLI:

   1. single hyper-parameter:
      `mlflow run . -P hydra_options="random_forest_pipeline.random_forest.max_depth=15"`
   2. two values of a single  hyper-parameter:
      `mlflow run . -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=13,15"`
   3. two values of two different  hyper-parameters:
      `mlflow run . -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=15 random_forest_pipeline.random_forest.min_samples_split: 3"`
   4. a range of one single hyper-parameter:
      `mlflow run . -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=(10,20,2)"` < generate a range from 10 to 20 in increments of 2

4. The same as above,, but with joblib launcher to make parallel computations:
`mlflow run . -P hydra_options="hydra/launcher=joblib -m random_forest_pipeline.random_forest.max_depth=13,15"` 
To apply more intelligent grid search, see hydra sweepers: https://hydra.cc/docs/plugins/ax_sweeper/



## MLflow run directly from GitHub

I've made a first release (1.0.0) of this pipeline on GitHub, so you can call it directly from there with:

`mlflow run -v 1.0.0 https://github.com/wodecki/sample_mlops_pipeline`



# Serving the model with MLFlow

## First, download Your model

Download the model to the "model" subdirectory, e.g. with:
`wandb artifact get sample_MLOps_pipeline/model_export:latest --root model`

It downloads:

- conda.yaml
- input_example.json
- MLmodel
- model.pkl

## Online processing

You can serve a model for online inference by using mlflow `models serve`:

`mlflow models serve -m model &`

Mlflow will create a REST API for us that we can interrogate by sending requests to the endpoint (which by default is http://localhost:5000/invocations). For example, we can do this from python like this:

`predictions = requests.post("http://localhost:5000/invocations", json=data)`

Where `data` is a file with samples to predict in a json format. 

## Batch processing

Just run:

`mlflow models predict -t csv -i input.csv -m model`

Where `input.csv` contains samples to predict.





   

   

