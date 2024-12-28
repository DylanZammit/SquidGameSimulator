from typing import List, Set, Type
from entities.base_game import Game
from entities.player import Player


class GameShow(Game):
    def __init__(self, players: Set[Player], game_list: List[Type[Game]]):
        super().__init__(players=players)
        self.players = players
        self.game_list = game_list
        self.active = set(players)
        self.eliminated = set()
        self.games_played = []

    def play(self):
        for MiniGame in self.game_list:
            g = MiniGame(players=self.active)

            g.play()
            self.active = g.active
            self.eliminated |= g.eliminated
            # TODO: implement vote/murder change
            # vote
            # murder
            self.games_played.append(g)
