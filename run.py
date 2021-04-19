from computer import Computer
from human import Human
from player import Player


class Run:
    def __init__(self):
        self.player_one = Human("Player One")
        self.player_two = Computer()
        self.round = 1

    def run_game(self):
        rounds_to_win = self.rounds()
        player_one = Human("Player One")
        player_two = Computer()
        while player_one.wins < rounds_to_win and player_two.wins < rounds_to_win:
            self.player_choice_prompt()
            self.computer_choice()
            self.results()
            print(self.round)

    def player_choice_prompt(self):
        self.player_one.choice = self.player_one.gestures[int(input(f"Round {self.round}\n{self.player_one.name}: Make your choice!\n"
              f"1: rock\n"
              f"2. paper\n"
              f"3. scissors\n"
              f"4. lizard\n"
              f"5. spock\n"
              f":")) - 1]
        if self.player_one.validate_input():
            self.player_choice_prompt()

    def computer_choice(self):
        self.player_two.get_gesture()

    def results(self):
        print(f"{self.player_one.name}'s choice: {self.player_one.choice}\n"
              f"{self.player_two.name}'s choice: {self.player_two.choice}")
        if self.player_one.choice == self.player_two.choice:
            print("Draw! Go again!")
        else:
            self.compare_results()
            self.round += 1

    def compare_results(self):
        # TODO compare results to get correct response
        pass

    def rounds(self):
        try:
            number = int(input("Enter a number for how many rounds to win\n:"))
            return number
        except:
            print("Need a number")
            return self.rounds()



