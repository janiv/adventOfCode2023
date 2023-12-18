from typing import List
import numpy as np
    
#Direction We are going into
LEFT = {'L', '-', 'F'}
RIGHT=  {'7', '-', 'J'}
UP = {'|', 'F', '7'}
DOWN = {'|', 'L', 'J'}
START = {'S'}

def find_start(arr: List[str]) -> List[int]:
    return np.argwhere(arr == "S")

def dfs(matrix: List[List[str]], row: int, col: int, steps: int, visited=set(), acceptable=set(), prev_dir=set()):
    pos = (row,col)
    if pos in visited and matrix[row][col] == 'S':
        print(steps)
        return visited
    if pos in visited:
        return
    if matrix[row][col] not in acceptable:
        return
    if (row < 0 or row>= len(matrix) or col < 0 or col >= len(matrix[row])):
        return
    if matrix[row][col] == '.':
        return
    
    visited.add(pos)
    if matrix[row][col] == 'S':
        dfs(matrix, row + 1, col, steps + 1, visited, RIGHT, START)
        dfs(matrix, row -1, col, steps + 1, visited, LEFT, START)
        dfs(matrix, row, col + 1, steps + 1, visited, DOWN, START)
        dfs(matrix, row, col - 1, steps + 1, visited, UP, START)
    if matrix[row][col] == "|":
        dfs(matrix, row + 1, col, steps + 1, visited, DOWN, UP)
        dfs(matrix, row - 1, col, steps + 1,  visited, UP, DOWN)
    if matrix[row][col] == "-":
        dfs(matrix, row, col + 1, steps+ 1, visited, RIGHT, LEFT)
        dfs(matrix, row, col - 1, steps + 1, visited, LEFT, RIGHT)
    if matrix[row][col] == "F":
        dfs(matrix, row, col + 1, steps+ 1, visited, RIGHT, DOWN)
        dfs(matrix, row + 1, col, steps+ 1, visited, DOWN)
    if matrix[row][col] == "L":
        dfs(matrix, row, col + 1, steps+ 1, visited, RIGHT)
        dfs(matrix, row - 1, col, steps+ 1, visited, UP)
    if matrix[row][col] == "7":
        dfs(matrix, row + 1, col, steps+1, visited, DOWN)
        dfs(matrix, row, col - 1, steps+1, visited, LEFT)
    if matrix[row][col] == "J":
        dfs(matrix, row -1, col, steps+1, visited, UP)
        dfs(matrix, row, col - 1, steps+1, visited, LEFT)
    
    return visited


def day_10_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    clean_data = []
    for line in data:
        line = line.strip()
        clean_data.append(line)
    max_row = len(clean_data)
    max_col = len(clean_data[0])
    arr = np.empty(shape=(max_row, max_col), dtype=str)
    for row in range(0, max_row):
        for col in range(0, max_col):
            arr[row][col] = clean_data[row][col]

    start = find_start(arr)
    s_row = start[0][0]
    s_col = start[0][1]
    e_set = set()
    visited = dfs(arr, s_row, s_col, 0, e_set, UP)
    print(visited)
    arr_2 = np.zeros(shape=(max_row, max_col), dtype=int)
    for pair in visited:
        row = pair[0]
        col = pair[1]
        arr_2[row][col] = 1

    print(arr)
    print(arr_2)

        

    


day_10_part1('day_10_test2.txt')