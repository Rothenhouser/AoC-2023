import functools

example = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()

DIGITS = "1234567890"


def iterate_over_grid(input_as_grid):
    for i, l in enumerate(input_as_grid):
        for j, c in enumerate(l):
            yield i, j, c


def get_number_locations(input_as_grid):
    current_number = ""
    current_number_indices = set()
    number_locations = []
    for i, j, c in iterate_over_grid(input_as_grid):
        if c in DIGITS:
            current_number += c
            current_number_indices |= {(i, j)}
        else:
            if current_number == "":
                continue
            else:
                number_locations.append((int(current_number), current_number_indices))
                current_number = ""
                current_number_indices = set()
    return number_locations


def just_indices_around(i, j):
    return {
        (i + i_range, j + j_range) for j_range in [-1, 0, 1] for i_range in [-1, 0, 1]
    }


def get_indices_around(input_as_grid, symbols):
    indices_of_symbols = set()
    for i, j, c in iterate_over_grid(input_as_grid):
        if c in symbols:
            indices_of_symbols |= just_indices_around(i, j)
    return indices_of_symbols


def part_one(input_text):
    symbols = set(input_text) - set("1234567890.") - {"\n"}
    print(symbols)

    input_as_grid = list(map(list, input_text.split("\n")))

    number_locations = get_number_locations(input_as_grid)
    indices_of_symbols = get_indices_around(input_as_grid, symbols)

    adjacent_numbers = []
    for number, number_indices in number_locations:
        if len(number_indices & indices_of_symbols) > 0:
            adjacent_numbers.append(number)

    return sum(adjacent_numbers)


print(part_one(example))

with open("day-03.in", "rt") as f:
    print(part_one(f.read().strip()))


def part_two(input_text):
    input_as_grid = list(map(list, input_text.split("\n")))

    current_number = ""
    current_number_indices = set()
    numbers_by_locations = {}
    for i, j, c in iterate_over_grid(input_as_grid):
        if c in DIGITS:
            current_number += c
            current_number_indices |= {(i, j)}
        else:
            if current_number == "":
                continue
            else:
                numbers_by_locations |= {
                    idx: int(current_number) for idx in current_number_indices
                }
                current_number = ""
                current_number_indices = set()

    print(numbers_by_locations)

    sum_gear_ratios = 0
    for i, j, c in iterate_over_grid(input_as_grid):
        if c == "*":
            numbers_around_position = set()
            for indices in just_indices_around(i, j):
                try:
                    numbers_around_position |= {numbers_by_locations[indices]}
                except KeyError:
                    continue
            print(numbers_around_position)
            if len(numbers_around_position) == 2:
                sum_gear_ratios += functools.reduce(
                    lambda x, y: x * y, numbers_around_position
                )
            print(sum_gear_ratios)

            print(just_indices_around(i, j))
            pass

            # check in dict, see if n_numbers ==2
    return sum_gear_ratios


print(part_two(example))

with open("day-03.in", "rt") as f:
    print(part_two(f.read().strip()))
