import os

os.chdir('./10')

# examplepuzzle.txt
# examplepuzzle_2.txt
# puzzleinput.txt

with open('puzzleinput.txt', 'r') as readfile:
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
variations = 0

def lookback(last_3, joltage):
    count = 0
    for num in last_3:
        if num[0] >= joltage - 3:
            count += num[1]
    return count

for i, num in enumerate(nums):
    if i == 0:
        num.append(1)
    else:
        lbk_count = i - 3
        if lbk_count < 0:
            lbk_count = 0
        num.append(lookback(nums[lbk_count:i], num[0]))
    variations += num[1]
    diff = num[0] - joltage
    joltage = num[0]
    if diff == 1:
        jolt_1 += 1
    elif diff == 2:
        jolt_2 += 1
    elif diff == 3:
        jolt_3 += 1
    if i == len(nums) - 1:
        jolt_3 += 1

# print(jolt_1 * jolt_3)
print(nums[-1][1])