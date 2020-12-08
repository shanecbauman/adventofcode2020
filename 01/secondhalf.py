import csv
import os
import sys

os.chdir('./01')

values = []

with open('puzzleinput.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(int(row[0]))

for value in values:
    for secondValue in values:
        for thirdValue in values:
            sumResult = value + secondValue + thirdValue
            if sumResult == 2020:
                multipliedResult = value * secondValue * thirdValue
                print(multipliedResult)
                sys.exit()