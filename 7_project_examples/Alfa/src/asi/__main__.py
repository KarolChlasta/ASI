"""ASI file for ensuring the package is executable
as `asi` and `python -m asi`
"""
import importlib
import pickle

import requests
import streamlit as st
from pathlib import Path

# from kedro.framework.cli.utils import KedroCliError, load_entry_points
# from kedro.framework.project import configure_project

def _find_run_command(package_name):
    try:
        project_cli = importlib.import_module(f"{package_name}.cli")
        # fail gracefully if cli.py does not exist
    except ModuleNotFoundError as exc:
        if f"{package_name}.cli" not in str(exc):
            raise
        plugins = load_entry_points("project")
        run = _find_run_command_in_plugins(plugins) if plugins else None
        if run:
            # use run command from installed plugin if it exists
            return run
        # use run command from `kedro.framework.cli.project`
        from kedro.framework.cli.project import run

        return run
    # fail badly if cli.py exists, but has no `cli` in it
    if not hasattr(project_cli, "cli"):
        raise KedroCliError(f"Cannot load commands from {package_name}.cli")
    return project_cli.run


def _find_run_command_in_plugins(plugins):
    for group in plugins:
        if "run" in group.commands:
            return group.commands["run"]


def main(*args, **kwargs):
    # package_name = Path(__file__).parent.name
    # configure_project(package_name)
    # run = _find_run_command(package_name)
    # run(*args, **kwargs)
    overview = st.container()
    left, center, right = st.columns(3)
    prediction = st.container()

    with overview:
        st.title("Rain prediction app")

    with left:
        minTemp_slider = st.slider("Min temperature", min_value=-10, max_value=50, step=1)
        maxTemp_slider = st.slider("Max temperature", min_value=-10, max_value=50, step=1)
        rainfall_slider = st.slider("Rainfall", min_value=0, max_value=400, step=1)
        evaporation_slider = st.slider("Evaporation", min_value=0, max_value=150, step=1)
        sunshine_slider = st.slider("Sunshine", min_value=0, max_value=15, step=1)
        windGustSpeed_slider = st.slider("Wind gust speed", min_value=0, max_value=140, step=1)
        windSpeed9am_slider = st.slider("Wind speed at 9am", min_value=0, max_value=140, step=1)
        windSpeed3pm_slider = st.slider("Wind speed at 3am", min_value=0, max_value=140, step=1)

    with center:
        humidity9am_slider = st.slider("Humidity at 9am", min_value=0, max_value=100, step=1)
        humidity3pm_slider = st.slider("Humidity at 3pm", min_value=0, max_value=100, step=1)
        pressure9am_slider = st.slider("Pressure at 9am", min_value=970, max_value=1050, step=1)
        pressure3pm_slider = st.slider("Pressure at 3pm", min_value=970, max_value=1050, step=1)
        cloud9am_slider = st.slider("Cloudiness at 9am", min_value=0, max_value=10, step=1)
        cloud3pm_slider = st.slider("Cloudiness at 3pm", min_value=0, max_value=10, step=1)
        temp9am_slider = st.slider("Temperature at 9am", min_value=-10, max_value=50, step=1)
        temp3pm_slider = st.slider("Temperature at 3pm", min_value=-10, max_value=50, step=1)

    with right:
        location = st.selectbox('Select city', ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
           'Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond',
           'Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown',
           'Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat',
           'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura',
           'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
           'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
           'Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport',
           'Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston',
           'AliceSprings', 'Darwin', 'Katherine', 'Uluru'])
        windGustDir = st.selectbox("Select wind direction", ['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE',
           'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW'])
        windDir9am = st.selectbox("Select wind direction at 9am", ['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE',
           'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW'])
        windDir3pm = st.selectbox("Select wind direction at 3pm",
                                  ['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW', 'ENE',
                                   'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW'])
        rainToday = st.selectbox("Select if rain today", ["Yes", "No"])

    st.subheader("Will it rain in Australia?")

    if (st.button("Predict")):
        res = requests.get(url="http://localhost:8000/my_model?Location={}&MinTemp={}&MaxTemp={}&Rainfall={}&"
                               "Evaporation={}&Sunshine={}&WindGustDir={}&WindGustSpeed={}&WindDir9am={}&WindDir3pm={}&"
                               "WindSpeed9am={}&WindSpeed3pm={}&Humidity9am={}&Humidity3pm={}&Pressure9am={}&"
                               "Pressure3pm={}&Cloud9am={}&Cloud3pm={}&Temp9am={}&Temp3pm={}&RainToday={}"
                           .format(location, minTemp_slider, maxTemp_slider, rainfall_slider, evaporation_slider,
                                   sunshine_slider, windGustDir, windGustSpeed_slider, windDir9am, windDir3pm,
                                   windSpeed9am_slider, windSpeed3pm_slider, humidity9am_slider, humidity3pm_slider,
                                   pressure9am_slider, pressure3pm_slider, cloud9am_slider, cloud3pm_slider,
                                   temp9am_slider, temp3pm_slider, rainToday))

        st.subheader(res.json()["0"])


if __name__ == "__main__":
    main()
