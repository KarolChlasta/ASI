# Ćwiczenie: prosta transformacja danych z pandas

*Uwaga: komplet wersji demonstracyjnych, ćwiczeń i rozwiązań oraz rekomendacje dotyczące środowiska uruchomieniowego znajdziesz tutaj:*

https://github.com/wodecki/ASI_2022

---

W tym ćwiczeniu stworzysz obraz i oraz instrukcje uruchomienia prostego kontenera docker umożliwiającego uruchomienie notatnika jupyter i wytrenowania prostego modelu regresji

**Lista kontrolna**

- [ ] Plik `Dockerfile` specyfikujący obraz, który:
  - [ ] Instaluje pakiety niezbędne do uruchomienia notatnika `1. tworzenie modelu regresji.ipynb` 
    Wskazówka: wcześniej zidentyfikuj listę niezbędnych pakietów. Nie zapomnij o pakiecie `jupyter`
  - [ ] Kopiuje zawartość plików z dysku lokalnego (np.  `1. tworzenie modelu regresji.ipynb` , `Boston.csv`, etc.) do katalogu roboczego `\app`
  - [ ] Uruchamia jupyter notebook.
- [ ] Plik README.md z instrukcją dla użytkownika pokazującą, 
  - [ ] w jaki sposób zbudować obraz
  - [ ] w jaki sposób uruchomić kontener.
