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
        else:
            print("Invalid input. Please enter 4 unique letters (a-z).")
        user_input = list(user_input)
    return user_input

def generate_puzzle():
    puzzle = list(range(1, 9)) + [None]
    auto = 0
    while auto < 100:
        ran_num = random.randint(0, 3)
        make_move(puzzle, ran_num)
        auto += 1
    #random.shuffle(puzzle)
    return puzzle
    # Generate a randomized, SOLVABLE 8-tile puzzle

def display_puzzle(puzzle):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x is not None else " " for x in puzzle[i:i+3]))
    # Display the puzzle on the screen in a simple text format

#def make_move(puzzle, move, moves):
#def get_dir(move, moves):
    #empty_index = puzzle.index(None)
    #dir = moves.index(move)
    
def make_move(puzzle, dir):
    empty_index = puzzle.index(None)
    #if move == moves[1]:# right
    if dir == 1:
        if empty_index % 3 > 0:
            puzzle[empty_index], puzzle[empty_index - 1] = puzzle[empty_index - 1], puzzle[empty_index]
    #elif move == moves[0]:# left
    elif dir == 0:
        if empty_index % 3 < 2:
            puzzle[empty_index], puzzle[empty_index + 1] = puzzle[empty_index + 1], puzzle[empty_index]
    #elif move == moves[3]: # down
    elif dir == 3:
        if empty_index >= 3:
            puzzle[empty_index], puzzle[empty_index - 3] = puzzle[empty_index - 3], puzzle[empty_index]
    #elif move == moves[2]: # up
    elif dir == 2:
        if empty_index < 6:
            puzzle[empty_index], puzzle[empty_index + 3] = puzzle[empty_index + 3], puzzle[empty_index]
    else:
        print("Invalid move. Please enter 'left', 'right', 'up', or 'down'.")

def is_solved(puzzle):
    return puzzle == list(range(1, 9)) + [None]
    # Check if the puzzle is solved

def main():
    display_intro()
    moves = prompt_player_input()
    puzzle = generate_puzzle()
    display_puzzle(puzzle)
    while not is_solved(puzzle):
        move = input("Enter your move: ").strip().lower()
        dir = moves.index(move)
        #make_move(puzzle, move, moves)
        make_move(puzzle, dir)
        display_puzzle(puzzle)
    print("Congratulations! You solved the puzzle!")
    play_again = input("Enter 'n' for another game, or 'q' to end the game: ").strip().lower()
    if play_again == 'n':
        main()

main()