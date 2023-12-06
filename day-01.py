import itertools

example = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def part_one(text):
    sum_values = 0
    for line in text.split("\n"):
        if len(line) == 0:
            continue
        chars = list(line)
        digits = []
        for char in chars:
            try:
                digits.append(int(char))
            except ValueError:
                pass

        print(digits)
        value = int(f"{digits[0]}{digits[-1]}")
        print(value)

        sum_values += value
        # print(type(line))
        # print(list(line))

    print(sum_values)


digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digit_map_reversed = {k[::-1]: v for k, v in digit_map.items()}


def _find_first(line, digit_map):
    for cs in itertools.accumulate(line):
        try:
            return int(cs[-1])
        except ValueError:
            for k in digit_map:
                if k in cs:
                    return digit_map[k]


def part_two(text):
    sum_values = 0
    for line in text.split("\n"):
        if len(line) == 0:
            continue

        first_digit = _find_first(line, digit_map)
        last_digit = _find_first(line[::-1], digit_map_reversed)

        value = int(f"{first_digit}{last_digit}")
        print(value)

        sum_values += value
        # print(type(line))
        # print(list(line))

    print(sum_values)


part_one(example)

with open("day-01.in", "rt") as f:
    part_one(f.read())

part_two(example2)

with open("day-01.in", "rt") as f:
    part_two(f.read())
