import csv
import os

os.chdir('./03')

slopes = []
x = 3
xLocation = 0
treesHit = 0

with open('puzzleinput.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        slopes.append(row[0])

def check_for_tree(symbol):
    if symbol == "#":
        return 1
    else:
        return 0

for i, horizontal_slope in enumerate(slopes):
    if i == 0:
        continue
    xLocation += x
    try:
        treesHit += check_for_tree(horizontal_slope[xLocation])
    except IndexError:
        xLocation -= len(horizontal_slope)
        treesHit += check_for_tree(horizontal_slope[xLocation])

print(treesHit)