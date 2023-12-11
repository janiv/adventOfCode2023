from typing import List
import numpy as np


def day_8_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.read()
    file.close()
    data = data.split('\n\n')
    instructions = data[0]
    nodes_map = {}
    nodes = data[1].strip()

    nodes = nodes.split('\n')
    for line in nodes:
        full_line = line.split(' = ')
        dict_key = full_line[0]
        dict_key = dict_key.strip()
        left_right = full_line[1]
        left_right = left_right.replace('(', '')
        left_right = left_right.replace(')', '')
        left_right = left_right.split(', ')
        nodes_map[dict_key] = left_right

    curr = 'AAA'
    instr = instructions
    steps = 0
    while (curr != 'ZZZ'):
        dir = instr[0]
        instr = instr[1:]
        if (len(instr) == 0):
            instr = instructions
        if dir == 'L':
            curr = nodes_map[curr][0]
        else:
            curr = nodes_map[curr][1]
        steps += 1
    print(curr)
    return steps


def check_all_z(nodes: List[str]) -> bool:
    for word in nodes:
        if word[2] != 'Z':
            return False
    return True



def day_8_part2(filename: str) -> int:
    file = open(filename, 'r')
    data = file.read()
    file.close()
    data = data.split('\n\n')
    instructions = data[0]
    nodes_map = {}
    nodes = data[1].strip()

    nodes = nodes.split('\n')
    starts = []
    for line in nodes:
        full_line = line.split(' = ')
        dict_key = full_line[0]
        dict_key = dict_key.strip()
        left_right = full_line[1]
        left_right = left_right.replace('(', '')
        left_right = left_right.replace(')', '')
        left_right = left_right.split(', ')
        nodes_map[dict_key] = left_right
        if (dict_key[2] == 'A'):
            starts.append(dict_key)

    steps = []
    for start in starts:
        step = 0
        curr = start
        instr = instructions
        while (curr[2] != 'Z'):
            dir = instr[0]
            instr = instr[1:]
            if (len(instr) == 0):
                instr = instructions
            if dir == 'L':
                curr = nodes_map[curr][0]
            else:
                curr = nodes_map[curr][1] 
            step += 1
        steps.append(step)
    print(steps)
    left = np.lcm.reduce(steps[0:3])
    right = np.lcm.reduce(steps[3::])
    print(left, right)
    return np.lcm(np.int64(left), np.int64(right))

print(day_8_part2("day_8_input.txt"))
