from typing import Set, Union, Tuple
from copy import copy, deepcopy
import numpy as np
from matplotlib import pyplot as plt

from entities.base_game import Game
from entities.player import Player


class RedLightGreenLight(Game):
    def __init__(
            self,
            players: Set[Player],
            time_limit_sec: int = 300,
            n_stops: int = 20,
            distance: int = 100,
            save_hist: bool = True,
    ):
        super().__init__(players=players)
        self.n_stops = n_stops
        self.walking_window_sec = time_limit_sec / n_stops / 2  # half of the time is spent standing still
        self.still_window_sec = self.walking_window_sec
        self.distance = distance
        self.player_distance = {player: 0 for player in players}
        self.state_hist = []
        self.save_hist = save_hist

    def save_state(self):
        self.state_hist.append({
            'active': copy(self.active),
            'eliminated': copy(self.eliminated),
            'distances': copy(self.player_distance),
        })

    def play(self):
        scale_factor = 0.1
        i = 0
        while len(self.active) and i < self.n_stops:
            active_players = self.active.copy()
            if self.save_hist:
                self.save_state()
            for player in active_players:
                if self.player_distance[player] >= self.distance:
                    continue
                time_stood_still = np.random.gamma(
                    scale=1 / scale_factor,
                    shape=player.avg_player_standing_still_sec * scale_factor
                )
                if time_stood_still < self.still_window_sec:
                    self.eliminate(player)
                    continue
                next_position = self.player_distance[player] + player.walking_speed * self.walking_window_sec
                self.player_distance[player] = min(self.distance, next_position)

            i += 1

        slow_players = [player for player in self.active if self.player_distance[player] < self.distance]
        self.eliminate(slow_players)
        if self.save_hist:
            self.save_state()

    def get_statuses(self) -> Union[Tuple, Tuple]:
        x_coords_alive = []
        y_coords_alive = []

        x_coords_dead = []
        y_coords_dead = []
        for player in self.players:
            player_x = self.player_distance[player]
            player_y = player.id

            if player in self.active:
                x_coords_alive.append(player_x)
                y_coords_alive.append(player_y)
            else:
                x_coords_dead.append(player_x)
                y_coords_dead.append(player_y)

        return (x_coords_alive, y_coords_alive), (x_coords_dead, y_coords_dead)

    def plot_game(self) -> None:
        (x_coords_alive, y_coords_alive), (x_coords_dead, y_coords_dead) = self.get_statuses()
        plt.scatter(x_coords_alive, y_coords_alive, c='g', s=10, marker='o')
        plt.scatter(x_coords_dead, y_coords_dead, c='r', s=10, marker='X')
        plt.xlim([0, 100])
        plt.show()
