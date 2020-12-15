import os
import copy

os.chdir('./11')

# examplepuzzle2.txt
# examplepuzzle.txt
# puzzleinput.txt

with open('examplepuzzle2.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
rows = []
for i, p_input in enumerate(puzzleinput):
    rows.append([])
    for seat in p_input:
        rows[i].append(seat)

def checkforseat():
    pass

def checkseats(seatrow, seatcol):
    surround_seats = [
        (seatrow - 1, seatcol - 1),
        (seatrow - 1, seatcol),
        (seatrow - 1, seatcol + 1),
        (seatrow, seatcol - 1),
        (seatrow, seatcol + 1),
        (seatrow + 1, seatcol - 1),
        (seatrow + 1, seatcol),
        (seatrow + 1, seatcol + 1),
    ]
    occ_seats_count = 0
    for seat in surround_seats:
        if seat[0] not in range(0, len(rows)) or seat[1] not in range(0, len(rows[0])):
            continue
        cur_seat = rows[seat[0]][seat[1]]
        if cur_seat == "#":
            occ_seats_count += 1
    return occ_seats_count

for rnd in range(1):
    seat_assignment = copy.deepcopy(rows)
    seat_cnt = 0
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            occ_seats = checkseats(i, j)
            if col == 'L' and occ_seats == 0:
                seat_assignment[i][j] = '#'
                continue
            elif col == '#' and occ_seats >= 4:
                seat_assignment[i][j] = 'L'
            else:
                seat_assignment[i][j] = rows[i][j]
            if seat_assignment[i][j] == '#':
                seat_cnt += 1
    rows = copy.deepcopy(seat_assignment)
    print(seat_cnt)