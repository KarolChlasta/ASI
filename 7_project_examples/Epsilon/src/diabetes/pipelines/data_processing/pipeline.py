from kedro.pipeline import Pipeline, node, pipeline

from .nodes import download, preprocess, init_wandb


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=download,
                inputs=['params:host','params:database','params:user','params:password'],
                outputs='diabetes_predictions',
                name='download_diabetes_predictions_node'
            ),
            node(
                func=init_wandb,
                inputs='params:configg',
                outputs=None,
                name='init_wandb_diabetes_predictions_node'
            ),
            node(
                func=preprocess,
                inputs=['diabetes_predictions', 'params:random_state', 'params:constring'],
                outputs=['X_train', 'X_test', 'X_validate', 'y_train', 'y_test', 'y_validate'],
                name='preprocess_diabetes_predictions_node'
            )
        ]
    )
