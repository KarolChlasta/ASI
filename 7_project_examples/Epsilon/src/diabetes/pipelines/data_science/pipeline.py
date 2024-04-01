from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model, predict, save_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_model,
                inputs=["X_train", "y_train",'params:model_type','params:hyperparameters'],
                outputs="regressor",
                name="create_model_node",
            ),
            node(
                func=predict,
                inputs=["X_validate", "y_validate", "regressor"],
                outputs="accuracy",
                name="predict_node",
            ),
            node(
                func=save_model,
                inputs=["regressor"],
                outputs=None,
                name="save_model_node",
            ),
        ]
    )
