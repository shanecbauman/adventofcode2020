import os
import re

os.chdir('./07')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read()
rules = puzzleinput.split('\n')

descriptions = []
for rule in rules:
    details = rule.split(' bags contain ')
    details[1] = details[1].strip(' bags.')
    bags = re.split(r' bags?, ', details[1])
    interior_bags = []
    for bag in bags:
        if re.search(r'^\d', bag):
            quantity, color = bag.split(maxsplit=1)
            interior_bags.append({
                "color": color,
                "quantity": int(quantity)
            })
    descriptions.append({
        "color": details[0],
        "interior_bags": interior_bags
    })

for description in descriptions:
    print(description)