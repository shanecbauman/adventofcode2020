import csv
import os
import sys

os.chdir('./01')
print(os.getcwd())

values = []

with open('puzzleinput.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(int(row[0]))

# print(values)

for value in values:
    for secondValue in values:
        sumResult = value + secondValue
        if sumResult == 2020:
            multipliedResult = value * secondValue
            print(multipliedResult)
            sys.exit()
            