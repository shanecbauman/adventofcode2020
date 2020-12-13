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

eyecolors = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]

with open("puzzleinput.txt", 'r') as readfile:
    puzzleinput = readfile.read()
passports = puzzleinput.split("\n\n")

def validate_entries(key, value):
    if key == 'byr':
        return int(value) in range(1920, 2002 + 1)
    elif key == 'iyr':
        return int(value) in range(2010, 2020 + 1)
    elif key == 'eyr':
        return int(value) in range(2020, 2030 + 1)
    elif key == 'hgt':
        if re.search(r'^\d+(cm|in)$', value):
            measurement, units = re.findall(r'\d+|[A-Za-z]+', value)
            if units == 'cm':
                return int(measurement) in range(150, 193 + 1)
            else:
                return int(measurement) in range(59, 76 + 1)
    elif key == 'hcl':
        return re.search(r'^#[a-z0-9]{6}$', value)
    elif key == 'ecl':
        return value in eyecolors
    else:
    # Key is 'pid'
        return re.search(r'^\d{9}$', value)

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
                if not validate_entries(req_field, field_dict[req_field]):
                    break
                elif i == len(required_fields) - 1:
                        valid_passports += 1
            else:
                break
print (valid_passports)