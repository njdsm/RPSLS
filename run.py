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

    def computer_choice(self, player_two):
        player_two.gesture = player_two.get_gesture(self.gestures)
        return player_two.gesture

    def results(self, player_one_choice, player_two_choice):
        if player_one_choice == player_two_choice:
            print("Draw! Go again!")
        else:
            self.compare_results(player_one_choice, player_two_choice)

    def compare_results(self, player_one_choice, player_two_choice):
        pass

    def rounds(self):
        try:
            number = int(input("Enter a number for how many rounds to win\n:"))
            return number
        except:
            print("Need a number")
            return self.rounds(number)



