from itertools import batched
from typing import Set, List, Tuple

import numpy as np

from entities.base_game import Game
from entities.player import Player, Team


class TugOfWar(Game):
    def __init__(self, players: Set[Player]):
        super().__init__(players=players)
        self.teams = self.gen_teams(n_teams=8)
        self.matchups = self.gen_matchups()

    # handle odd num of teams
    def gen_teams(self, n_teams: int) -> List[Team]:
        team_size = len(self.players) // n_teams
        players_shuffled = list(self.players.copy())
        np.random.shuffle(players_shuffled)
        teams = [Team(players) for players in batched(players_shuffled, team_size)]
        if len(teams[-1]) < team_size:
            small_team = teams.pop(-1)
            last_team = teams.pop(-1)
            merged_team = Team(players=small_team.players + last_team.players)
            teams.append(merged_team)
        return teams

    def gen_matchups(self) -> List[Tuple[Team, Team]]:
        np.random.shuffle(self.teams)
        return [(team_a, team_b) for team_a, team_b in batched(self.teams, 2)]

    def play(self) -> None:
        for team_a, team_b in self.matchups:
            left_wins = np.random.rand() < 0.5
            team_loser = team_b if left_wins else team_a
            self.eliminate(team_loser.players)

