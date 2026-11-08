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
