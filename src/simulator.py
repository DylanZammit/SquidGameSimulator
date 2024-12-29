from entities.games import RedLightGreenLight, SugarHoneycombs, TugOfWar, Marbles, GameShow, GlassStones
from entities.games.squid_game import SquidGame
from utils import gen_players


def main(n_players: int = 456, n_sims: int = 1):

    players = gen_players(n_players)
    game_list = [
        RedLightGreenLight,
        SugarHoneycombs,
        TugOfWar,
        Marbles,
        GlassStones,
        SquidGame,
    ]

    for _ in range(n_sims):
        game_show = GameShow(players=players, game_list=game_list)
        game_show.play()
        print(game_show)
        for i, g in enumerate(game_show.games_played, start=1):
            print(f'Game {i}) {g}')

if __name__ == '__main__':
    main()
