import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # 16 pistettä
            Player("Lemieux", "PIT", 45, 54),  # 99 pistettä
            Player("Kurri",   "EDM", 37, 53),  # 90 pistettä
            Player("Yzerman", "DET", 42, 56),  # 98 pistettä
            Player("Gretzky", "EDM", 35, 89)   # 124 pistettä
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytyy(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_ei_loydy(self):
        player = self.stats.search("Tuntematon")
        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        names = [p.name for p in players]
        self.assertListEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_palauttaa_tyhjan_kun_ei_osumia(self):
        players = self.stats.team("XYZ")
        self.assertEqual(len(players), 0)

    def test_top_palauttaa_oikean_maaran_ja_jarjestyksen(self):
        top_players = self.stats.top(2)
        # top(2) palauttaa 3 pelaajaa (i <= how_many, eli indeksit 0, 1, 2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
