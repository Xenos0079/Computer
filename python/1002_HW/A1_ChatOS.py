import random

def display_intro():
    print("Welcome to the 8-tile sliding puzzle game!")
    print("The objective of the game is to arrange the numbers in sequential order.")
    print("You can use any four letters for left, right, up and down moves.")

def get_user_moves():
    while True:
        moves = input("Enter the four letters used for left, right, up and down move: ").strip().lower()
        if len(moves) != 4 or not moves.isalpha() or len(set(moves)) < 4:
            print("Please enter exactly four unique letters.")
        else:
            return moves

def generate_puzzle():
    puzzle = list(range(1, 9))
    random.shuffle(puzzle)
    return puzzle

def display_puzzle(puzzle):
    for i in range(0, 8, 3):
        print(*puzzle[i:i+3])
        print()

'''
def make_move(puzzle, move):
    empty_index = puzzle.index(8)
    if move == 'l' and empty_index % 3 != 0:
        puzzle[empty_index], puzzle[empty_index-1] = puzzle[empty_index-1], puzzle[empty_index]
    elif move == 'r' and empty_index % 3 != 2:
        puzzle[empty_index], puzzle[empty_index+1] = puzzle[empty_index+1], puzzle[empty_index]
    elif move == 'u' and empty_index > 2:
        puzzle[empty_index], puzzle[empty_index-3] = puzzle[empty_index-3], puzzle[empty_index]
    elif move == 'd' and empty_index < 6:
        puzzle[empty_index], puzzle[empty_index+3] = puzzle[empty_index+3], puzzle[empty_index]
    else:
        print("Invalid move. Please try again.")
        return False
    return True
'''

def make_move(puzzle, move):
    empty_index = puzzle.index(0)
    if move == 'l' and empty_index % 3 != 0:
        target_index = empty_index - 1
    elif move == 'r' and empty_index % 3 != 2:
        target_index = empty_index + 1
    elif move == 'u' and empty_index > 2:
        target_index = empty_index - 3
    elif move == 'd' and empty_index < 6:
        target_index = empty_index + 3
    else:
        print("Invalid move. Please try again.")
        return False

    # 进行目标数字和空格子的交换
    puzzle[empty_index], puzzle[target_index] = puzzle[target_index], puzzle[empty_index]
    return True


def is_solved(puzzle):
    return puzzle == [1, 2, 3, 4, 5, 6, 7, 8]

def move_string(s: str, moves: str) -> str:
    # 将字符串转换为列表方便操作
    string_list = list(s)
    # 初始化位置指针
    row, col = 0, 0
    # 定义移动方向的映射关系
    directions = {'l': [0, -1], 'r': [0, 1], 'u': [-1, 0], 'd': [1, 0]}

    for move in moves:
        # 根据用户输入的移动指令进行移动
        if move in directions:
            # 计算新的位置坐标
            new_row = row + directions[move][0]
            new_col = col + directions[move][1]
        
            # 检查新的位置是否越界
            if 0 <= new_row < len(string_list) and 0 <= new_col < len(string_list[new_row]):
                # 交换当前位置和新位置上的字母
                string_list[row][col], string_list[new_row][new_col] = string_list[new_row][new_col], string_list[row][col]
                # 更新位置指针
                row, col = new_row, new_col

    # 将列表转换回字符串并返回结果
    return ''.join([''.join(row) for row in string_list])

def main():
    display_intro()
    while True:
        moves = get_user_moves()
        puzzle = generate_puzzle()
        moves_made = 0
        while not is_solved(puzzle):
            print("Current puzzle:")
            display_puzzle(puzzle)
            move = input(f"Enter your move: ").strip().lower()
            if make_move(puzzle, move):
                moves_made += 1
            else:
                continue
        print("Congratulations! You solved the puzzle in", moves_made, "moves!")
        choice = input("Enter 'n' for another game, or 'q' to end the game: ").strip().lower()
        if choice == 'q':
            break


main()
