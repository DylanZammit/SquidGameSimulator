from typing import Set

import numpy as np

from entities.player import Player


def gen_players(n_players: int) -> Set[Player]:
    #https://www.researchgate.net/figure/The-walking-speed-of-pedestrians-is-distributed-normally-with-an-estimated-mean-of-134_fig4_286071735
    # https: // revistapesquisa.fapesp.br / en / the - art - of - standing - still /
    avg_walking_speed_mps = 1.34
    std_walking_speed_mps = 0.37
    avg_standing_still_sec = 30

    walking_speeds = list(np.random.randn(n_players) * std_walking_speed_mps + avg_walking_speed_mps)
    scale_factor = 10
    avg_player_standing_still_sec = np.random.gamma(
        shape=avg_standing_still_sec * scale_factor,
        scale=1 / scale_factor,
        size=n_players
    )

    return {
        Player(
            id=i,
            walking_speed=float(walking_speeds[i]),
            avg_player_standing_still_sec=float(avg_player_standing_still_sec[i]),
        ) for i in range(n_players)
    }
