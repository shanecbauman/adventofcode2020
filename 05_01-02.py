import sys

with open("puzzleinput_05.txt", 'r') as readfile:
    puzzleinput = readfile.read()
seats = puzzleinput.split('\n')

seatid = []

def findseatid(currentseat, seatindex, rowmin, rowmax, columnmin, columnmax):
    if currentseat[seatindex] == 'F':
        rowmax -= (rowmax - rowmin) // 2
    elif currentseat[seatindex] == 'B':
        rowmin += (rowmax - rowmin) // 2
    elif currentseat[seatindex] == 'L':
        columnmax -= (columnmax - columnmin) // 2
    elif currentseat[seatindex] == 'R':
        columnmin += (columnmax - columnmin) // 2
    seatindex += 1
    if seatindex == len(currentseat):
        seatid = rowmin * 8 + columnmin
        return seatid
    else:
        return findseatid(currentseat, seatindex, rowmin, rowmax, columnmin, columnmax)
 
for seat in seats:
    seatid.append(findseatid(seat, 0, 0, 128, 0, 8))

sortedseats = sorted(seatid)
for i, seat in enumerate(sortedseats):
    if sortedseats[i+1] != seat + 1:
        print(seat + 1)
        sys.exit()