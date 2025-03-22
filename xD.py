import csv

def wczytaj_najnowsze_wyniki(nazwa_pliku="szybkie600.csv"):
    """
    Wczytuje plik CSV z wynikami.
    Zakładamy, że plik ma nagłówek i kolumny:
      Data;Liczby
    gdzie w kolumnie 'Liczby' liczby są oddzielone przecinkami.
    Funkcja zwraca zbiór liczb z najnowszego losowania.
    """
    try:
        with open(nazwa_pliku, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            wyniki = list(reader)
            if not wyniki:
                print("Plik z wynikami jest pusty!")
                exit(1)
            # Zakładamy, że najnowszy wynik znajduje się na końcu pliku.
            najnowszy = wyniki[-1]
            liczby_str = najnowszy["Liczby"]
            liczby = set(map(int, liczby_str.split(",")))
            return liczby
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie został znaleziony!")
        exit(1)
    except Exception as e:
        print("Błąd podczas wczytywania pliku:", e)
        exit(1)

def pobierz_liczby_zakladu(komunikat):
    """
    Pobiera od użytkownika 6 unikalnych liczb z zakresu 1-32.
    """
    while True:
        try:
            liczby = set(map(int, input(komunikat).split()))
            if len(liczby) != 6:
                print("Musisz podać dokładnie 6 unikalnych liczb!")
                continue
            if any(l < 1 or l > 32 for l in liczby):
                print("Wszystkie liczby muszą być w zakresie 1-32!")
                continue
            return liczby
        except ValueError:
            print("Niepoprawny format liczb. Spróbuj ponownie.")

def main():
    print("=== Lotto Szybkie 600 === Wersja 1.0")
    
    # Wczytaj najnowsze wylosowane liczby z pliku
    drawn_numbers = wczytaj_najnowsze_wyniki()
    print("Najnowsze wylosowane liczby:", sorted(drawn_numbers))
    
    # Pobranie liczby zakładów od użytkownika
    while True:
        try:
            num_bets = int(input("Ile masz zakładów? "))
            if num_bets <= 0:
                print("Liczba zakładów musi być większa od 0.")
                continue
            break
        except ValueError:
            print("Podaj poprawną liczbę!")
    
    # Pobieranie zakładów użytkownika
    bets = []
    for i in range(1, num_bets + 1):
        print(f"\nZakład {i}:")
        bet = pobierz_liczby_zakladu("Podaj 6 liczb (1-32), oddzielonych spacjami: ")
        bets.append(bet)
    
    # Sprawdzenie wyników
    print("\n=== Wyniki zakładów ===")
    for idx, bet in enumerate(bets, 1):
        trafione = bet & drawn_numbers
        print(f"Zakład {idx}: {sorted(bet)} -> Trafione liczby: {sorted(trafione)} (łącznie: {len(trafione)})")

if __name__ == '__main__':
    main()