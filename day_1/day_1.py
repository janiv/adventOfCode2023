import re


TEST_FILE_P1 = "example_data.txt"
TEST_FILE_P2 = "example_data_p2.txt"
FILE_NAME = "day_1_input.txt"
STR_NUMS_ARR = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine']
STR_NUMS_ARR_REV = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves',
                    'thgie', 'enin']


def day_1_part1(filename: str) -> int:
    result = 0
    try:
        file = open(filename, "r")
    except IOError:
        print("No such file found!")
    lines = file.readlines()
    for item in lines:
        left, right = "", ""
        for ch in item:
            if ch.isdigit():
                left = ch
                break
        for ch in reversed(item):
            if ch.isdigit():
                right = ch
                break
        coordinates = left + right
        result += int(coordinates)
    return result


def day_1_part2(filename: str) -> int:
    result = 0

    try:
        file = open(filename, "r")
    except IOError:
        print("No such file found!")
    patt = r"(zero|one|two|three|four|five|six|seven|eight|nine|[0-9])"
    r_patt = r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez|[0-9])"
    lines = file.readlines()

    for item in lines:
        left, right = "", ""
        left = re.findall(pattern=patt, string=item)[0]
        right = re.findall(pattern=r_patt, string=item[::-1])[0]
        if not left.isdigit():
            left = STR_NUMS_ARR.index(left)
        if not right.isdigit():
            right = STR_NUMS_ARR_REV.index(right)
        coordinates = str(left) + str(right)
        print(item + " || "+ coordinates)
        result += int(coordinates)
    return result


print(day_1_part2(FILE_NAME))
