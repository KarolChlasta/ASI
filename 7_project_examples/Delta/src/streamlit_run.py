
import streamlit as st
import requests
from bank_client import Bank_Client


st.header("Run Kedro Pipeline")
with st.expander("kedro"):
    st.header("Data_Science parameters")
    random_state = st.slider("Select random_state", min_value=1, max_value=10, value=3)
    kernel = st.select_slider("Select kernel", ["linear", "poly", "rbf", "sigmoid"], value="poly")
    rebalance = st.selectbox("Select rebalance:", ["undersampled", "oversampled"])
    model_type = st.selectbox("Select model_type:", ["logistic", "svc", "random_forest"])
    n_estimators = st.slider("Select n_estimators", min_value=100, max_value=500, value=150)

    st.header("Train_Test_Split Parameters")
    test_size = st.slider("Choose test_size:", min_value=0.1, max_value=1.0, value=0.2)
    val_size = st.slider("Choose val_size:", min_value=0.1, max_value=1.0, value=0.2)
    random_state_split = st.slider("Select_random_state", min_value=1, max_value=10, value=3)
    rebalance_split = st.selectbox("Select_rebalance:", ["undersampled", "oversampled"])


    pipeline = st.select_slider("Select pipeline", ["__default__", "dp", "ds","syn"], value="__default__")
    if st.button("Run the pipeline!"):
        with st.spinner("Running pipeline and updating backend..."):
           
                          
            data = {
                 "pipeline" : pipeline,
                "data_science_params": {
                    "random_state": random_state,
                    "kernel": kernel,
                    "rebalance": rebalance,
                    "model_type": model_type,
                    "n_estimators": n_estimators,
                },
                "split_params": {
                    "test_size": test_size,
                    "val_size": val_size,
                    "random_state_split": random_state_split,
                    "rebalance_split": rebalance_split,
                }
            }

            response = requests.post('http://localhost:8001/runpipeline', json=data)
        


st.header("Predict")
with st.expander("Test Specific Results"):
  
    age = st.slider("Choose age:", min_value=0, max_value=100)
    job = st.selectbox("Choose job:",
                       ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin.',
                        'services', 'self-employed', 'unemployed', 'housemaid', 'student'])
    marital = st.selectbox("Choose marital:", ['married', 'single', 'divorced'])
    education = st.selectbox("Choose education:", ['tertiary', 'secondary', 'primary'])
    default = st.selectbox("Choose default:", ["yes", "no"])
    balance = st.slider("Choose balance:", min_value=-8019, max_value=102127)
    housing = st.selectbox("Choose housing:", ["yes", "no"])
    contact = st.selectbox("Choose housing:", ["cellular", "telephone"])
    loan = st.selectbox("Choose loan:", ["yes", "no"])
    day_of_week = st.slider("Choose day:", min_value=1, max_value=31)
    month = st.select_slider("Choose month:",
                                        ["January", "February", "March", "April", "May", "June", "July",
                                         "August", "September", "October", "November", "December"]).lower()[:3]
    duration = st.slider("Choose duration:", min_value=0, max_value=4918)
    campaign = st.slider("Choose campaign:", min_value=1, max_value=63)
    pdays = st.slider("Choose pdays:", min_value=-1, max_value=873)
    previous = st.slider("Choose previous:", min_value=0, max_value=275)
    
    req =  Bank_Client(age=age, job=job, marital=marital, education=education, default=default,
                  balance=balance, housing=housing, contact=contact, loan=loan,
                  day_of_week=day_of_week, month=month, duration=duration,
                  campaign=campaign, pdays=pdays, previous=previous)
    
    if st.button("reaload models"):
         # Send GET request to FastAPI endpoint
            response = requests.get('http://localhost:8001/downloadmodels')

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                st.success("Models downloaded successfully!")
            else:
                st.error(f"Failed to download models. Status code: {response.status_code}")



    if st.button("Predict!"):
        prediction_response = requests.post('http://localhost:8001/predict/client', json=req.dict()).json()
        modelinfo_response = requests.get('http://localhost:8001/modelinfo').json()

        # Display prediction information
        st.subheader("Prediction Result")
        st.write(f"Prediction: {prediction_response['prediction']}")
        st.write(prediction_response['probabilityA'])
        st.write(prediction_response['probabilityB'])
         # Progress bar
        
        # Display model information
        st.subheader("Model Information")
        st.write(f"Model Type: {modelinfo_response['model_type']}")
     

       
        