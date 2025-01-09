# Always play against computer

# Welcome the player to the game

# Computer generate a random sequence

# Player makes their guess

# Computer grades the guess

# Player makes another guess (until player wins with a correct guess or player loses with 10 turns max)


# Possible functions:

import random


def generate_secret_code(possible_colors):
    secret_code = random.choices(possible_colors, k=4)
    return secret_code


def play_turn(possible_colors):
    # Prompt for guess
    guesses = []
    valid_move = False
    print("Possible colors: R, Y, G, B, M, P")
    while not valid_move:
        for i in range(4):
            local_guess = None
            # keep track of the number of tries for each position to provide error message for invalid input:
            num_tries = 0
            # Check to make sure player's input is a valid color
            while local_guess not in possible_colors:
                # first try
                if num_tries == 0:
                    local_guess = input(f"Enter your guess for position {i}: ").upper()
                # subsequent tries
                else:
                    print("Oops! Please enter a possible color")
                    print("Possible colors: R, Y, G, B, M, P")
                    local_guess = input(f"Enter your guess for position {i}: ").upper()
                num_tries += 1
            # add the guess to guesses only after we know it's valid
            guesses.append(local_guess)
        # stop when we've collected 4 guesses
        if len(guesses) >= 4:
            valid_move = True
    print("You guessed:\n")
    print(guesses)
    return guesses


def analyze_turn(secret_code, turn_result):
    # Compare turn_result to secret_code
    # If player guess is correct, return True, which will end the game
    if secret_code == turn_result:
        return True
    else: 
        # Check if any of the guesses match the correct color and position of the secret_code
        correct_positions = 0
        still_secret = []
        for code, guess in zip(secret_code, turn_result):
            if code == guess:
                correct_positions += 1
            else:
                still_secret.append(code)
                print(still_secret)

            # Print for debugging/development help
            print(f"Player guess: {guess} | Secret code: {code}")

            # If the guess matches the color and position, award a black peg
            print(f"Correct color & position (black pegs): {correct_positions}")

    
        # Check if any of the letters match the correct color but not position of the secret_code
        # Please update!
        for code, guess in zip(still_secret, turn_result):
            if code == guess:
                correct_positions += 1
            else:
                still_secret.append(code)
                print(still_secret)

            # If the guess matches the color but the position is incorrect, award a white peg


        # Return false since secret code has not been guessed and game is still in progress
        return False, 

    # TODO: also need to give black/white peg feedback to the player



def show_game_state():
    pass


def main():
    # Define tracking variables
    game_over = False
    turn_number = 0
    possible_colors = ["R", "Y", "G", "B", "M", "P"]
    empty_board = [
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
        ["o", "o", "o", "o"],
    ]

    print("Welcome to Mastermind!")
    print(empty_board)
    print(
        "Here are the six available colors: Red (R), Yellow (Y), Green (G), Blue (B), Magenta (M), Purple (P)"
    )

    secret_code = generate_secret_code(possible_colors)
    # Print secret_code to help with assessing if game is working
    # TODO: Remove this when game is working as expected
    print(f"This is the secret code: {secret_code}")

    while turn_number < 10 and not game_over:
        turn_result = play_turn(possible_colors)
        # TODO: we need to update the board with the player's turn here
        game_over = analyze_turn(secret_code, turn_result)
        show_game_state()
        turn_number += 1
    
    print("Game over.")


main()
