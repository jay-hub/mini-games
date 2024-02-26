from game_base import GameBase
from hangman import HangMan
from story_teller import StoryTeller
from tic_tac_toe import TicTagToe

if __name__ == "__main__":
    game = 1
    current_game: GameBase | None = None
    while game and game != "0":
        print("Pick a game to play: [1] Hangman, [2] TicTacToe, [3] Story Teller, [0] Quit")
        game = input()
        if game == "1":
            print("Starting Hangman")
            current_game = HangMan()
            current_game.start_game()
        if game == "2":
            print("Starting TicTacToe")
            current_game = TicTagToe()
            current_game.start_game()
        if game == "3":
            print("Starting Story Teller")
            current_game = StoryTeller()
            current_game.start_game()
        if game == "0":
            print('Thanks for playing !')
            break
