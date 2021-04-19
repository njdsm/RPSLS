from player import Player


class Human(Player):
    def __init__(self, player):
        self.name = player
        super().__init__()

    def validate_input(self):
        if self.choice in self.gestures:
            return False
        else:
            return True
