import os.path

from dotenv import load_dotenv
from pydantic import FilePath
from pydantic_settings import BaseSettings

env_path = '.env'
local_env_path = '.env_local'

if os.path.isfile(local_env_path):
    env_path = local_env_path

load_dotenv(env_path)


class Setting(BaseSettings):
    app_name: str = ""
    wandb_api_key: str = None  # Set to the type you expect, str is just an example
    dataset_path: str = ""
    kaggle_dataset_path: str = ""
    local_dataset_path: str = ""
    conda_kedro_env: str = ""
    kedro_parameters_path: str = ""

    # TODO: Define the logic or usage for these later
    zip_dataset_name: str = ""
    dataset_name: str = ""

    class Config:
        # Configuration class meta-data (e.g., where to load the variables from)
        env_file = "default.env"
        env_prefix = ""


# Creating an instance of the settings
settings = Setting()

