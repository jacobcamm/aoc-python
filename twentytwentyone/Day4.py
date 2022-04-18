from pathlib import Path

filepath = Path('Day4.txt')
lines = [x for x in filepath.read_text().splitlines()]

called = lines[0].split(",")
grids = lines[2:]

width = len([x for x in grids[0].split(" ") if x != ""])

grid_single = [
    item for sublist in grids for item in sublist.split(" ") if item != ""]


grids = []
no_grids = int(len(grid_single) / (width * width))

for x in range(no_grids):
    start = x * width * width
    end = (x + 1) * width * width
    grids.append(grid_single[start:end])


def slice_per(source, step):
    return [source[i::step] for i in range(step)]


rounds_to_win = []
for index, grid in enumerate(grids):
    cols_to_check = slice_per(grid, 5)
    rows_to_check = [grid[i:i + 5] for i in range(0, len(grid), 5)]
    check = called[0:5]
    found = False
    for i in range(len(called) - 5):
        for col in cols_to_check:
            found = all(item in check for item in col)
            if found:
                break
        if found:
            rounds_to_win.insert(index, i + 5)
            break
        for row in rows_to_check:
            found = all(item in check for item in row)
            if found:
                break
        if found:
            rounds_to_win.insert(index, i + 5)
            break
        check.append(called[i + 5])

best = rounds_to_win[0]
winning_grid = 0
for index, rounds in enumerate(rounds_to_win):
    if (rounds > best):
        best = rounds
        winning_grid = index

unmarked = [int(x) for x in grids[winning_grid]
            if x not in called[0:best]]

print(sum(unmarked) * int(called[best - 1]))
