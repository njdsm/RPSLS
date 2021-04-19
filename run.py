from computer import Computer
from human import Human


class Run:
    def __init__(self):
        self.player_one = Human("Player One")
        self.player_two = Computer()
        self.round = 1

    def run_game(self):
        multiplayer = self.multiplayer()
        rounds_to_win = self.rounds()
        if multiplayer:
            self.player_two = Human("Player Two")
        while self.player_one.wins < rounds_to_win and self.player_two.wins < rounds_to_win:
            self.player_choice_prompt(self.player_one)
            if self.player_two.name == "Player Two":
                self.player_choice_prompt(self.player_two)
            else:
                self.computer_choice()
            self.results()
        self.display_winner()

    def multiplayer(self):
        try:
            user_input = int(input("play against computer or play locally against a friend"
                                   "(must provide your own friend)\n"
                                   "1: Singleplayer\n"
                                   "2: Multiplayer\n:"))
            if user_input == 1:
                return False
            else:
                return True
        except:
            print("Pick 1 or 2")
            return self.multiplayer()

    def display_winner(self):
        if self.player_one.wins > self.player_two.wins:
            print(f"{self.player_one.name} is the winner!")
        else:
            print(f"{self.player_two.name} is the winner!")

    def player_choice_prompt(self, player_turn):
        try:
            player_turn.choice = player_turn.gestures[int(input(f"Round {self.round}\n"
            f"Score: {self.player_one.wins} to {self.player_two.wins}\n"
            f"{player_turn.name}: Make your choice!\n"
            f"1: rock\n"
            f"2. paper\n"
            f"3. scissors\n"
            f"4. lizard\n"
            f"5. spock\n"
            f":")) - 1]
        except:
            print("Pick a number 1 - 5 please.")
            self.player_choice_prompt(player_turn)
        print("\n" * 100)


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

    def display_round_results(self, winner, winner_choice, loser, loser_choice, word):
        print(f"{winner}'s {winner_choice} {word} {loser}'s {loser_choice}")

    def rounds(self):
        try:
            number = int(input("Enter a number for how many rounds to win\n:"))
            if number < 2:
                print("At least 2 rounds please.")
                return self.rounds()
            return number
        except:
            print("Need a number")
            return self.rounds()

    def compare_results(self):
        if self.player_one.choice == "rock":
            if self.player_two.choice == "scissors" or self.player_two.choice == "lizard":
                self.player_one.wins += 1
                self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                           self.player_two.choice, "crushes")
            else:
                self.player_two.wins += 1
                if self.player_two.choice == "paper":
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "covers")
                else:
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "vaporizes")
        elif self.player_one.choice == "paper":
            if self.player_two.choice == "rock" or self.player_two.choice == "spock":
                self.player_one.wins += 1
                if self.player_two.choice == "rock":
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "covers")
                else:
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "disproves")
            else:
                self.player_two.wins += 1
                if self.player_two.choice == "lizard":
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "eats")
                else:
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "cuts")
        elif self.player_one.choice == "scissors":
            if self.player_two.choice == "paper" or self.player_two.choice == "lizard":
                self.player_one.wins += 1
                if self.player_two.choice == "paper":
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "cuts")
                else:
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "decapitate")
            else:
                self.player_two.wins += 1
                self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                           self.player_one.choice, "smashes")
        elif self.player_one.choice == "lizard":
            if self.player_two.choice == "spock" or self.player_two.choice == "paper":
                self.player_one.wins += 1
                if self.player_two.choice == "spock":
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "poisons")
                else:
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "eats")
            else:
                self.player_two.wins += 1
                if self.player_two.choice == "rock":
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "smashes")
                else:
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "decapitate")
        elif self.player_one.choice == "spock":
            if self.player_two.choice == "scissors" or self.player_two.choice == "rock":
                self.player_one.wins += 1
                if self.player_two.choice == "scissors":
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "smashes")
                else:
                    self.display_round_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                               self.player_two.choice, "vaporizes")
            else:
                self.player_two.wins += 1
                if self.player_two.choice == "paper":
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "disproves")
                else:
                    self.display_round_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                               self.player_one.choice, "poisons")
