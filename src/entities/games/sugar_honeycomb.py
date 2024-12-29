from typing import Set
import numpy as np
from entities.base_game import Game
from entities.player import Player
from entities.cookies import Triangle, Circle, Star, Umbrella

class SugarHoneycombs(Game):
    def __init__(self, players: Set[Player]):
        super().__init__(players=players)
        self.options = [Triangle, Circle, Star, Umbrella]
        self.num_cookies = len(self.options)
        self.player_cookies = self.assign_cookies()

    def assign_cookies(self):
        player_choices = np.random.randint(0, self.num_cookies, size=self.num_players)
        return {player: self.options[choice] for player, choice in zip(self.players, player_choices)}

    def play(self) -> None:
        for player, cookie in self.player_cookies.items():
            prob_success = np.random.beta(a=cookie.alpha, b=cookie.beta)
            if np.random.rand() > prob_success:
                self.eliminate(player)
