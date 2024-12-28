from typing import Set

from entities.base_game import Game
from entities.player import Player


class SugarHoneycombs(Game):
    def __init__(self, players: Set[Player]):
        super().__init__(players=players)

    def play(self) -> None:
        for player in self.players:
            ...
