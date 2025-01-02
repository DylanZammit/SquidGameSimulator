from typing import Set
from copy import copy
import numpy as np

from entities.base_game import Game
from entities.player import Player


class GlassStones(Game):
    def __init__(
            self,
            players: Set[Player],
            n_steps: int = 18,
            time_limit_sec: int = 300,
            save_hist: bool = True,
    ):
        super().__init__(players=players)
        self.n_steps = n_steps
        self.time_limit_sec = time_limit_sec
        self.player_eliminated_step = {}
        self.state_hist = []
        self.save_hist = save_hist

    def play(self) -> None:
        shuffled_players = list(self.players)
        np.random.shuffle(shuffled_players)

        curr_step = 0
        player_num = 0
        while curr_step < self.n_steps and self.num_active > 0:
            player = shuffled_players[player_num]
            while curr_step < self.n_steps:
                is_good_step = np.random.rand() < 0.5
                curr_step += 1
                if not is_good_step:
                    self.eliminate(player)
                    self.player_eliminated_step[player] = curr_step
                    break
            if self.save_hist:
                self.state_hist.append(
                    {'curr_step': curr_step, 'num_active': copy(self.active), 'eliminated': copy(self.eliminated)}
                )
            player_num += 1
