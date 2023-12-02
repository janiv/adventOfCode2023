import re

#Being lazy, putting things into variables, so I don't need to ask for input
INPUT_FILE_NAME = "day_2_input.txt"
TEST_FILE_NAME = "day_2_test.txt"
RED_PATTERN = r"([\d,]+)[ ]+red"
GREEN_PATTERN = r"([\d,]+)[ ]+green"
BLUE_PATTERN = r"([\d,]+)[ ]+blue"


def day_2_solver_part1(filename: str, red: int, green: int, blue: int) -> int:
    total = 0
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        data = line.split(':')
        pulls = data[1].split(';')
        addable = True
        for pull in pulls:
            r = re.search(RED_PATTERN, pull)
            g = re.search(GREEN_PATTERN, pull)
            b = re.search(BLUE_PATTERN, pull)
            if r:
                r = r.group().split()[0]
                r = int(r)
                if(r>red):
                    addable= False
                    break
        
            if g:
                g = g.group().split()[0]
                g = int(g)
                if(g>green):
                    addable= False
                    break

            if b:
                b = b.group().split()[0]
                b = int(b)
                if(b > blue):
                    addable= False
                    break
        if addable:
            gameInfo = data[0].split()
            gameNum = gameInfo[1]
            total += int(gameNum)


    return total


def day_2_part2(filename: str) -> int:
    total = 0
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        data = line.split(':')
        pulls = data[1].split(';')
        min_r = 0
        min_g = 0
        min_b = 0
        for pull in pulls:
            r = re.search(RED_PATTERN, pull)
            g = re.search(GREEN_PATTERN, pull)
            b = re.search(BLUE_PATTERN, pull)
            if r:
                r = r.group().split()[0]
                r = int(r)
                min_r = max(r, min_r)
        
            if g:
                g = g.group().split()[0]
                g = int(g)
                min_g = max(g, min_g)

            if b:
                b = b.group().split()[0]
                b = int(b)
                min_b = max(b, min_b)
        power = min_r * min_g * min_b
        total += power

    return total


print(day_2_part2(INPUT_FILE_NAME))

