from collections import namedtuple


def square_sum(n: int, size_restriction: int) -> list[int]:
    """Returns all of the combinations of square numbers
    that can sum up to equal our given number. In our case,
    we only care about the square numbers 1, 4, and 9."""
    
    Square = namedtuple('Square', ['size', 'value'])
    
    terms = [Square(1, 1), Square(2, 4), Square(3, 9)]
    combinations = set([(Square(1, 1),), (Square(2, 4),), (Square(3, 9),)])

    terminated = False
    completed = set()
    while not terminated:
        updated = set()
        for combination in combinations:
            for term in terms:
                value_total = sum([x.value for x in combination])
                size_total = sum([x.size for x in combination])
                if value_total + term.value <= n and size_total + term.size <= size_restriction:
                    updated.add(tuple(sorted(list(combination + (term,)))))
                if value_total == n and size_total <= size_restriction:
                    completed.add(combination)
        if len(updated) == 0:
            terminated = True
        else:
            combinations = updated

    for combination in completed:
        print(n, [x.value for x in combination])


if __name__ == "__main__":
    numbers = sorted(list(set([13, 20, 22, 28, 30, 36, 35, 39, 49, 39, 39, 23, 32, 23, 17, 13, 
               14, 24, 24, 39, 43, 22, 23, 29, 28, 34, 36, 29, 26, 26, 24, 20])))
    size_restriction = 17
    for number in numbers:
        square_sum(number, size_restriction)
