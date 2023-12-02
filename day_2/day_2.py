import re

#Being lazy, putting things into variables, so I don't need to ask for input
INPUT_FILE_NAME = "day_2_input.txt"
TEST_FILE_NAME = "day_2_test.txt"
RED_PATTERN = r"([\d,]+)[ ]+red"
GREEN_PATTERN = r"([\d,]+)[ ]+green"
BLUE_PATTERN = r"([\d,]+)[ ]+blue"


def day_2_solver(filename: str, red: int, green: int, blue: int) -> int:
    total = 0
    try:
        file = open(filename, 'r')
    except IOError:
        print("Dat file no exist")
    lines = file.readlines()

    for line in lines:
        data = line.split(':')
        pulls = data[1].split(';')
        addable = True
        for pull in pulls:
            r = re.search(RED_PATTERN, pull)
            g = re.search(GREEN_PATTERN, pull)
            b = re.search(BLUE_PATTERN, pull)
            print(r)
        

        if addable:
            gameInfo = data[0].split()
            gameNum = gameInfo[1]
            total += int(gameNum)


    return total

day_2_solver(TEST_FILE_NAME, 12, 13, 14)