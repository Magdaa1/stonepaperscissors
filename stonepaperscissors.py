import random

MOZLIWE_RUCHY = ["kamien", "papier", "nozyce"]
ZASADY = {
    "kamien": "nozyce",
    "papier": "kamien",
    "nozyce": "papier"
}
HISTORIA_RUCHOW_GRACZA = []

def show_menu():
    print("Witaj w grze: KAMIEN, PAPIER, NOZYCE")
    print("1. Zagraj jedna runde")
    print("2. Best of 3")
    print("3. Best of 4")
    print("4. Wyjdz")


def get_user_choice():
    while True:
        choice = input("Wybierz opcje (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
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


def play_single_round():
    wynik = play_round()
    if wynik == "gracz":
        print("🎉 Wygrałeś cala gre!")
    elif wynik == "komputer":
        print("💻 Komputer wygrał!")
    else:
        print("🤝 Remis!")


def play_round():
    ruch_gracza = get_player_move()
    ruch_komputera = random.choice(MOZLIWE_RUCHY)

    print(f"Komputer zagrywa: {ruch_komputera}")

    wynik = determine_winner(ruch_gracza, ruch_komputera)
    if wynik == "gracz":
        print("Wygrales runde!\n")
    elif wynik == "komputer":
        print("Przegrales runde!\n")
    else:
        print("Remis w tej rundzie!")
    return wynik

def play_best_of_x(cel):
    """Opcja 2/3 - best of X"""
    wygrane_gracz = 0
    wygrane_komputer = 0

    print(f"Gramy do {cel} wygranych!\n")

    while wygrane_gracz < cel and wygrane_komputer < cel:
        print(f"Wynik: Ty {wygrane_gracz} - {wygrane_komputer} Komputer")

        wynik = play_round()
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

def determine_winner(ruch_gracza, ruch_komputera):
    if ruch_gracza == ruch_komputera:
        return "remis"
    elif ZASADY[ruch_gracza] == ruch_komputera:
        return "gracz"
    else:
        return "komputera"

# F-cja pomocnicza: ruch, ktory pokonuje dany ruch
def get_pokonujacy_ruch(ruch):
    # Szukamy klucza w ZASADY, ktorego Wartosc (to co bije) jest rowna argumentowi ruch
    for r_pokonujacy, r_bity in ZASADY.items():
        if r_bity == ruch:
            return r_pokonujacy
        return random.choice(MOZLIWE_RUCHY) #Zabezpieczenie przed mozliwmi ruchami
def ai_przewidujace(historia):
    #"przewiduje nastepne ruchy gracza na podstawie analizy powtarzajacych sie dwoch ostatnich sekwencji ruchow"
    # 1. Sprawdz, czy mamy wystarczajaco ilosc ruchow min to 3, aby przeanalizowac najczesciej wystepujacy wzorzec A-B -> C
    if len(historia) < 3:
        return random.choice(MOZLIWE_RUCHY)
    # zidentyfikuj wzorzec: Ostatnie dwa ruchy gracza
    ostatnie_dwa = tuple(historia[-2:])
    #zliczanie co gracz zagrywa po tym wzorcu
    statystyki_po_wzorcu = {"kamien": 0, "papier": 0, "nozyce": 0}
    #przeszukaj historie, ale tylko do przedostatniego ruchu (bo potrzebujemy ruch 'po')
    for i in range(len(historia) - 2): #zakres iteracji, gdzie len(historia) - to calkowita liczba ruchow w historii
        # np: historia ma 5 elementow [0,1,2,3,4] dl -> 5; range(5 - 2) to range(3), czyli i ma 0,1,2. dlatego mamy i=2
        # wzorzec to historia[2:4], czyli elementy 2 i 3;
        # ruch_po_wzorcu to historia[2+2], czyli element 4 (ostatni)
        wzorzec = tuple(historia[i:i + 2:]) # tymczasowy wzorzec o dlugosci dwoch elementow zaczynajcych sie od indeksu i
        #uzycie krotki(tuple) jest kluczowe, poniewaz sa niemutowalne, i sa uzywane jako klucze w slowniku.
        # Mozna zliczac statystyki dla kazdego uniklnego wzorca(ruch_A, ruch_B) np: Gdy i=0, wzorzec to (historia[0], historia[1])
        if wzorzec == ostatnie_dwa: #sprawdz czy znaleziony wzorzec jest identyczny z ostatnia sekwencja zagadnien graczz (ostatnie_dwa)
            ruch_po_wzorcu = historia[i + 2] #jesli wzorce takie same to odczytujemy ruch, ktory nastapil bezposrednio po tym wzorcu w przeszlosci
            statystyki_po_wzorcu[ruch_po_wzorcu] += 1 #nastepnie ten ruch jest zliczany w sloeniku. Zbudowanie statystyk sekecni co zagral gracz X a co Y

        #jesli wzorzec sie nie powtarza (brak statystyk), graj losowo
        if sum(statystyki_po_wzorcu.values()) == 0:
            return random.choice(MOZLIWE_RUCHY)
        #znalezc przewidywany ruch gracza (ten, ktory ma najwiecej zliczen)
        przewidywany_ruch_gracza = max(statystyki_po_wzorcu,key=statystyki_po_wzorcu.get) #key=statystyki_po_wzorcu.get -> aby porwonac klucze, uzyj ich wartosci ze slownika statystyki_po_wzorcu
        #zagraj rucj, ktory POKONA przewidywany ruch gracza
        return get_pokonujacy_ruch(przewidywany_ruch_gracza)

def main():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            play_single_round()
        elif choice == "2":
            play_best_of_x(3)
        elif choice == "3":
            play_best_of_x(5)
        elif choice == "4":
            print("Dzięki za grę!")
            break


# uruchamianie gry
if __name__ == "__main__":
    main()
