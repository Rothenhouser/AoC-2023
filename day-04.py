import functools

example = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip()


def part_one(text_input):
    def score(n_match):
        match n_match:
            case 0:
                return 0
            case _:
                return 2 ** (n_match - 1)

    total_wins = 0
    for line in text_input.split("\n"):
        _, numbers_str = line.split(":")

        # this was more fun to write than it is to read
        matching_numbers = functools.reduce(
            lambda winning_numbers, my_numbers: winning_numbers & my_numbers,
            map(
                lambda numbers: set(map(int, numbers)),
                map(lambda s: s.split(), numbers_str.split("|")),
            ),
        )
        total_wins += score(len(matching_numbers))

    return total_wins


print(part_one(example))

with open("day-04.in", "rt") as f:
    print(part_one(f.read().strip()))
