with open("puzzleinput_05.txt", 'r') as readfile:
    puzzleinput = readfile.read()
seats = puzzleinput.split('\n')

seatid = []

rows = []
[rows.append(row) for row in range(0, 127 + 1)]
columns = []
[columns.append(column) for column in range(0, 7 + 1)]

def findseatid(currentseat, seatindex, seatrow, seatcolumn):
    if currentseat[seatindex] == 'F':
        del seatrow[len(seatrow) // 2:len(seatrow)]
    elif currentseat[seatindex] == 'B':
        del seatrow[0:len(seatrow) // 2]
    elif currentseat[seatindex] == 'L':
        del seatcolumn[len(seatcolumn) // 2:len(seatcolumn)]
    elif currentseat[seatindex] == 'R':
        del seatcolumn[0:len(seatcolumn) // 2]
    seatindex += 1
    if seatindex == len(currentseat):
        seatid = seatrow[0] * 8 + seatcolumn[0]
        return seatid
    else:
        return findseatid(currentseat, seatindex, seatrow, seatcolumn)
    
for seat in seats:
    seatrows = rows[:]
    seatcolumns = columns[:]
    seatid.append(findseatid(seat, 0, seatrows, seatcolumns))

print(max(seatid))