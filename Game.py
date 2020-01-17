import math

class Game:

    # keeps track of players and score
    def __init__(self, p1, p1_score, p2, p2_score):
        self.p1 = p1
        self.p1_score = p1_score
        self.p2 = p2
        self.p2_score = p2_score

    def get_winner(self):
        if self.p1_score > self.p2_score:
            return self.p1
        else:
            return self.p2

    def get_differential(self):

        # Get ratio
        r1 = self.p1_score / (self.p2_score - 1)
        r2 = self.p2_score / (self.p1_score - 1)
        ratio = min(r1, r2)

        # Get differential
        numerator = math.sin(min(1, (1 - ratio) / 0.5) * 0.4 * math.pi)
        denominator = math.sin(0.4 * math.pi)
        frac = numerator / denominator
        differential = 125 + (475 * frac)
        return differential

    def get_game_rating(self, player):

        # If winner add score differential
        if player is self.get_winner():
            # player is p1, add to rating of p2
            if player is self.p1:
                return self.p2.rating + self.get_differential()
            # player is p2, add to rating of p1
            else:
                return self.p1.rating + self.get_differential()
        # If loser subtract score differential
        else:
            # player is p1, subtract from rating of p2
            if player is self.p1:
                return self.p2.rating - self.get_differential()
            # player is p2, subtract from rating of p1
            else:
                return self.p1.rating - self.get_differential()

    def __str__(self):
        left = self.p1.last + " " + str(self.p1_score)
        right = str(self.p2_score) + " " + self.p2.last
        return left + "-" + right

    def __repr__(self):
        return self.__str__()
