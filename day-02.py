example = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip()


def parse_line(line):
    game_str, sets_str = line.split(":")
    game_id = int(game_str.split()[-1])
    sets_strs = sets_str.split(";")
    sets = []
    for s in sets_strs:
        cube_strs = s.strip().split(",")
        sets.append({col: int(n) for c in cube_strs for n, col in [c.split()]})
    return game_id, sets


def parse_games(text_in):
    return {
        game_id: cubes
        for line in text_in.split("\n")
        for game_id, cubes in [parse_line(line)]
    }


def set_is_possible(bag, cubes):
    for color, count in cubes.items():
        if count > bag[color]:
            return False
    else:
        return True


def game_is_possible(bag, cube_sets):
    return all(set_is_possible(bag, cubes) for cubes in cube_sets)


def part_one(text, bag):
    games = parse_games(text)

    possible_ids = [
        game_id
        for game_id, cube_sets in games.items()
        if game_is_possible(bag, cube_sets)
    ]

    sum_possible_ids = sum(possible_ids)
    print(possible_ids)
    print(sum_possible_ids)


bag = {"red": 12, "green": 13, "blue": 14}
part_one(example, bag)


with open("day-02.in", "rt") as f:
    part_one(f.read().strip(), bag)
