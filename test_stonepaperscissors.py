import unittest
from stonepaperscissors import *

TEST_MOZLIWE_RUCHY = ["kamien", "papier", "nozyce"]
TEST_ZASADY = {
    "kamien": "nozyce",
    "papier": "kamien",
    "nozyce": "papier",
}


class UnitTestKPN(unittest.TestCase):
    # Testuje wszystkie mozliwe remisy
    def test_remis(self):
        for ruchy in TEST_MOZLIWE_RUCHY:
            self.assertEqual(determine_winner(ruchy, ruchy), "remis", f"Oczekiwano remisu dla {ruchy} vs {ruchy}")

            # Testuje wszytskie mozliwe wygrane gracza

    def test_wygrana_gracza(self):
                self.assertEqual(determine_winner("kamien", "nozyce"), "gracz",
                                 "Oczekiwano wygranej gracza: kamien vs nozyce")
                self.assertEqual(determine_winner("papier", "kamien"), "gracz",
                                 "Oczekiwano wygranej gracza: papier vs kamien")
                self.assertEqual(determine_winner("nozyce", "papier"), "gracz",
                                 "Oczekiwano wygranej gracza: nozyce vs papier")


    def test_wygrana_komputera(self):
                """Testuje wszystkie możliwe przegrane gracza (wygrane komputera)."""
                 # Gracz: kamien, Komputer: papier
                self.assertEqual(determine_winner("kamien", "papier"), "komputer",
                     "Oczekiwano wygranej komputera: kamien vs papier")
                # Gracz: papier, Komputer: nozyce
                self.assertEqual(determine_winner("papier", "nozyce"), "komputer",
                     "Oczekiwano wygranej komputera: papier vs nozyce")
                # Gracz: nozyce, Komputer: kamien
                self.assertEqual(determine_winner("nozyce", "kamien"), "komputer",
                     "Oczekiwano wygranej komputera: nozyce vs kamien")

    # Dodatkowe testy stałych (dla przyszłych zmian)


    def test_stale_ruchow(self):
                """Sprawdza, czy wszystkie ruchy są zdefiniowane w ZASADACH."""
                self.assertEqual(set(MOZLIWE_RUCHY), set(ZASADY.keys()),
                     "Klucze ZASAD powinny odpowiadać MOZLIWYM_RUCHOM")
                for ruch, bity_ruch in ZASADY.items():
                    self.assertIn(bity_ruch, MOZLIWE_RUCHY,
                      f"Ruch '{ruch}' bije '{bity_ruch}', który nie jest zdefiniowany jako możliwy ruch.")

    def test_ai_losowe_na_poczatku(self):
        historia_krotka = ["kamien","papier"]
        #powienien zwrocic jeden z mozliwych ruchow, bo historia jest za krotka,
        # assertIn poniewaz zwraca wynik losowy, a nie konkretna wartosc jak przyassertEqual
        self.assertIn(ai_przewidujace(historia_krotka), MOZLIWE_RUCHY)

    def test_ai_przewidywanie_wzorca_nozyce_papier(self):
        #"gracz powtarza N-P. Po (N, P) gracz zagral N. AI przewiduje czy jest N jak jest to powinien zagrac K (Kamien)."
        #wzorzec N-P powtarza sie, a po nim zawsze N
        historia_gracza = [
            "nozyce", "papier", "nozyce",
            "nozyce", "papier", "nozyce",
            "nozyce", "papier",  #ostatnie dwa ruchy
        ]
        #oczekiwany ruch gracza to nozyce
        #oczekiwany ruch AI to kamien
        self.assertEqual(ai_przewidujace(historia_gracza),"kamien","AI powinna zagrac Kamien, aby pokonac przeidywane nozyce.")
if __name__ == '__main__':
    unittest.main()
