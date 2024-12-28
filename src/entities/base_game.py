from typing import Set

from entities.player import Player


class Game:
    def __init__(self, players: Set[Player]):
        self.players = players
        self.player_distance = {player: 0 for player in players}
        self.active = set(players)
        self.eliminated = set()
        self.num_players = len(self.players)

    @property
    def active_players(self) -> Set[Player]:
        return self.active

    @property
    def eliminated_players(self) -> Set[Player]:
        return self.eliminated

    @property
    def num_active(self) -> int:
        return len(self.active)

    @property
    def num_eliminated(self) -> int:
        return len(self.eliminated)

    @property
    def survival_ratio(self) -> float:
        return len(self.eliminated) / len(self.players)

    def play(self) -> None:
        raise NotImplementedError

    def __repr__(self):
        return f'{type(self).__name__}: {self.num_players=}, {self.num_active=}, {self.num_eliminated=}, {self.survival_ratio=:.2f}'
