from player import Player
import random

class Computer(Player):
    def __init__(self, player):
        self.name = "computer"
        self.player = player

    def get_gesture(self, list_of_gestures):
        choice = list_of_gestures[random.randrange(0, 5)]
        return choice
