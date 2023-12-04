from typing import List
import re


NUM_PAT = r'[0-9]+'
PUNCT_PAT=r'[@#$%&*\-+=\/]'
GEAR_PAT = r'[*]'


def day_3_symbols(string: str):
    non_symbols = '0123456789.'
    symbols = set(string) - set(non_symbols)

def areThereSymbols(line: str, left: int, right:int)->bool:
    if re.search(PUNCT_PAT, line[left:right]):
        return True
    return False


def isValidPart(lines: List[str], above: int, below: int, left: int, right: int)-> bool:
    if left != 0:
        left_end = left - 1
    else:
        left_end = 0
    if right != len(lines[0]):
        right_end = right + 1
    else:
        right_end = right 
    if above > -1:
        found = areThereSymbols(lines[above], left_end, right_end)
        if found:
            return True
    if below < len(lines):
        found = areThereSymbols(lines[below], left_end, right_end)
        if found:
            return True
    found = areThereSymbols(lines[above+1], left_end, right_end)
    if found:
        return True
        
    return False

def substitute(start: int, end: int, character: str)->str:
    rep_str = ""
    for i in range(start, end):
        rep_str = rep_str + character
    return rep_str

def day_3_part1(filename: str)-> int:
    total = 0
    file = open(filename, 'r')
    raw_file = file.readlines()
    lines = []
    for r_line in raw_file:
        lines.append(r_line.strip('\n'))
    
    for i, line in  enumerate(lines):
        #First we search for numbers in line
        nums = re.findall(NUM_PAT, line)
        print(nums)
        #For each number match object we do verification
        for num in nums:
            left = re.search(num, line).start()
            right = re.search(num, line).end()
            print("Num: ", num, " Left: ", left, "Right", right, "Length of line: ", len(line))
            if (isValidPart(lines, i-1, i+1, left, right)):
                total += int(num)
            #We need to do this to handle duplicates of same number
            #Is it dumb? yes. Does it work? also yes.
            filler = substitute(left, right, "a")
            line = line.replace(num, filler, 1)
            
    print(total)
    return total

def num_search_helper(line: str, left: int, right: int) -> List[int]:
    numbers = []
    while re.search(NUM_PAT, line):
        num = re.search(NUM_PAT, line)
        num_span = num.span()
        for i in range(num_span[0], num_span[1]):
            if left-1 <= i <= right:
                numbers.append(num.group())
                break
        filler = substitute(num_span[0], num_span[1], 'n')
        line = line.replace(num.group(), filler, 1)
    return numbers
            
def find_nums(lines: List[str], line_number: int, left: int, right: int) -> List[int]:
    #First find all nums near rectangle
    #above
    nums = []
    if line_number > 0:
        above = line_number -1
        nums_above = num_search_helper(lines[above], left, right)
        nums += nums_above
    if line_number < len(lines) -1:
        below = line_number + 1
        nums_below = num_search_helper(lines[below], left, right)
        nums += nums_below
    nums_adjacent = num_search_helper(lines[line_number], left, right)
    nums += nums_adjacent

    return nums
    

def day_3_part2(filename: str) -> int:
    total = 0
    file = open(filename, 'r')
    raw_file = file.readlines()
    lines = []
    for r_line in raw_file:
        lines.append(r_line.strip('\n'))

    for i, line in enumerate(lines):
        gears = re.findall(GEAR_PAT, line)
        for gear in gears:
            parts = []
            left = re.search("\\" + gear, line).start()
            right = re.search("\\" + gear, line).end()
            parts = find_nums(lines, i, left, right)
            if len(parts) == 2:
                ratio = int(parts[0]) * int(parts[1])
                total += ratio
            filler = substitute(left, right, "g")
            line = line.replace(gear, filler, 1)
            
    return total



s = "String"
print(day_3_part2("day_3_input.txt"))