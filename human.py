from player import Player


class Human(Player):
    def __init__(self, player):
        self.name = player
        super().__init__()


    # def validate_input(self, input, gestures):
    #     if gestures includes input:
    #         return True
    #     else:
    #         return False
