import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


def print_pause2(message_to_print):
    print(message_to_print)
    time.sleep(2)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        # Player stores own move and opponent move
        self.my_move = my_move
        self.their_move = their_move


class BasicPlayer(Player):
    # Basic Player selects move at random
    def move(self):
        return random.choice(self.moves)


class BartPlayer(Player):
    # Bart Player always picks rock
    def move(self):
        return 'rock'


class OrderedPlayer(Player):
    # Ordered Player cycles through the moves in order
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move == None:
            return random.choice(self.moves)
        elif self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class Order2Player(Player):
    # Similar to Ordered Player but skips 2 moves ahead
    def __init__(self):
        self.my_move = None
        
    def move(self):
        if self.my_move == None:
            return random.choice(self.moves)
        elif self.my_move == self.moves[0]:
            return self.moves[2]
        elif self.my_move == self.moves[1]:
            return self.moves[0]
        else:
            return self.moves[1]


class UserPlayer(Player):
    def move(self):
        user_input = input("Please enter rock, paper, or scissors:\n")
        if user_input.lower() in moves:
            return user_input.lower()
        else:
            print_pause2("Not a valid selection. Please enter "
                         "rock, paper, or scissors:\n")
            self.move()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(UserPlayer(), random.choice(
        [BasicPlayer(), BartPlayer(), OrderedPlayer(), Order2Player()])
    game.play_game()