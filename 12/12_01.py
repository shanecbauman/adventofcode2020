import os
import re

os.chdir('./12')

# examplepuzzle2.txt
# exampleinput.txt
# puzzleinput.txt

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
directions = []
for i, p_input in enumerate(puzzleinput):
    dirs = list(filter(None, re.split(r'([a-zA-Z]|\d+)', p_input)))
    directions.append(dirs)

class navigation():
    def __init__(self):
        self.boat_loc = [0, 0]
        self.boat_dir = [1, 0]
        self.boat_deg = 90
        # Degrees, x axis, y axis
        self.cardinal_dirs = [
            [0, 0, 1],
            [90, 1, 0],
            [180, 0, -1],
            [270, -1, 0]
        ]

    def check_dir(self):
        for card_dir in self.cardinal_dirs:
            if card_dir[0] == self.boat_deg:
                self.boat_dir = card_dir[1:]
                return

    def move(self, action, value):
        if action == 'L':
            self.boat_deg = (self.boat_deg - value) % 360
            self.check_dir()
        elif action == 'R':
            self.boat_deg = (self.boat_deg + value) % 360
            self.check_dir()
        if action == 'N':
            self.boat_loc[1] += value
        elif action == 'E':
            self.boat_loc[0] += value
        elif action == 'S':
            self.boat_loc[1] -= value
        elif action == 'W':
            self.boat_loc[0] -= value
        elif action == 'F':
            mv_amt = [element * value for element in self.boat_dir]
            for i in range(0, len(self.boat_loc)):
                self.boat_loc[i] += mv_amt[i]

navigate = navigation()
for direction in directions:
    navigate.move(direction[0], int(direction[1]))
print(abs(navigate.boat_loc[0]) + abs(navigate.boat_loc[1]))