from run import Run
from human import Human
from computer import Computer

if __name__ == '__main__':
    game = Run()
    round = 0
    rounds_to_win = game.rounds()
    print(rounds_to_win)
    player_one = Human("Player One")
    player_two = Computer()
    while player_one.wins < rounds_to_win and player_two.wins < rounds_to_win:
        game.player_choice_prompt(player_one)
        game.computer_choice(player_two)
        round = game.results(player_one, player_two, round)
        print(round)
