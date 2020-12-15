import os
import re
import operator
import sys

os.chdir('./08')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read()

class run_instructions:
    def __init__(self):
        self.ops = {
            "+": operator.add,
            "-": operator.sub
            }
        self.accumulator = 0
        self.instructions = []
        self.found_new_path = False
        self.new_path_indexes = []
        self.og_instruction = []
        self.og_index = 0
        self.first_recursion = True

    def compile_instructions(self, raw_instructions):
        for instruction in raw_instructions:
            components = re.split(r' |(\+|\-)', instruction)
            components.pop(1)
            components.pop(1)
            components.append(False)
            components.append(False)
            if components[0] == 'acc':
                components[4] = True
            self.instructions.append(components)

    def indexer(self, index, operation, offset, operator):
        if self.first_recursion:
            self.first_recursion = False
            return index
        if operation == 'acc' or operation == 'nop':
            offset = 1
            operator = '+'
        index = self.ops[operator](index, offset)
        if index == len(self.instructions) and offset == 1:
            print(self.accumulator)
            sys.exit()
        return index

    def reset_path_checks(self):
        self.found_new_path = False
        self.first_recursion = True
        self.accumulator = 0
        self.instructions[self.og_index] = self.og_instruction
        for index in self.new_path_indexes:
            self.instructions[index][3] = False
        self.new_path_indexes.clear()

    def change_instruction(self, instruction, index):
        if self.found_new_path == True or self.instructions[index][4] == True:
            return instruction
        else:
            self.found_new_path = True
            self.instructions[index][4] = True
            self.og_instruction = instruction
            self.og_index = index
            if instruction[0] == 'jmp':
                return [
                    'nop',
                    instruction[1],
                    instruction[2],
                    instruction[3],
                    instruction[4]
                ]
            elif instruction[0] == 'nop':
                return  [
                    'jmp',
                    instruction[1],
                    instruction[2],
                    instruction[3],
                    instruction[4]
                ]

    def execute_instructions(self, index):
        if self.instructions[index][3] == True and self.found_new_path == True:
            self.reset_path_checks()
            return False
        else:
            self.instructions[index][3] = True
            if self.found_new_path == True:
                self.new_path_indexes.append(index)
            self.instructions[index] = self.change_instruction(self.instructions[index], index)
            index = self.indexer(index, self.instructions[index][0], int(self.instructions[index][2]), self.instructions[index][1])
            if self.instructions[index][0] == 'acc':
                self.accumulator = self.ops[self.instructions[index][1]](self.accumulator, int(self.instructions[index][2]))
            self.execute_instructions(index)

executor = run_instructions()
executor.compile_instructions(puzzleinput.split('\n'))
while True:
    executor.execute_instructions(0)