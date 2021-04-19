from computer import Computer
from human import Human


class Run:
    def __init__(self):
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def player_choice_prompt(self, player):
        player.gesture = self.gestures[int(input(f"{player.name}: Make your choice!\n"
              f"1: rock\n"
              f"2. paper\n"
              f"3. scissors\n"
              f"4. lizard\n"
              f"5. spock\n"
              f":")) - 1]
       # if player.validate_input(player.gesture, self.gestures):
        return player



