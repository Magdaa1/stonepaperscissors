import random

MOZLIWE_RUCHY = ["kamien", "papier", "nozyce"]
ZASADY = {
    "kamien": "nozyce",
    "papier": "kamien",
    "nozyce": "papier"
}


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
