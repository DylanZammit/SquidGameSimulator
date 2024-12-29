from typing import Set

import numpy as np

from entities.base_game import Game
from entities.player import Player


class SquidGame(Game):
    def __init__(self, players: Set[Player]):
        super().__init__(players=players)
        self.attackers, self.defenders = self.gen_teams()

    def gen_teams(self):
        shuffled_players = list(self.players.copy())
        np.random.shuffle(shuffled_players)
        team_size = self.num_players // 2
        attackers, defenders = shuffled_players[:team_size], shuffled_players[team_size:]
        return attackers, defenders

    def play(self):
        # model p uncertainty with beta distribution
        prob_defender_wins = np.random.beta(a=3, b=2)
        defender_wins = np.random.rand() < prob_defender_wins
        self.eliminate(self.attackers if defender_wins else self.defenders)
