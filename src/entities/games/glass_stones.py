from typing import Set

import numpy as np

from entities.base_game import Game
from entities.player import Player


class GlassStones(Game):
    def __init__(self, players: Set[Player], n_steps: int = 18, time_limit_sec: int = 300):
        super().__init__(players=players)
        self.n_steps = n_steps
        self.time_limit_sec = time_limit_sec
        self.player_eliminated_step = {}

    def play(self) -> None:
        shuffled_players = list(self.players)
        np.random.shuffle(shuffled_players)

        curr_step = 0
        for player in shuffled_players:
            while curr_step < self.n_steps:
                is_good_step = np.random.rand() < 0.5
                curr_step += 1
                if not is_good_step:
                    self.eliminate(player)
                    self.player_eliminated_step[player] = curr_step
                    break

            if curr_step == self.n_steps:
                break
