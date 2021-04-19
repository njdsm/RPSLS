from run import Run
from human import Human
from computer import Computer

if __name__ == '__main__':
    game = Run()
    player_one = Human("Player One")
    player_two = Computer()
    print(player_one.name)
    print(player_two.name)
    game.player_choice_prompt(player_one)
    print(player_one.gesture)
