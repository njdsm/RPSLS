from run import Run

if __name__ == '__main__':
    again = True
    while again:
        game = Run()
        game.run_game()
        user_input = input("\n\n\nWould you like to play again? y/n\n:")
        if user_input != "y":
            again = False
