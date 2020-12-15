import os

os.chdir('./10')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
nums = []
for p_input in puzzleinput:
    nums.append(int(p_input))
nums.sort()

jolt_1 = 0
jolt_2 = 0
jolt_3 = 0
joltage = 0

for i, num in enumerate(nums):
    diff = num - joltage
    joltage = num
    if diff == 1:
        jolt_1 += 1
    elif diff == 2:
        jolt_2 += 1
    elif diff == 3:
        jolt_3 += 1
    if i == len(nums) - 1:
        jolt_3 += 1

print(jolt_1 * jolt_3)