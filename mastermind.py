# Always play against computer

# Welcome the player to the game

# Computer generate a random sequence

# Player makes their guess

# Computer grades the guess

# Player makes another guess (until player wins with a correct guess or player loses with 10 turns max)


# Possible functions:

import random

def generate_secret_code(possible_colors):
    secret_code = random.choices(possible_colors, k = 4)
    return secret_code

def play_turn(possible_colors):
    # Prompt for guess
    valid_move = False
    # while valid_move = False:
    guess_0 = input("Enter your guess for the first position: ")
    
    if guess_0 not in possible_colors: 
        print("Please choose an available color: R, Y, G, B, M, P")

    guess_1 = input("Enter your guess for the second position: ")
    guess_2 = input("Enter your guess for the third position: ")
    guess_3 = input("Enter your guess for the fourth position: ")
    # Check to make sure player's input is a valid color 
    pass

def analyze_turn():
    # If player guess is correct, update game_over to True
    return True

def show_game_state():
    pass

def main():
    # Define tracking variables
    game_over = False
    turn_number = 0
    possible_colors = ["R", "Y", "G", "B", "M", "P"]
    empty_board = [["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"],
    ["o", "o", "o", "o"]]

    print("Welcome to Mastermind!")
    print(empty_board)
    print("Here are the six available colors: Red (R), Yellow (Y), Green (G), Blue (B), Magenta (M), Purple (P)")

    secret_code = generate_secret_code(possible_colors)
    print(secret_code)

    while turn_number < 10 or not game_over:
        play_turn()
        game_over = analyze_turn()
        show_game_state()

main()