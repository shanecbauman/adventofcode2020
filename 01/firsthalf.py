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
        sumResult = value + secondValue
        if sumResult == 2020:
            multipliedResult = value * secondValue
            print(multipliedResult)
            sys.exit()