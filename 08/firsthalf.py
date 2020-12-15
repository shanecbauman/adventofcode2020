import os
import re
import operator

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

    def compile_instructions(self, raw_instructions):
        for instruction in raw_instructions:
            components = re.split(r' |(\+|\-)', instruction)
            components.pop(1)
            components.pop(1)
            components.append(False)
            self.instructions.append(components)

    def indexer(self, index, offset, operation):
        index = self.ops[operation](index, offset)
        self.execute_instructions(index)

    def execute_instructions(self, index):
        if self.instructions[index][3] == True:
            return
        else:
            self.instructions[index][3] = True
        if self.instructions[index][0] == 'acc':
            self.accumulator = self.ops[self.instructions[index][1]](self.accumulator, int(self.instructions[index][2]))
            self.indexer(index, 1, "+")
        elif self.instructions[index][0] == 'jmp':
            self.indexer(index, int(self.instructions[index][2]), self.instructions[index][1])
        elif self.instructions[index][0] == 'nop':
            self.indexer(index, 1, "+")

executor = run_instructions()
executor.compile_instructions(puzzleinput.split('\n'))
executor.execute_instructions(0)
print(executor.accumulator)