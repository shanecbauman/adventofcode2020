import os
import re
import operator
import sys

os.chdir('./08')

# examplepuzzle.txt
# puzzleinput.txt

# Need to find a way to track the executiion path,  backtrack the accumulator to the starting point for the changed operation.  

with open('examplepuzzle.txt', 'r') as readfile:
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
        self.og_instruction = []
        self.og_accumulator = 0
        self.og_index = 0

    def compile_instructions(self, raw_instructions):
        for instruction in raw_instructions:
            components = re.split(r' |(\+|\-)', instruction)
            components.pop(1)
            components.pop(1)
            # 'Been executed' bool
            components.append(False)
            self.instructions.append(components)

    def indexer(self, index, offset, operation):
        if index == len(self.instructions) - 1 and offset == 1:
            print(self.accumulator)
            sys.exit()
        index = self.ops[operation](index, offset)
        if index not in range(0, len(self.instructions)):
            # Might have to add a modulus to get this to a corrext index number.  
            # Not sure if the index number can be higher than the list length in either positive or negative directions
            index -= len(self.instructions)
        return self.execute_instructions(index)

    def reset_path_checks(self):
        self.found_new_path = False
        self.accumulator = self.og_accumulator
        self.instructions[self.og_index] = self.og_instruction
        # Cannot reset ALL 'been executed' bools, as when we back track we are not backtracking to the start of the program.
        # Rather, we are backtracking to where we changed an operation
        for instruction in self.instructions:
            instruction[3] = False

    def change_instruction(self, instruction, index):
        if self.found_new_path == True:
            return None
        else:
            self.found_new_path = True
            self.og_accumulator = self.accumulator
            self.og_instruction = instruction
            self.og_index = index
            if instruction[0] == 'jmp':
                return [
                    'nop',
                    "+",
                    1,
                    instruction[3]
                ]
            else:
                return  [
                    'jmp',
                    instruction[1],
                    instruction[2],
                    instruction[3]
                ]

    def execute_instructions(self, index):
        if self.instructions[index][3] == True:
            self.reset_path_checks()
            return False
        else:
            self.instructions[index][3] = True
        if self.instructions[index][0] == 'acc':
            self.accumulator = self.ops[self.instructions[index][1]](self.accumulator, int(self.instructions[index][2]))
            self.indexer(index, 1, "+")
        new_instruction = self.change_instruction(self.instructions[index], index)
        if new_instruction is not None:
            self.instructions[index] = new_instruction
        if self.indexer(index, int(self.instructions[index][2]), self.instructions[index][1]) == False:
            index = self.og_index
            # Cannot just iterate one, as that may not be the executuion path
            self.indexer(index, 1, "+")
        else:
            print("No")

executor = run_instructions()
executor.compile_instructions(puzzleinput.split('\n'))
executor.execute_instructions(0)
# print(executor.accumulator)