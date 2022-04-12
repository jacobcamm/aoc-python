from pathlib import Path
filepath = Path('Day2.txt')
lines = [x for x in filepath.read_text().splitlines()]

print(lines)


def part_one():
    horizonal = 0
    depth = 0

    for ins in lines:
        dir, amount = ins.split(" ")

        if (dir == "forward"):
            horizonal += int(amount)
        elif (dir == "down"):
            depth -= int(amount)
        else:
            depth += int(amount)

    print(horizonal * depth)


def part_two():
    horizonal = 0
    depth = 0
    aim = 0

    for ins in lines:
        dir, amount = ins.split(" ")

        if (dir == "forward"):
            horizonal += int(amount)
            depth += aim * int(amount)
        elif (dir == "down"):
            aim += int(amount)
        else:
            aim -= int(amount)

    print(horizonal * depth)

part_one()
part_two()