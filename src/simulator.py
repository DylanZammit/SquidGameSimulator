from entities.games import RedLightGreenLight, SugarHoneycombs, TugOfWar, Marbles, GameShow
from utils import gen_players


def main(n_players: int = 456):

    players = gen_players(n_players)
    game_list = [
        RedLightGreenLight,
        SugarHoneycombs,
        TugOfWar,
        Marbles,
        # GlassStones,
        # SquidGame,
    ]

    game_show = GameShow(players=players, game_list=game_list)
    game_show.play()
    print(game_show)
    for g in game_show.games_played:
        print(g)

if __name__ == '__main__':
    main()
