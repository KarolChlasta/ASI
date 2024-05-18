# Ćwiczenie: prosta transformacja danych z pandas

*Uwaga: komplet wersji demonstracyjnych, ćwiczeń i rozwiązań oraz rekomendacje dotyczące środowiska uruchomieniowego znajdziesz tutaj:*

https://github.com/wodecki/ASI_2022

---

W tym ćwiczeniu stworzysz i uruchomisz prosty kontener docker umożliwiający wczytanie danych z istniejącego pliku csv, przemnożenie ich przez 2 i zapis tak zmienionej ramki danych do nowego pliku.

**Lista kontrolna**

- [ ] Skrypt Python `app1.py`:
  - [ ] Wczytuje pakiet pandas w poprawnej wersji i drukuje tę wersję na ekranie
  - [ ] Wczytuje zawartość pliku `/input/input.csv` do ramki danych, i drukuje ją na ekranie
  - [ ] Mnoży tę treść x2, przypisuje do nowej ramki danych i drukuje wynik na ekranie
  - [ ] Zapisuje nową ramkę do pliku tekstowego `/output/output.csv`
- [ ] Plik `Dockerfile` specyfikujący obraz, który kopiuje komplet niezbędnych danych, ale nie uruchamia skryptu `app1.py` (dzięki czemu kontener nie zatrzymuje się po jego uruchomieniu)
- [ ] Obraz docker o nazwie `app1`
- [ ] Plik README.md z instrukcją dla użytkownika pokazującą, 
  - [ ] w jaki sposób zbudować obraz
  - [ ] w jaki sposób uruchomić kontener tak, by użytkownik mógł obejrzeć i modyfikować pliki wewnątrz kontenera (komponent `app1.py` i artefakt `input\input.csv`). 
    - [ ] Wskazówka: aby umożliwić edycję pliku, po uruchomieniu kontenera trzeba w nim zainstalować wybrany edytor. Przykładowo, dla edytora `nano`, uruchomić:
      - [ ] `$ apt-get update`
      - [ ] `$ apt-get install nano`
  - [ ] w jaki sposób uruchomić skrypt `app1.py` dostępny wewnątrz uruchomionego kontenera?
