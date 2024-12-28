from typing import Set

import numpy as np

from entities.base_game import Game
from entities.player import Player


class Marbles(Game):
    def __init__(self, players: Set[Player]):
        super().__init__(players=players)

    def play(self) -> None:
        shuffled_players = list(self.players)
        np.random.shuffle(shuffled_players)
        n_eliminated = self.num_players // 2 + (1 if self.num_players % 2 == 1 else 0)
        self.eliminated = set(shuffled_players[:n_eliminated])
        self.active = set(shuffled_players[n_eliminated:])

