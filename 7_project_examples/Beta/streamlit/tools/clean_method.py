from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from pathlib import Path


def get_kedro_catalog(project_path: str):
    project_path = Path(project_path)
    metadata = bootstrap_project(project_path)

    with KedroSession.create(metadata.package_name, project_path=project_path) as session:
        context = session.load_context()
        return context.catalog


catalog = get_kedro_catalog(r'C:\Users\Admin\Dropbox\Komputer\Documents\DoSzkoly\ASI\kedroApi__asi\asi-kedro')

def raw_data():
    return catalog.load("raw_data")

# Cleaning functions
def clean_method_avg():
    return catalog.load("filled_data_avg")


def clean_method_iter():
    return catalog.load("filled_data_iter")


def clean_method_knn():
    return catalog.load("filled_data_knn")


def clean_method_tidy():
    return catalog.load("filled_data_tidy")
