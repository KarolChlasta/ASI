import os
from api import UploadFile
from services.cli import run_commands

def update_file(file: UploadFile, path: str):
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())


def if_file_exist(dataset_path: str) -> bool:
    return os.path.isfile(dataset_path)


def download_dataset(env_name: str, dataset_path: str, file_name: str):
    run_commands(
        f"conda activate {env_name}",
        r'cd ..\temp',
        f'kaggle datasets download -d {dataset_path}',
        f'Expand-Archive -Path "{file_name}.zip" -DestinationPath "{file_name}"',
        f'move .\\{file_name}.csv ..\\asi-kedro\\data\\01_raw\\{file_name}.csv'
    )
