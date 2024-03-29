import os
import re

os.chdir('./07')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read()
rules = puzzleinput.split('\n')

descriptions = []
for rule in rules:
    details = rule.split(' bags contain ')
    details[1] = re.sub(r' bags?\.', '', details[1])
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

bags_holding_gold = []

def find_outermost_bags(outer_bag, interior_bag):
    if outer_bag['color'] == interior_bag or outer_bag['color'] in bags_holding_gold:
        return
    for inner_bag in outer_bag['interior_bags']:
        if inner_bag['color'] == interior_bag:
            bags_holding_gold.append(outer_bag['color'])
            for description in descriptions:
                find_outermost_bags(description, outer_bag['color'])

for description in descriptions:
    find_outermost_bags(description, 'shiny gold')

print(len(bags_holding_gold))