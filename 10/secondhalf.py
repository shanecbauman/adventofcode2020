import os

os.chdir('./10')

# examplepuzzle.txt
# examplepuzzle_2.txt
# puzzleinput.txt

with open('examplepuzzle.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
nums = [[0]]

for p_input in puzzleinput:
    nums.append([int(p_input)])
nums.sort()
nums.append([nums[-1][0] + 3])


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