import os

os.chdir('./06')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read()
groups = puzzleinput.split('\n\n')

def qs_answered_per_group(i, individual_answers, group_answers):
    for answer in individual_answers[i]:
        if answer not in group_answers:
            group_answers.append(answer)
    i += 1
    if i == len(individual_answers):
        return len(group_answers)
    else:
        return qs_answered_per_group(i, individual_answers, group_answers)

sum_of_qs_per_group = 0
for group in groups:
    individual_answers = group.split('\n')
    group_answers = []
    sum_of_qs_per_group += qs_answered_per_group(0, individual_answers, group_answers)

print(sum_of_qs_per_group)