import os
import math

os.chdir('./13')

# examplepuzzle2.txt
# exampleinput.txt
# puzzleinput.txt

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
dept_time = int(puzzleinput[0])
puzzleinput.append(puzzleinput[1].split(','))
buses = []
for p_inpt in puzzleinput[2]:
    if p_inpt != 'x':
        num = int(p_inpt)
        bus_dept_time = math.ceil(dept_time / num) * num
        time_to_dept = bus_dept_time - dept_time
        buses.append({
            'id': int(p_inpt),
            'dept_time': bus_dept_time,
            'time_to_dept': time_to_dept
        })

for i, bus in enumerate(buses):
    if i == 0:
        erly_bus = bus
        continue
    elif bus['time_to_dept'] < erly_bus['time_to_dept']:
        erly_bus = bus

print(erly_bus['id'] * erly_bus['time_to_dept'])