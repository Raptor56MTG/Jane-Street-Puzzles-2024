################################################################
###                                                          ###
###                      HELPER FUNCTIONS                    ###
###                                                          ###
################################################################

def find_original_value_locations(board: list[list[int]]) -> list[tuple[int]]:
    """This returns a list of locations where the non empty
    squares are located."""
    value_locations = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col != '-':
                value_locations.append((i, j))
    return value_locations

def find_empty_space(board: list[list]) -> tuple[int, int] | None:
    """Traverse the board from left to right, top to bottom
    in order to find empty spaces."""
    row = len(board)
    column = len(board[0])
    for i in range(row):
        for j in range(column):
            if board[i][j] == '-':
                return (i, j)
    return None

def find_empty_space_in_L(board: list[list], current_option) -> tuple[int, int] | None:
    """Traverse the board from left to right, top to bottom
    in order to find empty spaces."""
    row = current_option[0]
    col = current_option[1]
    for i in range(len(board)):
        for j in range(len(board)):
            if (i == row or j == col) and board == '-':
                return (i, j)
    return None

def generate_choices(board: list[list]) -> list[int]:
    """This generates all of the choices in terms of our sequences."""
    return [i for i in range(len(board) + 1)][::-1]

def print_board(board: list[list]):
    """Display the board in a pretty fashion."""
    
    if len(board) == 5:
        for i, _ in enumerate(board):
            if (i == 3 or i == 2) and i > 0:
                print("-" * 12)
            for j, term in enumerate(board[i]):
                if (j == 3 or j == 2) and j > 0:
                    print("|", end="")
                print(term if len(str(term)) > 1 else f' {term}', end='')
            print("")
        print("")
    if len(board) == 9:
        for i, _ in enumerate(board):
            if i % 3 == 0 and i > 0:
                print("-" * 20)
            for j, term in enumerate(board[i]):
                if j % 3 == 0 and j > 0:
                    print("|", end="")
                print(term if len(str(term)) > 1 else f' {term}', end='')
            print("")
        print("")

################################################################
###                                                          ###
###                       VALIDATION LOGIC                   ###
###                                                          ###
################################################################

def sum_validation(board, value_locations, value, row, col):
    """Verify that each value location has a valid sum."""
    # validate sums for value locations
    for v in value_locations:

        current_value = board[v[0]][v[1]]
        sums = []

        # above
        above = (v[0] - 1, v[1]) if v[0] - 1 >= 0 else None
        if above is not None:
            sums.append(above)
        # below
        below = (v[0] + 1, v[1]) if v[0] + 1 < len(board) else None
        if below is not None:
            sums.append(below)
        # right
        right = (v[0], v[1] + 1) if v[1] + 1 < len(board) else None
        if right is not None:
            sums.append(right)
        # left
        left = (v[0], v[1] - 1) if v[1] - 1 >= 0 else None 
        if left is not None:
            sums.append(left)

        total = 0
        empty_spaces = 0
        
        for s in sums:
            sum_term = board[s[0]][s[1]]
            if sum_term == '-':
                if s[0] == row and s[1] == col:
                    total += value
                else:
                    empty_spaces += 1
            else:
                total += board[s[0]][s[1]]

        if ((total != current_value and empty_spaces == 0) or total > current_value):
            return False
    return True

def term_validation(board, value_locations):
    """Ensure that there are exactly x given values for term x."""
    # ensure that there are correct number of terms
    counting = {i: [] for i in range(0, len(board) + 1)}
    for i, line in enumerate(board):
        for j, term in enumerate(line):
            if (i, j) in value_locations or term == '-':
                continue
            else:
                counting[term].append(term)
    # get allowed terms
    choices = {i: i for i in range(1, len(board) + 1)}
    total = sum([i for i in choices])
    zero_options = len(board) ** 2 - len(value_locations) - total
    choices[0] = zero_options
    for number, v, in choices.items():
        if len(counting[number]) > v:
            return False
    return True

def l_validation(board: list[list[int]], value_locations: list[tuple[int, int]],  value: int, row: int, col: int):
    """This determines that the L pattern in the board is valid."""
    # list of row options
    rows = [i for i in range(len(board))]
    cols = [i for i in range(len(board))]

    while len(rows) > 0 and len(cols) > 0:

        # generate options
        L_piece_options = []
        for i in [rows[0], rows[-1]]:
            for j in [cols[0], cols[-1]]:
                L_piece_options.append((i, j))
        
        L_scores = {}

        # grab pieces in each L piece (exclude zero's and values and '-')
        for option in L_piece_options:
            L_score = []
            for i, row_val in enumerate(board):
                for j, term in enumerate(row_val):
                    if ((i, j) not in value_locations and (i == option[0] or j == option[1])
                        and (i in rows and j in cols)):
                        if term == '-':
                            if i == row and j == col and value != 0:
                                    L_score.append(value)
                        else:
                            if term != 0:
                                L_score.append(term)
            L_scores[option] = L_score

        # account for all empty sets
        empty_set_count = 0
        for option, scores in L_scores.items():
            if len(scores) == 0:
                empty_set_count += 1
        if empty_set_count == 4:
            return True
        
        # check for any valid L's
        valid_Ls = 0
        valid_option = {}
        
        for option, scores in L_scores.items():
            if len(set(scores)) == 1 and len(scores) > 0:
                valid_Ls += 1
                valid_option[option] = scores

        if valid_Ls == 0 and empty_set_count > 0:
            return True

        if valid_Ls == 0:
            # print(row, col, value)
            return False
        if valid_Ls == 1:
            # print(valid_Ls, valid_option, rows, cols, end="\n\n")
            for k in valid_option.keys():
                rows.remove(k[0])
                cols.remove(k[1])
        if valid_Ls > 1:
            # print(valid_Ls, valid_option, rows, cols, end="\n\n")
            i_c = 0
            for k in valid_option.keys():
                if i_c == 0:
                    rows.remove(k[0])
                    cols.remove(k[1])
                    i_c += 1
    return True


def valid(board: list[list[int]], value_locations: list[tuple[int, int]], value: int, row: int, col: int):
    
    # print_board(board)
    # print(row, col, value)
    # print(l_validation(board, value_locations, value, row, col))
    return (sum_validation(board, value_locations, value, row, col) and 
            term_validation(board, value_locations) and
            l_validation(board, value_locations, value, row, col))



    # ---------------GET L CONTRIAINT WORKING
    # if row == len(board) - 1 and col == len(board) - 1 and valid:
    #     L1 = []  # Top left L
    #     for i, term in enumerate(board[0]):
    #         if (0, i) in value_locations:
    #             continue
    #         else:
    #             L1.append(term)
    #     for j, _ in enumerate(board):
    #         if (j, 0) in value_locations:
    #             continue
    #         else:
    #             L1.append(board[j][0])
    #     L2 = []  # Top right L
    #     for i, term in enumerate(board[0]):
    #         if (0, i) in value_locations:
    #             continue
    #         else:
    #             L2.append(term)
    #     for j, _ in enumerate(board):
    #         if (j, len(board) - 1) in value_locations:
    #             continue
    #         elif j == len(board) - 1:
    #             L2.append(value)
    #         else:
    #             L2.append(board[j][len(board) - 1])
    #     L3 = []  # Bottom left L
    #     for i, term in enumerate(board[len(board) - 1]):
    #         if (len(board) - 1, i) in value_locations:
    #             continue
    #         elif i == len(board) - 1:
    #             L3.append(value)
    #         else:
    #             L3.append(term)
    #     for j, line in enumerate(board):
    #         if (j, 0) in value_locations:
    #             continue
    #         else:
    #             L3.append(board[j][0])
    #     L4 = []  # Bottom right L
    #     for i, term in enumerate(board[len(board) - 1]):
    #         if (len(board) - 1, i) in value_locations:
    #             continue
    #         elif i == len(board) - 1:
    #             L4.append(value)
    #         else:
    #             L4.append(term)
    #     for j, line in enumerate(board):
    #         if (j, len(board) - 1) in value_locations:
    #             continue
    #         elif j == len(board) - 1:
    #             L4.append(value)
    #         else:
    #             L4.append(board[j][len(board) - 1])
    
    #     L1 = [x for x in L1 if x != 0]
    #     L2 = [x for x in L2 if x != 0]
    #     L3 = [x for x in L3 if x != 0]
    #     L4 = [x for x in L4 if x != 0]

    #     all_LS = [L1, L2, L3, L4]
    #     unique = [set(L) for L in all_LS]
    #     count_same_elements = sum(1 for s in unique if len(s) == 1)
    #     if count_same_elements != 1:
    #         valid = False
    #     print(all_LS, unique)
    # for row in board:
    #     print(row)
    # print("\n\n")
    # print(value)

################################################################
###                                                          ###
###                           OLD CODE                       ###
###                                                          ###
################################################################


board = [
    ['-', 18, '-', '-', '-', '-', '-', 7, '-'],
    ['-', '-', '-', '-', 12, '-', '-', '-', '-'],
    ['-', '-', 9, '-', '-', '-', '-', 31, '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', 5, '-', 11, '-', 22, '-', 22, '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', 9, '-', '-', '-', '-', 19, '-', '-'],
    ['-', '-', '-', '-', 14, '-', '-', '-', '-'],
    ['-', '-', 22, '-', '-', '-', '-', 15, '-'],
]


# def solve(board: list[list], search_space_x: list[int], search_space_y: list[int],
#           traversed_x: list[int], traversed_y: list[int], L_options: list[int], current_option: int | None):

#     # generate current L option to start traversal
#     if current_option is None:
#         current_option = L_options[0]

#     find = find_empty_space_in_L(board, current_option)

#     # we have completed current L
#     if not find:


# x = generate_choices(board)
# print(x)

# print(find_value_locations(board))

# x = get_starting_points(board)
# for a in x:
#     print(a)
# print(len(x))

# search_space_x = [i for i in range(len(board))]
# search_space_y = [i for i in range(len(board))]
# traversed_x = []
# traversed_y = []
# L_options = []
# for i in [search_space_x[0], search_space_x[-1]]:
#     for j in [search_space_y[0], search_space_y[-1]]:
#         L_options.append((i, j))

# print(L_options)

################################################################
###                                                          ###
###                      IMPLEMENTATION                      ###
###                                                          ###
################################################################

def solve(board: list[list]):

    # find first empty space on board
    find = find_empty_space(board)
    
    if not find:
        return True
    else:
        row, col = find

    for choice in choices:
        if valid(board, value_locations, choice, row, col):
            board[row][col] = choice
            if solve(board):
                return True

            board[row][col] = '-'

    return False

# board
# board = [
#     [0, '-', '-', '-', '-'],
#     ['-', '-', 9, '-', 7],
#     [8, '-', '-', '-', '-'],
#     ['-', '-', 15, '-', 12],
#     [10, '-', '-', '-', '-'],
# ]

# have reference of value locations in original board
value_locations = find_original_value_locations(board)
# generate original list of choices on board
choices = generate_choices(board)

print_board(board)
solve(board)
print("___________________")
print_board(board)
