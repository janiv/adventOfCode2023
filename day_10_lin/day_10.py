from typing import List
import numpy as np


# We can use pipe_dict by keeping track of prev_position
# For each pipe one value is equal to
# Curr_position - prev_position
# The other is the next step
pipes_dict = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]]
}


def find_start(matrix: List[List[str]]) -> List[int]:
    return np.where(matrix == 'S')


def dfs(matrix: List[List[str]], dist_matrix: List[List[int]],
        curr_pos: List[int], prev_pos: List[int], steps: int, visited: set()):
    row = curr_pos[0]
    col = curr_pos[1]
    cur_pos = (row, col)
    print("Curr pos: ", curr_pos)
    if row < 0 or (row > (len(matrix) - 1)):
        return
    if col < 0 or col > (len(matrix[0]) - 1):
        return
    if cur_pos in visited:
        return
    if matrix[row][col] == ".":
        return
    dist_matrix[row][col] = steps
    visited.add(cur_pos)
    steps += 1
    print(dist_matrix)

    if matrix[row][col] == 'S':
        dfs(matrix, dist_matrix, (row, col+1), curr_pos, steps, visited)
        dfs(matrix, dist_matrix, (row+1, col), curr_pos, steps, visited)
        dfs(matrix, dist_matrix, (row-1, col), curr_pos, steps, visited)
        dfs(matrix, dist_matrix, (row, col-1), curr_pos, steps, visited)
    else:
        dir = np.array(prev_pos) - np.array(curr_pos)
        pipes_dir = pipes_dict[matrix[row][col]]
        pipes_dir = np.array(pipes_dir)
        print(matrix[row][col])
        print("Dir: ", dir)
        print("Pipes dir: ", pipes_dir)
        p = [0, 0]
        for pair in pipes_dir:
            if not np.array_equal(dir, pair):
                p = pair
        if np.array_equal(p, np.array([0, 0])):
            return
        new_pos = np.array(curr_pos) + np.array(p)
        dfs(matrix, dist_matrix, new_pos, curr_pos, steps, visited)


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

    print(arr)
    init_pos = find_start(arr)
    d_mat = np.full(shape=(max_row, max_col), fill_value=-1, dtype=int)
    print(init_pos[0][0], init_pos[1][0])
    s_pos = (init_pos[0][0], init_pos[1][0])
    x = dfs(arr, d_mat, s_pos, s_pos, 0, set())
    print(x)
    print(d_mat.argmax()/2)


day_10_part1('day_10_input.txt')
