from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train", "params:model_params"],
                outputs="predictor",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["predictor", "X_test", "y_test", "params:model_params"],
                outputs=None,
                name="evaluate_model_node",
            ),
        ]
    )
