from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

SEASONS = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
]

NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
    "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS",
]


def build_table(season, category, players):
    table = Table(title=f"Season {season} players from {category}")
    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    return table


def search_players(stats):
    search_by = Prompt.ask(
        "Search by", choices=["nationality", "team", "quit"],
        default="nationality",
    )
    if search_by == "quit":
        return None

    if search_by == "nationality":
        category = Prompt.ask(
            "Nationality", choices=NATIONALITIES, default=""
        )
        if not category:
            return None
        players = stats.top_scorers_by_nationality(category)
    else:
        category = Prompt.ask("Team").upper()
        players = stats.top_scorers_by_team(category)

    return category, players


def main():
    console = Console()
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    while True:
        result = search_players(stats)
        if result is None:
            break
        category, players = result
        console.print(build_table(season, category, players))


if __name__ == "__main__":
    main()
