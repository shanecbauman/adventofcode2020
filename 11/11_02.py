import os
import copy

os.chdir('./11')

# examplepuzzle2.txt
# examplepuzzle.txt
# puzzleinput.txt

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
rows = []
for i, p_input in enumerate(puzzleinput):
    rows.append([])
    for seat in p_input:
        rows[i].append(seat)

def lookforseat(active_seat, direction):
    new_seat = (active_seat[0] + direction[0], active_seat[1] + direction[1])
    if new_seat[0] not in range(0, len(rows)) or new_seat[1] not in range(0, len(rows[0])):
        return None
    cur_seat = rows[new_seat[0]][new_seat[1]]
    if cur_seat == '.':
        return lookforseat(new_seat, direction)
    else:
        return cur_seat

def checkseats(seatrow, seatcol):
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    occ_seats_count = 0
    for direction in directions:
        cur_seat = lookforseat((seatrow, seatcol), direction)
        if cur_seat == None:
            continue
        if cur_seat == '.':
            cur_seat = lookforseat((seatrow, seatcol), direction)
        if cur_seat == "#":
            occ_seats_count += 1
    return occ_seats_count

for rnd in range(100):
    seat_assignment = copy.deepcopy(rows)
    seat_cnt = 0
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            occ_seats = checkseats(i, j)
            if col == 'L' and occ_seats == 0:
                seat_assignment[i][j] = '#'
                continue
            elif col == '#' and occ_seats >= 5:
                seat_assignment[i][j] = 'L'
            else:
                seat_assignment[i][j] = rows[i][j]
            if seat_assignment[i][j] == '#':
                seat_cnt += 1
    rows = copy.deepcopy(seat_assignment)
    print(rnd, seat_cnt)