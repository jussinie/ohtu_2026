class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered = [
            player
            for player in self._players
            if player.nationality == nationality
        ]
        return sorted(filtered, key=lambda p: p.points, reverse=True)

    def top_scorers_by_team(self, team):
        filtered = [player for player in self._players if player.team == team]
        return sorted(filtered, key=lambda p: p.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä."""
        return sorted(
            self._players, key=lambda p: p.goals, reverse=True)[:how_many]
