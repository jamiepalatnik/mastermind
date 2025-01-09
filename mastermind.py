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
    # If player guess is correct, update game_over to True
    # TODO: also need to give black/white peg feedback to the player
    return True


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
    print(secret_code)

    while turn_number < 10 and not game_over:
        turn_result = play_turn(possible_colors)
        # TODO: we need to update the board with the player's turn here
        game_over = analyze_turn(secret_code, turn_result)
        show_game_state()
        turn_number += 1


main()
