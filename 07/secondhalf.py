import os
import re

os.chdir('./07')

with open('examplepuzzle_02.txt', 'r') as readfile:
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

bags_in_gold = []
total_bags = 0

def find_inner_bag_count(outer_bag, descriptions, bag_count):
    working_bag = list(filter(lambda bag: bag['color'] == outer_bag, descriptions))
    print(working_bag)
    for inner_bag in working_bag[0]['interior_bags']:
        next_working_bag = list(filter(lambda bag: bag['color'] == inner_bag['color'], descriptions))
        if len(next_working_bag[0]['interior_bags']) == 0:
            return 1
        bag_count += inner_bag['quantity'] * find_inner_bag_count(inner_bag['color'], descriptions, bag_count)
    return 1
    # if outer_bag['color'] == interior_bag or outer_bag['color'] in bags_in_gold:
    #     return
    # for inner_bag in outer_bag['interior_bags']:
    #     if len(inner_bag['interior_bags']) == 0:
    #         return bag_count * 1
    #     else:
    #         bag_count = bag_count + inner_bag['quantity'] * find_inner_bag_count(inner_bag, )
    #         # bags_in_gold.append(outer_bag['color'])
    #         for inner_inner_bag in inner_bag['interior_bags']:
    #             bag_count = bag_count + inner_inner_bag['quantity'] * find_inner_bag_count(inner_inner_bag, )
    #             pass
    #         for description in descriptions:
    #             find_inner_bag_count(description, outer_bag['color'])



# i = descriptions.index(['color'])

# for description in descriptions:
#     total_bags += find_inner_bag_count('shiny gold', description, 0)

total_bags += find_inner_bag_count('shiny gold', descriptions, 0)
print(total_bags)

# print(len(bags_in_gold))