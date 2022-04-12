from pathlib import Path
filepath = Path('Day3.txt')
lines = [[int(char) for char in x] for x in filepath.read_text().splitlines()]

totals = [0 for x in lines[0]]

column_count = len(lines)


for row in lines:
    for index, digit in enumerate(row):
        totals[index] = totals[index] + digit

most_common = ["1" if x / column_count > 0.5 else "0" for x in totals]

least_common = ["0" if x == "1" else "1" for x in most_common]


def convert(input):
    return int(''.join(input), 2)


most_common_binary = convert(most_common)
least_common_binary = convert(least_common)

answer = most_common_binary * least_common_binary

print(answer)


def find_most_common(lines, position):
    total = 0
    for row in lines:
        total = total + row[position]

    return 1 if total / len(lines) >= 0.5 else 0


def find_value(lines, keepMostCommon):
    for x in range(0, len(lines[0])):
        most_common = find_most_common(lines, x)
        check = 0
        if keepMostCommon:
            check = most_common
        else:
            check = 1 if most_common == 0 else 0
        lines = [line for line in lines if line[x] == check]
        if len(lines) == 1:
            return map(str, lines[0])


oxygen = convert(find_value(lines, True))
c02 = convert(find_value(lines, False))

life_support = oxygen * c02

print(life_support)
