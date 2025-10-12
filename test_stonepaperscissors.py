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
                self.assertEqual(determine_winner("kamien", "papier"), "komputera",
                     "Oczekiwano wygranej komputera: kamien vs papier")
                # Gracz: papier, Komputer: nozyce
                self.assertEqual(determine_winner("papier", "nozyce"), "komputera",
                     "Oczekiwano wygranej komputera: papier vs nozyce")
                # Gracz: nozyce, Komputer: kamien
                self.assertEqual(determine_winner("nozyce", "kamien"), "komputera",
                     "Oczekiwano wygranej komputera: nozyce vs kamien")

    # Dodatkowe testy stałych (dla przyszłych zmian)


    def test_stale_ruchow(self):
                """Sprawdza, czy wszystkie ruchy są zdefiniowane w ZASADACH."""
                self.assertEqual(set(MOZLIWE_RUCHY), set(ZASADY.keys()),
                     "Klucze ZASAD powinny odpowiadać MOZLIWYM_RUCHOM")
                for ruch, bity_ruch in ZASADY.items():
                    self.assertIn(bity_ruch, MOZLIWE_RUCHY,
                      f"Ruch '{ruch}' bije '{bity_ruch}', który nie jest zdefiniowany jako możliwy ruch.")


if __name__ == '__main__':
    unittest.main()
