import os
import re

os.chdir('./12')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
directions = []
for i, p_input in enumerate(puzzleinput):
    dirs = list(filter(None, re.split(r'([a-zA-Z]|\d+)', p_input)))
    directions.append(dirs)

class navigation():
    def __init__(self):
        self.boat_loc = [0, 0]
        self.rel_wypt_loc = [10, 1]
        # x axis, y axis
        self.direct_plns = [
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 1]
        ]

    def rotate_waypoint(self, direct, rot_amnt):
        rot_cnt = rot_amnt // 90
        for i, plane in enumerate(self.direct_plns):
            same_sign = (abs(self.rel_wypt_loc[0]) + abs(plane[0]) == 
                         abs(self.rel_wypt_loc[0] + plane[0]) and 
                         abs(self.rel_wypt_loc[1]) + abs(plane[1]) == 
                         abs(self.rel_wypt_loc[1] + plane[1]))
            if same_sign:
                cur_pln = i
                break
        new_pln = (cur_pln + (rot_cnt * direct)) % len(self.direct_plns)
        if (cur_pln - new_pln) % 2 == 0:
            wypt_x = abs(self.rel_wypt_loc[0]) * self.direct_plns[new_pln][0]
            wypt_y = abs(self.rel_wypt_loc[1]) * self.direct_plns[new_pln][1]
        else:
            wypt_x = abs(self.rel_wypt_loc[1]) * self.direct_plns[new_pln][0]
            wypt_y = abs(self.rel_wypt_loc[0]) * self.direct_plns[new_pln][1]
        self.rel_wypt_loc = [wypt_x, wypt_y]

    def mvship(self, value):
        boat_x = self.boat_loc[0] + (self.rel_wypt_loc[0] * value)
        boat_y = self.boat_loc[1] + (self.rel_wypt_loc[1] * value)
        self.boat_loc = [boat_x, boat_y]

    def move(self, action, value):
        if action == 'L':
            self.rotate_waypoint(-1, value)
        elif action == 'R':
            self.rotate_waypoint(1, value)
        if action == 'N':
            self.rel_wypt_loc[1] += value
        elif action == 'E':
            self.rel_wypt_loc[0] += value
        elif action == 'S':
            self.rel_wypt_loc[1] -= value
        elif action == 'W':
            self.rel_wypt_loc[0] -= value
        elif action == 'F':
            self.mvship(value)

navigate = navigation()
for direction in directions:
    navigate.move(direction[0], int(direction[1]))
print(abs(navigate.boat_loc[0]) + abs(navigate.boat_loc[1]))