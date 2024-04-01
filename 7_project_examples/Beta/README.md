
<h3 align="center">Projekt z przedmiotu “Architektury
rozwiązań i wdrożeń SI”</h3>
<p align="center">
    <br />
    <a href="./docs/Dokumentacja_Techniczna.pdf"><strong>Dokumentacja techniczna »</strong></a>
    <br />
</p>

Projekt służy do tworzenia modeli do predykcji zdatności wody na podstawie danych dostępnych na Kaggle. 

Projekt korzysta z:
* Kedro do zarządzania danymi i pipeline'ami, 
* sqlite do przechowywana danych,
* AutoGluon do automatycznego dostosowywania modeli,
* WandDB do śledzenia i wizualizacji trenowania modeli
* FastAPI do stworzenia API do interakcji z modelem,
* Streamlit do stworzenia prostego interfejsu użytkownika.

## Instalacja

- Utwórz wirtualne środowisko dla Python 3.9.18 (np. kedro_env), z którego będą uruchamiana back-end i streamlit
  - Przejdż do folderu system_level
  - Zainstaluj wymagane moduły za pomocą komendy:
    ```
    pip install -r requirements_kedro.txt
    ```
- Utwórz wirtualne środowisko dla Python 3.9.18 (np. fastAPI_env), z któego będą wystawiane endpointy z FastAPI
  - Przejdż do folderu system_level
  - Zainstaluj wymagane moduły za pomocą komendy:
    ```
    pip install -r requirements_fastapi.txt
    ```

## Tworzenie i retrenowanie modeli

W środowisku kendro_env, z folderu ASI_GROUP/asi-kedro można utworzyć modele za pomocą komendy:
```
kedro run
```
Retrenowanie modeli odbywa się za pomocą komendy:
```
kedro run --pipeline=retrain
```

## Uruchomienie FastAPI i Streamlita

W środowisku fastAPI_env, z folderu ASI_GROUP należy uruchomić FastAPI za pomocą komendy:
```
uvicorn api.main:app --reload
```

W środowisku kedro_env, z folderu ASI_GROUP należy uruchomić Streamlit za pomocą komendy:
```
streamlit run streamlit/stream_app.py
```

## Struktura plików

```
ASI_GROUP
├───.idea
│   └───inspectionProfiles
├───api
│   ├───asi-kedro
│   ├───config
│   ├───endpoint
│   │   └───__pycache__
│   ├───model
│   │   └───__pycache__
│   ├───services
│   │   └───__pycache__
│   ├───temp
│   ├───templates
│   └───__pycache__
├───asi-kedro
│   ├───AutogluonModels
│   ├───conf
│   │   ├───base
│   │   └───local
│   ├───dags
│   ├───data
│   │   ├───01_raw
│   │   ├───03_primary
│   │   ├───05_model_input
│   │   ├───06_models
│   │   └───07_model_outputs
│   ├───docs
│   │   └───source
│   ├───sqlite
│   ├───src
│   │   ├───asi_kedro
│   │   │   ├───pipelines
│   │   │   │   ├───data_engineering
│   │   │   │   │   └───__pycache__
│   │   │   │   ├───data_science
│   │   │   │   │   └───__pycache__
│   │   │   │   ├───model_evaluation
│   │   │   │   │   └───__pycache__
│   │   │   │   ├───model_retraining
│   │   │   │   │   └───__pycache__
│   │   │   │   ├───synthetic_data_creation
│   │   │   │   │   └───__pycache__
│   │   │   │   └───__pycache__
│   │   │   └───__pycache__
│   │   └───tests
│   │       └───pipelines
│   │           ├───data_engineering
│   │           ├───data_science
│   │           ├───model_evaluation
│   │           ├───model_retraining
│   │           └───synthetic_data_creation
│   └───wandb
├───streamlit
│   ├───tools
│   │   └───__pycache__
│   └───__pycache__
├───visulation
│   └───tools
├───system_level
└───__pycache__
```