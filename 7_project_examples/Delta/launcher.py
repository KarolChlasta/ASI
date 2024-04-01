import subprocess
import requests
import time

# Launch backend
backend_process = subprocess.Popen(["python", "app/prediction_api.py"])

# Wait until the backend is ready
while True:
    try:
        # Check if the backend is ready by sending a request to an endpoint
        response = requests.get("http://localhost:8001/")
        response.raise_for_status()
        if response.status_code == 200:
            break  # Backend is ready
    except requests.RequestException:
        pass  # Backend is not yet ready
    time.sleep(1)

# Launch frontend after backend is done
subprocess.run(["streamlit", "run", "src/streamlit_run.py"])