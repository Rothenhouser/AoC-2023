from dataclasses import dataclass

example = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip()


@dataclass
class Shmap:
    # sheed to shoil etc
    dest_start: int
    source_start: int
    range_len: int


def seed_to_new(old, shmaps):
    for shmap in shmaps:
        if shmap.source_start <= old <= shmap.source_start + shmap.range_len:
            return old + shmap.dest_start - shmap.source_start
    else:
        return old


def eval_all_shmaps_r(initial_old, shmapss):
    if len(shmapss) == 0:
        return initial_old
    else:
        new = seed_to_new(initial_old, shmapss[0])
        return eval_all_shmaps_r(new, shmapss[1:])


def eval_all_shmaps(seed, shmapss):
    for shmaps in shmapss:
        seed = seed_to_new(seed, shmaps)
    return seed


def part_one(input_text):
    seeds, *shmap_blocks = input_text.split("\n\n")

    seeds = map(int, seeds.split()[1:])

    all_shmaps = [
        [Shmap(*map(int, line.split())) for line in shmaps.split("\n")[1:]]
        for shmaps in shmap_blocks
    ]

    locations = [eval_all_shmaps(seed, all_shmaps) for seed in seeds]
    return min(locations)


print(part_one(example))

with open("day-05.txt", "rt") as f:
    print(part_one(f.read().strip()))
