from Game import *
from statistics import mean

class Player:

    def __init__(self, first, last, id_num):
        self.first = first
        self.last = last
        self.id_num = id_num
        self.games = []
        self.rating = 1000.0

    def add_game(self, game):
        self.games.append(game)

    def update_rating(self):

        game_ratings = []

        for game in self.games:
            game_rating = game.get_game_rating(self)
            game_ratings.append(game_rating)

        self.rating = mean(game_ratings)

    def get_rating(self):
        return self.rating

    def __str__(self):
        output = self.last + ',' + self.first + ': ' + str(self.rating)
        return output

    def __repr__(self):
        return self.__str__()
