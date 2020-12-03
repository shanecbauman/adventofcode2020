import csv
import os

os.chdir('./02')

values = []

with open('puzzleinput.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        values.append(row[0])

class password_validator:
    def __init__(self):
        self.validPasswords = 0

    def parsePassword(self, og_pw_string):
        str_list = og_pw_string.split()
        char_range = str_list[0].split('-')
        letter = str_list[1][0]
        password = str_list[2]

        if (password[int(char_range[0]) - 1] == letter) ^ (password[int(char_range[1]) - 1] == letter):
            self.validPasswords += 1

passwords = password_validator()
for value in values:
    passwords.parsePassword(value)

print(passwords.validPasswords)