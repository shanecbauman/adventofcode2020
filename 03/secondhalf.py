import csv
import os

os.chdir('./03')

totalTreesHit = 1
slopes = []

decents = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

with open('puzzleinput.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        slopes.append(row[0])

def check_for_tree(symbol):
    if symbol == "#":
        return 1
    else:
        return 0

for decent in decents:
    x = decent[0]
    y = decent[1]
    xLocation = 0
    treesHit = 0
    for i, horizontal_slope in enumerate(slopes):
        if i == 0:
            continue
        elif i % y == 0:
            xLocation += x
            try:
                treesHit += check_for_tree(horizontal_slope[xLocation])
            except IndexError:
                xLocation -= len(horizontal_slope)
                treesHit += check_for_tree(horizontal_slope[xLocation])
    totalTreesHit *= treesHit

print(totalTreesHit)