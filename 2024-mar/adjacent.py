

def adjacent_four(value: int) -> list[tuple[int]]:
    """This function takes a number and outputs a list of possible
    values of four different numbers 1 - 9 that can sum up to it. The sum
    must be of the form x + x + y + z = value"""
    
    valid_sums = []

    doubles = [2, 3, 4, 5, 6, 7, 8, 9]
    singles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in doubles:
        # remove our double value from the singles list
        updated_singles = singles.copy()
        updated_singles.remove(i)
        for index, j in enumerate(updated_singles):
            # move up by 1 to prevent duplicate and reference index
            for k_index in range(index + 1, len(updated_singles)):
                if 2 * i + j + updated_singles[k_index] == value:
                    valid_sums.append([i, i, j, updated_singles[k_index]])

    return valid_sums


def adjacent_three_edge(value: int) -> list[tuple[int]]:
    """This function takes a number and outputs a list of possible
    values of three different numbers 1 - 9 that can sum up to it. The sum
    must be of the form x + y + z = value"""
    
    valid_sums = []
    for i in range(1, 10):
        for j in range(i + 1,  10):
            for k in range(j + 1, 10):
                if i + j + k == value:
                    valid_sums.append([i, j, k])
    return valid_sums


def adjacent_two_edge(value: int) -> list[tuple[int]]:
    """This function takes a number and outputs a list of possible
    values of three different numbers 1 - 9 that can sum up to it. The sum
    must be of the form 2x + y = value"""
    
    valid_sums = []

    doubles = [2, 3, 4, 5, 6, 7, 8, 9]
    singles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in doubles:
        # remove our double value from the singles list
        updated_singles = singles.copy()
        updated_singles.remove(i)
        for j in updated_singles:
            if 2 * i + j == value:
                valid_sums.append([i, i, j])

    return valid_sums



def main():
    
    # all the numbers in our layout
    centers = [5, 9, 11, 12, 14, 19, 22, 31]
    edges = [7, 15, 18, 22]
    print("-----------------2X+Y+Z=VALUE-----------------")
    for term in centers:
        sums = adjacent_four(term)
        for sum in sums:
            print(term, sum)
    print("-----------------X+Y+Z=VALUE-----------------")
    for term in edges:
        sums = adjacent_three_edge(term)
        for sum in sums:
            print(term, sum)
    print("-----------------2X+Y=VALUE-----------------")
    for term in edges:
        sums = adjacent_two_edge(term)
        for sum in sums:
            print(term, sum)

if __name__ == '__main__':
    main()