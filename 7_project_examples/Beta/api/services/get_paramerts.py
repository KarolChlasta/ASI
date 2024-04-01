import yaml
from config.env import settings as env
from model.parameters import Parameters


def execute() -> Parameters:
    model = Parameters()

    with open(env.kedro_parameters_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        config = config['model_parameters']

    attr = list(filter(lambda x: not x.startswith('__'), dir(model)))

    for key in attr:
        # not perfect, but works
        if key in config:
            setattr(model, key, config[key])

    return model
