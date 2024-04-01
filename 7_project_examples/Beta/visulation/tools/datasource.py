import requests


def get_training_data():
    return requests.get('http://localhost:8000/train_data').json()

def get_raw_data_api():
    return requests.get('http://localhost:8000/raw_data').json()


def get_confusion_matrix():
    return requests.get('http://localhost:8000/confusion_matrix').json()


def get_evaluation_metrics():
    return requests.get('http://localhost:8000/evaluation_metrics').json()
