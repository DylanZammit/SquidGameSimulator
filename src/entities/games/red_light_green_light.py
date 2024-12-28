from typing import Set

import numpy as np

from entities.base_game import Game
from entities.player import Player


class RedLightGreenLight(Game):
    def __init__(self, players: Set[Player], time_limit_sec: int = 300, n_stops: int = 20, distance: int = 100):
        super().__init__(players=players)
        self.n_stops = n_stops
        self.walking_window_sec = time_limit_sec / n_stops / 2  # half of the time is spent standing still
        self.still_window_sec = self.walking_window_sec
        self.distance = distance

    def play(self):
        scale_factor = 0.1
        i = 0
        while len(self.active) and i < self.n_stops:
            active_players = self.active.copy()
            for player in active_players:
                if self.player_distance[player] > self.distance:
                    continue
                self.player_distance[player] += player.walking_speed * self.walking_window_sec
                time_stood_still = np.random.gamma(
                    scale=1/scale_factor,
                    shape=player.avg_player_standing_still_sec * scale_factor
                )
                print(time_stood_still, self.still_window_sec)
                if time_stood_still < self.still_window_sec:
                    self.eliminated.add(player)
                    self.active.remove(player)
            i += 1
