from Player import *
from Game import *
import os

DAT_DIR = './../dat/'

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

def init_games(players, excluded_players, filepath):

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            strs = line.split(',')

            id1 = int(strs[0])
            score1 = int(strs[1])
            id2 = int(strs[2])
            score2 = int(strs[3])

            if id1 in excluded_players:
                continue
            if id2 in excluded_players:
                continue

            p1 = players[id1]
            p2 = players[id2]

            g = Game(p1, score1, p2, score2)
            p1.add_game(g)
            p2.add_game(g)

def iter_ranks(players):
    for player in players.values():
        player.update_rating()

def sort_players(players):

    output = []
    # players is dict int->Player.Player
    # convert of list of tuples
    player_list = list(players.items())

    sorted_list = sorted(player_list, key=lambda tup: tup[1].rating, reverse=True)
    # print(sorted_list)

    for player in sorted_list:
        player_json = {
            'id': player[0],
            'name': player[1].get_name(),
            'rating': round(player[1].get_rating(), 2)
        }
        output.append(player_json)
    return output 

def get_rankings(excluded_players = []):

    # Have list of players in dict based on player id
    players = init_players(DAT_DIR + 'players.csv')
    # Initalize games
    games = init_games(players, excluded_players, DAT_DIR + 'games.csv')
    # Delete players which should be excluded
    for player in excluded_players:
        del players[player]
    # Do rankings loop
    for i in range(2000):
        iter_ranks(players)

    return sort_players(players)

# Deprecated
def _print_rankings(players):

    print("Rank | Name                     | Rating")

    player_list = list(players.values())
    sorted_list = sorted(player_list, key=Player.get_rating, reverse=True)
    i = 1
    for player in sorted_list:
        rounded_rating = round(player.rating, 2)
        name = player.first + ' ' + player.last
        print("%4s | %-24s | %.2f" % \
            (str(i), name, rounded_rating))
        i += 1
