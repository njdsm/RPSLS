from player import Player
import random


class Computer(Player):
    def __init__(self):
        self.name = "Player Two"
        super().__init__()

    def get_gesture(self):
        self.choice = self.gestures[random.randrange(0, 5)]
