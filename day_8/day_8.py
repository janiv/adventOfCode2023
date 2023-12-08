from typing import List


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
    start = []
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
            start.append(dict_key)

    curr = start
    steps = 0
    instr = instructions

    while (not check_all_z(curr)):
        if (steps % 100 == 0):
            print(steps, curr)
        dir = instr[0]
        instr = instr[1:]
        if (len(instr) == 0):
            instr = instructions
        temp = []
        if dir == 'L':
            for c in curr:
                c = nodes_map[c][0]
                temp.append(c)
        else:
            for c in curr:
                c = nodes_map[c][1]
                temp.append(c)
        steps += 1
        curr = temp
    return steps


print(day_8_part2("day_8_input.txt"))
