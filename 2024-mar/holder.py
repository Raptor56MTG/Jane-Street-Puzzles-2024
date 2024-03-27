def generate_L_options(board: list[list[int]], level: int, row: int, col: int) -> list[tuple[int]]:
    """Given where we are in our search, This determines what our current options
    are, and if we need to move up a level or move down a level."""
    if level == 0:
        pass

def get_starting_points(board: list[list]) -> list[list[tuple[int, int]]]:
    """This looks at our board and grabs all of the possible starting
    L pieces and the corresponding coordinates for each depth and then
    iterates further until all possible configurations are chosen."""

    # start by listing dimensions of board
    rows = [i for i in range(len(board))]
    cols = [i for i in range(len(board[0]))]
    
    all_options = []

    # get the L pieces by getting the first and last items from each list and moving inward.

    for _ in range(len(board)):
        if len(all_options) == 0:
            row_options = [rows[0], rows[-1]]
            col_options = [cols[0], cols[-1]]
            for row in row_options:
                for col in col_options:
                    r = rows.copy()
                    c = cols.copy()
                    r.remove(row)
                    c.remove(col)
                    all_options.append([(row, col), r, c])
        else:
            updated = []
            for option in all_options:
                rows = option[-2]
                cols = option[-1]
                row_options = [rows[0], rows[-1]] if rows[0] != rows[-1] else [rows[0]]
                col_options = [cols[0], cols[-1]] if cols[0] != cols[-1] else [cols[0]]
                for row in row_options:
                    for col in col_options:
                        r = rows.copy()
                        c = cols.copy()
                        r.remove(row)
                        c.remove(col)
                        new_entry = []
                        new_entry.extend(option[:-2])
                        new_entry.extend([(row, col)])
                        if len(r) > 0 and len(c) > 0:
                            new_entry.extend([r, c])
                        updated.append(new_entry)

            all_options = updated

    return all_options