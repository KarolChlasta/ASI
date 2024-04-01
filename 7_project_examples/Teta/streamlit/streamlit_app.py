import pandas as pd
import requests

import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000/"

cap_shape_values = ["x", "b", "f", "s", "k", "c"]
cap_surface_values = ["s", "y", "f", "g"]
cap_color_values = ["n", "y", "w", "g", "e", "p", "b", "u", "c", "r"]
bruises_values = ["t", "f"]
odor_values = ["p", "a", "l", "n", "f", "c", "y", "s", "m"]
gill_attachment_values = ["f", "a"]
gill_spacing_values = ["c", "w"]
gill_size_values = ["n", "b"]
gill_color_values = ["k", "n", "g", "p", "w", "h", "u", "e", "b", "r", "y", "o"]
stalk_shape_values = ["e", "t"]
stalk_root_values = ["e", "c", "b", "r", "?"]
stalk_surface_above_ring_values = ["s", "f", "k", "y"]
stalk_surface_below_ring_values = ["s", "f", "y", "k"]
stalk_color_above_ring_values = ["w", "g", "p", "n", "b", "e", "o", "c", "y"]
stalk_color_below_ring_values = ["w", "p", "g", "n", "b", "e", "o", "c", "y"]
veil_type_values = ["p"]
veil_color_values = ["w", "n", "o", "y"]
ring_number_values = ["o", "t", "n"]
ring_type_values = ["p", "e", "l", "f", "n"]
spore_print_color_values = ["w", "n", "k", "h", "r", "u", "o", "y", "b"]
population_values = ["v", "y", "s", "n", "a", "c"]
habitat_values = ["d", "g", "p", "l", "u", "m", "w"]

hyperparameters_options = ["default", "light", "very_light", "toy"]
presets_options = [
    "best_quality",
    "high_quality",
    "good_quality",
    "medium_quality",
    "optimize_for_deployment",
]
eval_metric_options = [
    "accuracy",
    "balanced_accuracy",
    "mcc",
    "roc_auc",
    "f1",
]
time_limit_options = [60, 120, 180]


pred = None


def run_kerdo_pipeline(**kwargs):
    requests.get(f"{BACKEND_URL}run_pipeline", params=kwargs)


def get_prediction(data):
    URL = f"{BACKEND_URL}predict"
    resp = requests.post(URL, json=data)


def get_synthetic_data(ammount):
    URL = f"{BACKEND_URL}generate/{ammount}"
    resp = requests.get(URL)
    df = pd.read_json(resp.json())
    return df


def main():
    overview = st.container()
    left, center, right = st.columns(3)
    prediction = st.container()

    with overview:
        st.title("Mushroom edability prediction app")
        st.subheader("Select mushroom features:")

    with left:
        cap_shape_radio = st.selectbox("Select cap shape:", cap_shape_values)
        cap_surface_radio = st.selectbox("Select cap surface:", cap_surface_values)
        cap_color_radio = st.selectbox("Select cap color:", cap_color_values)
        bruises_radio = st.selectbox("Select bruises:", bruises_values)
        odor_radio = st.selectbox("Select odor:", odor_values)
        gill_attachment_radio = st.selectbox(
            "Select gill attachment:", gill_attachment_values
        )
        gill_spacing_radio = st.selectbox("Select gill spacing:", gill_spacing_values)

    with center:
        gill_size_radio = st.selectbox("Select gill size:", gill_size_values)
        gill_color_radio = st.selectbox("Select gill color:", gill_color_values)
        stalk_shape_radio = st.selectbox("Select stalk shape:", stalk_shape_values)
        stalk_root_radio = st.selectbox("Select stalk root:", stalk_root_values)
        stalk_surface_below_ring_radio = st.selectbox(
            "Select stalk surface below ring:", stalk_surface_below_ring_values
        )
        stalk_color_above_ring_radio = st.selectbox(
            "Select stalk color above ring:", stalk_color_above_ring_values
        )
        stalk_color_below_ring_radio = st.selectbox(
            "Select stalk color below ring:", stalk_color_below_ring_values
        )
        veil_type_radio = st.selectbox("Select veil type:", veil_type_values)

    with right:
        stalk_surface_above_ring_radio = st.selectbox(
            "Select stalk surface above ring:", stalk_surface_above_ring_values
        )
        veil_color_radio = st.selectbox("Select veil color:", veil_color_values)
        ring_number_radio = st.selectbox("Select ring number:", ring_number_values)
        ring_type_radio = st.selectbox("Select ring type:", ring_type_values)
        spore_print_color_radio = st.selectbox(
            "Select spore print color:", spore_print_color_values
        )
        population_radio = st.selectbox("Select population:", population_values)
        habitat_radio = st.selectbox("Select habitat:", habitat_values)

    data = {
        "cap_shape": cap_shape_radio,
        "cap_surface": cap_surface_radio,
        "cap_color": cap_color_radio,
        "bruises": bruises_radio,
        "odor": odor_radio,
        "gill_attachment": gill_attachment_radio,
        "gill_spacing": gill_spacing_radio,
        "gill_size": gill_size_radio,
        "gill_color": gill_color_radio,
        "stalk_shape": stalk_shape_radio,
        "stalk_root": stalk_root_radio,
        "stalk_surface_above_ring": stalk_surface_above_ring_radio,
        "stalk_surface_below_ring": stalk_surface_below_ring_radio,
        "stalk_color_above_ring": stalk_color_above_ring_radio,
        "stalk_color_below_ring": stalk_color_below_ring_radio,
        "veil_type": veil_type_radio,
        "veil_color": veil_color_radio,
        "ring_number": ring_number_radio,
        "ring_type": ring_type_radio,
        "spore_print_color": spore_print_color_radio,
        "population": population_radio,
        "habitat": habitat_radio,
    }

    URL = "http://127.0.0.1:8000/predict"
    resp = requests.post(URL, json=data)
    pred = resp.json()

    with prediction:
        st.subheader("Is the mushroom poisonous?")
        st.text("Yes" if pred["prediction"] == 0 else "No")

    st.subheader("Kedro pipeline")
    col_l, col_r = st.columns(2)
    with col_r:
        hyperparameters = st.selectbox("Hyperparameters", hyperparameters_options)
        presets = st.selectbox("Presets", presets_options)
        eval_metric = st.selectbox("Eval metric", eval_metric_options)
        time_limit = st.selectbox("Time limit", time_limit_options)
    extra_params = {
        "hyperparameters": hyperparameters,
        "presets": presets,
        "eval_metric": eval_metric,
        "time_limit": time_limit,
    }
    with col_l:
        st.button(
            "Run Kedro Pipeline", on_click=run_kerdo_pipeline, kwargs=extra_params
        )

        st.link_button("Go to KedroViz", "http://127.0.0.1:4141/")

    st.subheader("Synthetic data generation")
    synthetic_data_ammount = st.number_input(
        "Select synthetic data ammount", min_value=1, step=100, value=100
    )
    if st.button("Generate synthetic data"):
        data = get_synthetic_data(synthetic_data_ammount)
        # run_kerdo_pipeline(**extra_params)
        st.text("Synthetic data sample")
        st.dataframe(data)


if __name__ == "__main__":
    main()
