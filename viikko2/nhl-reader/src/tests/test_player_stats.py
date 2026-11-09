import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "team": "EDM",
                "nationality": "CAN",
                "goals": 4,
                "assists": 12,
            }),
            Player({
                "name": "Lemieux",
                "team": "PIT",
                "nationality": "CAN",
                "goals": 45,
                "assists": 54,
            }),
            Player({
                "name": "Kurri",
                "team": "EDM",
                "nationality": "FIN",
                "goals": 37,
                "assists": 53,
            }),
            Player({
                "name": "Yzerman",
                "team": "DET",
                "nationality": "CAN",
                "goals": 42,
                "assists": 56,
            }),
            Player({
                "name": "Gretzky",
                "team": "EDM",
                "nationality": "CAN",
                "goals": 35,
                "assists": 89,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_returns_players_by_points(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_top_scorers_by_team_returns_players_by_points(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_top_scorers_by_team_returns_empty_list_without_matches(self):
        players = self.stats.top_scorers_by_team("XYZ")

        self.assertEqual(players, [])

    def test_top_goal_scorers_returns_requested_players_by_goals(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman"],
        )
