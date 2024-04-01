# Projekt ASI

## Zaktualizuj plik credentials.yml (w katalogu conf/local) danymi do swojej bazy danych postgres

```
postgres:
  username: <username>
  password: <password>
  host: <host>
  port: <port>
  name: <name>
```

## Jak utworzyć środowisko?

Aby uruchomić projekt należy utworzyć środowisko w conda

```
conda env create -f python39.yaml
```

a następnie uruchomić środowisko za pomocą

```
conda activate python39
```

## Jak uruchomić projekt? 

Aby uruchomić streamlit należy wykonać: 

```
streamlit run streamlit_app.py
```

Aby móc uruchomić potok, wygenerować dane syntetyczne lub dokonać predykcji należy wykonać: 

```
uvicorn app:app
```

## Jeżeli twoja baza danych nie zawiera tabeli exoplanets wykonaj skrypt create_table.sql lub jeżeli tabela jest pusta

Utworzenie tabeli
```
psql -h <host> -p <port> -U <username> -d <name> -f <ścieżka do pliku create_table.sql>
```

Zasilenie bazy danych danymi po wcześniejszym polaczeniu sie z baza danych postgres

```
\copy exoplanets FROM '/ścieżka/do/pliku/cleaned_5250.csv' DELIMITER ',' CSV HEADER
```

## Użyte technologie

```
Streamlit
FastAPI
Kedro
Autogluon
Postgresql
Wandb
```

## Architektura

![architektura](<dokumentacja/ASI_architektura.jpg>)