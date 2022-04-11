from pathlib import Path
filepath = Path('Day1.txt')
conv_lines = [int(x) for x in filepath.read_text().splitlines()]
lines = [x for x in filepath.read_text().splitlines()]


def part_one(input):
    increased = 0
    prev = input[0]
    for reading in input[1:]:
        if reading > prev:
            increased += 1
        prev = reading

    return increased


def part_two(input, depth):
    increased = 0
    prev = input[0:depth]
    for reading in input[depth:]:
        new = prev[1:depth] + [reading]
        if sum(new) > sum(prev):
            increased += 1
        prev = new

    return increased


print("Day 1")
print(f"Part 1: {part_one(conv_lines)}")
print(f"Part 2: {part_two(conv_lines, 3)}")


def test(list1, list2):
    prev1 = list1[0]
    prev2 = list2[0]

    for f, b in zip(list1[1:], list2[1:]):
        test2(prev1, f, prev2, b)
        prev1 = f
        prev2 = b


def test2(prev1, new1, prev2, new2):
    if new1 < prev1:
        if new2 >= prev2:
            print(type(prev2))
            print(f"{prev1} {new1} {prev2} {new2}")


# test(conv_lines, lines)
