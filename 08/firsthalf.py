import os
import re
import operator

os.chdir('./08')

with open('puzzleinput.txt', 'r') as readfile:
    puzzleinput = readfile.read()
raw_instructions = puzzleinput.split('\n')

ops = {
    "+": operator.add,
    "-": operator.sub
    }

accumulator = 0

instructions = []
for instruction in raw_instructions:
    components = re.split(r' |(\+|\-)', instruction)
    components.pop(1)
    components.pop(1)
    components.append(False)
    instructions.append(components)

def indexer(instructions, index, offset, operation):
    index = ops[operation](index, offset)
    # Need to add checks in for when we go over list length
    if index == len(instructions) - 1:
        return
    else:
        execute_instruction(instructions, index)


def execute_instruction(instructions, index):
    if instructions[index][3] == True:
        return
    else:
        instructions[index][3] == True
    if instructions[index][0] == 'acc':
        accumulator = ops[instructions[index][1]](accumulator, instructions[index][2])
        index += 1
    elif instructions[index][0] == 'jmp':
        pass
    elif instructions[index][0] == 'nop':
        pass


execute_instruction(instructions, 0)