import yaml

from config import env
from model.parameters import Parameters
import services.get_paramerts as get_paramerts


def execute(webModel):
    model = get_paramerts.execute()

    attr = vars(webModel)

    data = {"model_parameters": {}}
    for key in attr:
        value = getattr(webModel, key)
        old_value = getattr(model, key)

        if value is not None:
            data["model_parameters"][key] = value
        else:
            data["model_parameters"][key] = old_value

    with open(env.KEDRO_PARAMETERS_PATH, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    return data

