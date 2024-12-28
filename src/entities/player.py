from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Player:
    id: int
    walking_speed: float
    avg_player_standing_still_sec: float

class Team:
    def __init__(self, players: Tuple[Player, ...]):
        self.players = players

    def __len__(self):
        return len(self.players)
