import os
import re
import operator

os.chdir('./09')

# puzzleinput.txt
# examplepuzzle.txt

with open('examplepuzzle.txt', 'r') as readfile:
    puzzleinput = readfile.read().split('\n')
nums = []
for p_input in puzzleinput:
    nums.append(int(p_input))

def match_nums(num_list, correct_sum):
    for num1 in num_list:
        for num2 in num_list:
            if num1 == num2:
                continue
            if num1 + num2 == correct_sum:
                return True
    return False

preamble = 5
for i, num in enumerate(nums):
    if i in range(0, preamble):
        continue
    if match_nums(nums[i - preamble:i], num) == False:
        print(num)
        break