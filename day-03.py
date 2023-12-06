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


def part_one(input_text):
    symbols = set(input_text) - set("1234567890.") - {"\n"}
    print(symbols)

    input_as_grid = list(map(list, input_text.split("\n")))

    indices_of_symbols = set()
    for i, j, c in iterate_over_grid(input_as_grid):
        if c in symbols:
            for i_range in [-1, 0, 1]:
                for j_range in [-1, 0, 1]:
                    indices_of_symbols |= {(i + i_range, j + j_range)}

    # print(indices_of_symbols)

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

    # print(number_locations)

    adjacent_numbers = []
    for number, number_indices in number_locations:
        if len(number_indices & indices_of_symbols) > 0:
            adjacent_numbers.append(number)

    return sum(adjacent_numbers)


print(part_one(example))

with open("day-03.in", "rt") as f:
    print(part_one(f.read().strip()))
