# README

Aby:

1. stworzyć obraz, w linii komend wpisz:
   `docker build --tag app1 .`

2. uruchomić kontener tak, by móc przeglądać jego zawartość i uruchamiać wewnątrz niego programu, w linii komend wpisz:
   `docker run -ti app1 bash`
3. wyjść z kontenera bez jego zatrzymywać, w jego powłoce wpisz
    `exit`.
4. zidentyfikować uruchomiony kontener, w linii komend wpisz 
   `$ docker ps`
5. uruchomić skrypt `app1.py` w folderze roboczym uruchomionego kontenera, w linii komend wpisz:
   `$ docker run -ti app1 python3 app1.py`





