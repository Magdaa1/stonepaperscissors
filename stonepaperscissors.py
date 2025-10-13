import random
import unittest
from collections import defaultdict

MOZLIWE_RUCHY = ["kamien", "papier", "nozyce"]
ZASADY = {
    "kamien": "nozyce",
    "papier": "kamien",
    "nozyce": "papier"
}


class Stonepaperscissors:

    def __init__(self):
        self.historia_gracza = []
        self.historia_komputera = []
        self.statystyki = {
            "wygrane_gracz": 0,
            "wygrane_komputer": 0,
            "remisy": 0
        }

    def reset_statystyki(self):
        self.statystyki = {
            "wygrane_gracz": 0,
            "wygrane_komputer": 0,
            "remisy": 0,
        }

    def wyswietl_statystyki(self):
        """Wyświetla szczegółowe statystyki."""

        print("\n" + "=" * 40)
        print("📊 STATYSTYKI GRY")
        print("=" * 40)
        print(f"Wygrane gracza: {self.statystyki['wygrane_gracz']}")
        print(f"Wygrane komputera: {self.statystyki['wygrane_komputer']}")
        print(f"Remisy: {self.statystyki['remisy']}")


        total = sum(self.statystyki.values())
        if total > 0:
            win_rate = (self.statystyki['wygrane_gracz'] / total) * 100
            print(f"\nWspolczynnik wygranych: {win_rate:.1f}%")
            print(f"Laczna liczba rund: {len(self.historia_gracza)}")
        else:
            print(f"Laczna liczba rund: {len(self.historia_gracza)}")
        print("=" * 40 + "\n")


def show_menu():
    print("\n" + "=" * 40)
    print("Witaj w grze: KAMIEN, PAPIER, NOZYCE")
    print("=" * 40)
    print("1. Zagraj jedna runde")
    print("2. Best of 3 (do 3 wygranych)")
    print("3. Best of 5 (do 5 wygranych)")
    print("4. Statystyki")
    print("5. Wyjdz")
    print("=" * 40)


def get_user_choice():
    while True:
        choice = input("Wybierz opcje (1-5): ").strip()
        if choice in ("1", "2", "3", "4", "5"):
            return choice
        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")


def get_player_move():
    while True:
        ruch = input("Wybierz: kamien, papier, nozyce ").lower().strip()
        if ruch in MOZLIWE_RUCHY:
            return ruch
        else:
            print("Nieprawidlowy wybor.Sprobuj pownownie")


def determine_winner(ruch_gracza, ruch_komputera):
    if ruch_gracza == ruch_komputera:
        return "remis"
    elif ZASADY[ruch_gracza] == ruch_komputera:
        return "gracz"
    else:
        return "komputer"


def get_pokonujacy_ruch(ruch):
    """Zwraca ruch, który pokonuje dany ruch."""
    for r_pokonujacy, r_bity in ZASADY.items():
        if r_bity == ruch:
            return r_pokonujacy
    return random.choice(MOZLIWE_RUCHY)


# F-cja pomocnicza: ruch, ktory pokonuje dany ruch
def get_pokonujacy_ruch(ruch):
    # Szukamy klucza w ZASADY, ktorego Wartosc (to co bije) jest rowna argumentowi ruch
    for r_pokonujacy, r_bity in ZASADY.items():
        if r_bity == ruch:
            return r_pokonujacy
    return random.choice(MOZLIWE_RUCHY)  # Zabezpieczenie przed mozliwmi ruchami


def ai_przewidujace(historia, dlugosc_wzorca=2):
    # "przewiduje nastepne ruchy gracza na podstawie analizy powtarzajacych sie dwoch ostatnich sekwencji ruchow"
    # 1. Sprawdz, czy mamy wystarczajaco ilosc ruchow min to 3, aby przeanalizowac najczesciej wystepujacy wzorzec A-B -> C
    if len(historia) < dlugosc_wzorca + 1:
        return random.choice(MOZLIWE_RUCHY)
    # zidentyfikuj wzorzec: Ostatnie dwa ruchy gracza
    ostatnie_ruchy = tuple(historia[-dlugosc_wzorca:])
    # zliczanie co gracz zagrywa po tym wzorcu
    statystyki_po_wzorcu = defaultdict(int)
    # przeszukaj historie, ale tylko do przedostatniego ruchu (bo potrzebujemy ruch 'po')
    for i in range(
            len(historia) - dlugosc_wzorca):  # zakres iteracji, gdzie len(historia) - to calkowita liczba ruchow w historii
        # np: historia ma 5 elementow [0,1,2,3,4] dl -> 5; range(5 - 2) to range(3), czyli i ma 0,1,2. dlatego mamy i=2
        # wzorzec to historia[2:4], czyli elementy 2 i 3;
        # ruch_po_wzorcu to historia[2+2], czyli element 4 (ostatni)
        wzorzec = tuple(historia[
                            i:i + dlugosc_wzorca:])  # tymczasowy wzorzec o dlugosci dwoch elementow zaczynajcych sie od indeksu i
        # uzycie krotki(tuple) jest kluczowe, poniewaz sa niemutowalne, i sa uzywane jako klucze w slowniku.
        # Mozna zliczac statystyki dla kazdego uniklnego wzorca(ruch_A, ruch_B) np: Gdy i=0, wzorzec to (historia[0], historia[1])
        if wzorzec == ostatnie_ruchy:  # sprawdz czy znaleziony wzorzec jest identyczny z ostatnia sekwencja zagadnien graczz (ostatnie_dwa)
            ruch_po_wzorcu = historia[
                i + dlugosc_wzorca]  # jesli wzorce takie same to odczytujemy ruch, ktory nastapil bezposrednio po tym wzorcu w przeszlosci
            statystyki_po_wzorcu[
                ruch_po_wzorcu] += 1  # nastepnie ten ruch jest zliczany w sloeniku. Zbudowanie statystyk sekecni co zagral gracz X a co Y

        # jesli wzorzec sie nie powtarza (brak statystyk), graj losowo
        if not statystyki_po_wzorcu:
            return random.choice(MOZLIWE_RUCHY)
        # znalezc przewidywany ruch gracza (ten, ktory ma najwiecej zliczen)
        przewidywany_ruch_gracza = max(statystyki_po_wzorcu,
                                       key=statystyki_po_wzorcu.get)  # key=statystyki_po_wzorcu.get -> aby porwonac klucze, uzyj ich wartosci ze slownika statystyki_po_wzorcu
        # zagraj rucj, ktory POKONA przewidywany ruch gracza
        return get_pokonujacy_ruch(przewidywany_ruch_gracza)


def play_round(gra):
    ruch_gracza = get_player_move()
    ruch_komputera = ai_przewidujace(gra.historia_gracza)

    gra.historia_gracza.append(ruch_gracza)
    gra.historia_komputera.append(ruch_komputera)

    print(f"\n🎲 Twój ruch: {ruch_gracza}")
    print(f"💻 Komputer: {ruch_komputera}")

    wynik = determine_winner(ruch_gracza, ruch_komputera)
    if wynik == "gracz":
        print("Wygrales runde!\n")
        gra.statystyki["wygrane_gracz"] += 1
    elif wynik == "komputer":
        print("Przegrales runde!\n")
        gra.statystyki["wygrane_komputer"] += 1
    else:
        print("Remis w tej rundzie!")
        gra.statystyki["remisy"] += 1
    return wynik


def play_single_round(gra):
    """Rozgrywa pojedynczą grę."""
    print("\n" + "=" * 40)
    print("POJEDYNCZA RUNDA")
    print("=" * 40)
    play_round(gra)


def play_best_of_x(gra, cel):
    """Opcja 2/3 - best of X"""
    gra.reset_statystyki()
    wygrane_gracz = 0
    wygrane_komputer = 0

    print(f"Gramy do {cel*2 - 1} (do {cel} wygranych!\n")

    while wygrane_gracz < cel and wygrane_komputer < cel:
        print(f"Wynik: Ty {wygrane_gracz} - {wygrane_komputer} Komputer")

        wynik = play_round(gra)
        if wynik == "gracz":
            wygrane_gracz += 1
        elif wynik == "komputer":
            wygrane_komputer += 1
        # remis nie zmienia liczników

    # Końcowy wynik
    print("=" * 30)
    if wygrane_gracz == cel:
        print("🎉 WYGRAŁEŚ CAŁĄ GRĘ! 🎉")
    else:
        print("💻 Komputer wygrał grę!")
    print(f"Ostateczny wynik: {wygrane_gracz} - {wygrane_komputer}")


def main():
    gra = Stonepaperscissors()
    print("\n🎮 Witaj w grze Kamień-Papier-Nożyce!")
    print("💡 Komputer używa AI, które uczy się Twoich wzorców!")

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            play_single_round(gra)
        elif choice == "2":
            play_best_of_x(gra,3)
        elif choice == "3":
            play_best_of_x(gra,5)
        elif choice == "4":
            gra.wyswietl_statystyki()
        elif choice == "5":
            print("Dzięki za grę!")
            gra.wyswietl_statystyki()
            break


# uruchamianie gry
if __name__ == "__main__":
    main()
