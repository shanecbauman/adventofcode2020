import os
import re
import operator
import sys

os.chdir('./09')

with open('puzzleinput.txt', 'r') as readfile:
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

preamble = 25
for i, num in enumerate(nums):
    if i in range(0, preamble):
        continue
    if match_nums(nums[i - preamble:i], num) == False:
        weaknum = num
        break

for i, num in enumerate(nums):
    num_sum = 0
    j = 0
    sum_list = []
    while num_sum < weaknum:
        sum_list.append(nums[i + j])
        num_sum += nums[i + j]
        if num_sum == weaknum:
            sum_list.sort()
            print(sum_list[0] + sum_list[-1])
            sys.exit()
        j += 1
    sum_list.clear()