from entities.games import RedLightGreenLight, SugarHoneycombs, TugOfWar, Marbles, GameShow, GlassStones
from entities.games.squid_game import SquidGame
from utils import gen_players
import matplotlib.pyplot as plt


def main(n_players: int = 456, n_sims: int = 10_000, verbose: bool = False):

    players = gen_players(n_players)
    game_list = [
        RedLightGreenLight,
        SugarHoneycombs,
        TugOfWar,
        Marbles,
        GlassStones,
        SquidGame,
    ]

    game_show_survivor_count = []
    for sim_num in range(1, n_sims + 1):
        if sim_num % 100 == 0:
            print(f'Sim {sim_num:,} of {n_sims:,}')
        game_show = GameShow(players=players, game_list=game_list)
        game_show.play()
        game_show_survivor_count.append(game_show.num_active)
        if verbose:
            print(game_show)
            for i, g in enumerate(game_show.games_played, start=1):
                print(f'Game {i}) {g}')
    plt.hist(game_show_survivor_count, bins=100, density=True)
    plt.show()

if __name__ == '__main__':
    main()
