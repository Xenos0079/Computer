def is_valid (proposed_row, proposed_col, already_placed_queen_cols):
    for earlier_row in range(0,proposed_row):
        already_placed_queen_col = already_placed_queen_cols[earlier_row]

        if proposed_col == already_placed_queen_col:
            return False

        column_dist = abs(proposed_col - already_placed_queen_col)
        row_dist = proposed_row - earlier_row

        if column_dist == row_dist:
            return False

    return True


def get_arrangements (row, already_placed_queen_cols, grid_size):
    if row == grid_size:
        yield already_placed_queen_cols
        return

    for col in range(0,grid_size):
        if is_valid(row,col, already_placed_queen_cols):
            already_placed_queen_cols[row] = col 
            yield from get_arrangements (row+1, already_placed_queen_cols, grid_size)

def eight_queen():
    global grid_size
    already_placed_queen_cols = [-1 for i in range(0,grid_size)]    
    return get_arrangements (0, already_placed_queen_cols, grid_size)

grid_size = 8
arrangements = eight_queen()

for arrangement in arrangements:
    position_list = []
    for row in range(0,grid_size):
        position_list.append((row+1, arrangement[row]+1))
    print (position_list)
