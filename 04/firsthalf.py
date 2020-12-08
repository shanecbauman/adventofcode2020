import os
import re

os.chdir('./04')

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

with open("puzzleinput.txt", 'r') as readfile:
    puzzleinput = readfile.read()
passports = puzzleinput.split("\n\n")

valid_passports = 0
for passport in passports:
    passport = re.split(' |\n', passport)
    if len(passport) < 7:
        continue
    else:
        field_dict = {}
        for field in passport:
            key, value = field.split(':')
            field_dict[key] = value
        for i, req_field in enumerate(required_fields):
            if req_field in field_dict:
                if i == len(required_fields) - 1:
                    valid_passports += 1
            else:
                break
print (valid_passports)