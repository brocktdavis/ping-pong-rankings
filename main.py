from Player import *
from Game import *

def init_players(filename):
    
    players = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            strs = line.split(',')

            first = strs[1]
            last = strs[0]
            id_num = int(strs[2])

            p = Player(first, last, id_num)
            players[id_num] = p

    return players

def init_games(players, filename):

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            strs = line.split(',')

            id1 = int(strs[0])
            score1 = int(strs[1])
            id2 = int(strs[2])
            score2 = int(strs[3])

            p1 = players[id1]
            p2 = players[id2]

            g = Game(p1, score1, p2, score2)
            p1.add_game(g)
            p2.add_game(g)

def iter_ranks(players):
    for player in players.values():
        player.update_rating()

def print_rankings(players):
    player_list = list(players.values())
    sorted_list = sorted(player_list, key=Player.get_rating, reverse=True)
    i = 1
    for player in sorted_list:
        rounded_rating = round(player.rating, 2)
        print("%2s %s %s: %.2f" % \
            (str(i), player.first, player.last, rounded_rating))
        i += 1

players = init_players('players.csv')
games = init_games(players, 'games.csv')
for i in range(2000):
    iter_ranks(players)
print_rankings(players)