from typing import List, Set, Type
from entities.base_game import Game
from entities.player import Player


class GameShow(Game):

    def __init__(self, players: Set[Player], game_list: List[Type[Game]], max_prize_pool: int = 30_000_000):
        super().__init__(players=players)
        self.players = players
        self.game_list = game_list
        self.active = set(players)
        self.eliminated = set()
        self.games_played = []
        self.max_prize_pool = max_prize_pool
        self.prize_cost_per_player = max_prize_pool / self.num_players
        self.prize_pool = 0
        self.prize_per_player = 0

    def update_prize_pool(self):
        self.prize_pool = self.prize_cost_per_player * self.num_eliminated
        self.prize_per_player = self.prize_pool / self.num_active

    def fight(self):
        pass

    def vote(self):
        pass

    def play(self):
        for MiniGame in self.game_list:
            g = MiniGame(players=self.active)

            g.play()
            self.games_played.append(g)

            self.active = g.active
            self.eliminated |= g.eliminated

            self.vote()
            self.fight()

            self.update_prize_pool()

    def __repr__(self):
        return f"""{type(self).__name__}
=============================
{self.num_players=}, 
{self.num_active=}, 
{self.num_eliminated=}, 
{self.survival_ratio=:.2f}
{self.prize_pool=:,.0f}€
{self.prize_per_player=:,.0f}€
============================="""
