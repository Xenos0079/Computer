# I need an original homework 1
import random

def display_intro():
    print("Welcome to the 8-tile sliding puzzle game!")
    print("The objective of the game is to arrange the numbers in sequential order.")
    print("You can use any four letters for left, right, up and down moves.")
    # Display the brief introduction about the game

def prompt_player_input():
    valid_input = False
    while not valid_input:
        user_input = input("Enter the four letters used for left, right, up and down move: ").strip().lower()
        # Perform input validation
        if len(user_input) == 4 and user_input.isalpha() and len(set(user_input)) == 4:
            valid_input = True
            # the input is valid
        else:
            print("Invalid input. Please enter 4 unique letters (a-z).")
            # report
        user_input = list(user_input)
    return user_input

def generate_puzzle():
    puzzle = list(range(1, 9)) + [None]
    auto = 0
    while auto < 100: # move the puzzle automatically
        ran_num = random.randint(0, 3)
        make_move(puzzle, ran_num)
        auto += 1
        # apply reverse engineering to ensure the puzzle is solvable
    return puzzle
    # generate the puzzle

def display_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x is not None else " " for x in puzzle[i:i+3]))
    # display the puzzle on the screen

def make_move(puzzle, dir):
    empty_index = puzzle.index(None)
    if dir == 0: # left
        if empty_index % 3 < 2:
            puzzle[empty_index], puzzle[empty_index + 1] = puzzle[empty_index + 1], puzzle[empty_index]
    elif dir == 1: # right
        if empty_index % 3 > 0:
            puzzle[empty_index], puzzle[empty_index - 1] = puzzle[empty_index - 1], puzzle[empty_index]
    elif dir == 2: # up 
        if empty_index < 6:
            puzzle[empty_index], puzzle[empty_index + 3] = puzzle[empty_index + 3], puzzle[empty_index]
    elif dir == 3: # down
        if empty_index >= 3:
            puzzle[empty_index], puzzle[empty_index - 3] = puzzle[empty_index - 3], puzzle[empty_index]

def is_solved(puzzle):
    return puzzle == list(range(1, 9)) + [None]
    # check if the puzzle is solved

def end_game():
    play_again = input("Enter 'n' for another game, or 'q' to end the game: ").strip().lower()
    if play_again == 'n':
        print()
        main()
        # replay the game
    elif play_again == 'q':
        print('\nThe game is end.')
        quit()
        # quit the game
    else:
        print()
        print("\nInvalid input. Please enter 'n' or 'q' to execute the process.")
        end_game()
        # report the invalid input

def main():
    display_intro() # display the introduction
    moves = prompt_player_input() # initialize the steps and get the corresponding letters
    puzzle = generate_puzzle() # generate the puzzle
    display_puzzle(puzzle) # print the puzzle
    move_count = 0 # initialize the count of the steps
    while not is_solved(puzzle): # start or continue the game
        move = input("Enter your move: ").strip().lower()
        while move not in moves: # invalid input
            move = input("Your input is invalid. Please enter the correct move: ").strip().lower()
        dir = moves.index(move) # get the direction
        make_move(puzzle, dir) # move the puzzle
        display_puzzle(puzzle) # renew the board
        move_count += 1 # add the count
    print("Congratulations! You solved the puzzle in " + str(move_count) + " qsteps.")
    end_game() # initialize the endgame process
    # define the main() function

main()
# START THE GAME