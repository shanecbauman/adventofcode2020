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

def find_inner_bag_count(outer_bag, descriptions):
    bag_count = 0
    if len(outer_bag['interior_bags']) == 0:
        return bag_count
    for i, inner_bag in enumerate(outer_bag['interior_bags']):
        next_working_bag = list(filter(lambda bag: bag['color'] == inner_bag['color'], descriptions)).pop(0)
        if i == len(outer_bag['interior_bags']) - 1:
            return bag_count + inner_bag['quantity'] + (inner_bag['quantity'] * find_inner_bag_count(next_working_bag, descriptions))
        else:
            bag_count = bag_count + inner_bag['quantity'] + (inner_bag['quantity'] * find_inner_bag_count(next_working_bag, descriptions))

gold_bag = list(filter(lambda bag: bag['color'] == 'shiny gold', descriptions)).pop(0)
print(find_inner_bag_count(gold_bag, descriptions))