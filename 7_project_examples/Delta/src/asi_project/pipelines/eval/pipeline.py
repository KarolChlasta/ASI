"""
This is a boilerplate pipeline 'eval'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import eval_model, log_results

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
          node(
                func=eval_model,
                inputs=['classifier',"test_dataset"],
                outputs=[ 'y_test', 'y_pred', 'y_probas'],
                name="eval_model_node",
            ),
        node(
                func=log_results,
                inputs=['y_test', 'y_pred', 'y_probas',"params:model_options", 'classifier'],
                outputs=None,
                name="log_results_node",
            )




    ])
