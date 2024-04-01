from kedro.framework.startup import bootstrap_project
from kedro.framework.session import KedroSession
from pathlib import Path


def get_kedro_catalog(project_path: str):
    project_path = Path(project_path)
    metadata = bootstrap_project(project_path)

    with KedroSession.create(metadata.package_name, project_path=project_path) as session:
        context = session.load_context()
        return context.catalog
