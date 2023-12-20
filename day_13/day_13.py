import numpy as np
from typing import List


def rows_equal(row_a: List[List[str]], row_b: List[List[str]]) -> bool:
    rev_a = row_a[::-1]
    return np.array_equal(rev_a, row_b)


def horizontal_line(matrix: List[List[str]]) -> int:
    res = 0
    # We need to "draw a line", short side determines
    # how far away from line indexes go.
    for i in range(1, len(matrix)):
        if (i <= len(matrix)//2):
            a = matrix[0:i, ]
            b = matrix[i: i+i,]
        else:
            a = matrix[i:,]
            dist = len(matrix) - i
            b = matrix[i-dist:i,]
        if rows_equal(a, b):
            res = i
    return res


def vertical_line(matrix: List[List[str]]) -> int:
    res = 0
    rows, cols = matrix.shape
    for i in range(1, cols):
        if (i <= cols//2):
            a = matrix[:, :i]
            b = matrix[:, i: i+1]
        else:
            a = matrix[:, i:]
            dist = cols - i
            b = matrix[:, i-dist: i]
        print("a : \n", a)
        print("b : \n", b)
        if rows_equal(a,b):
            res = i
    return res


def day_13_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.read()
    file.close()
    data = data.split("\n\n")

    # We need to get rid of \n, and create numpy array
    for patt in data:
        patt = patt.rstrip()
        lines = patt.split('\n')
        sh = (len(lines), len(lines[0]))
        a = np.empty(shape=sh, dtype=str)
        for i in range(0, len(lines)):
            for j in range(0, len(lines[0])):
                a[i][j] = lines[i][j]
        print(a)
        print(horizontal_line(a))
        print(vertical_line(a))


day_13_part1('day_13_test.txt')
