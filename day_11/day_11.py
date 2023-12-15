from typing import List
import numpy as np


def find_empty_rows(matrix: List[List[str]]) -> List[int]:
    empty = []
    for i, row in enumerate(matrix):
        if "#" in row:
            continue
        else:
            empty.append(i)
    return empty


def find_empty_cols(matrix: List[List[str]]) -> List[int]:
    empty = []
    max_col = len(matrix[0])
    for i in range(0, max_col):
        temp = matrix[:, i]
        if "#" in temp:
            continue
        else:
            empty.append(i)
    return empty


def day_11_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    clean_data = []
    for line in data:
        line = line.strip()
        clean_data.append(line)

    i_row = len(clean_data)
    i_col = len(clean_data[0])
    # Create numpy  array
    arr = np.empty(shape=(i_row, i_col), dtype=str)
    for row in range(0, i_row):
        for col in range(0, i_col):
            arr[row][col] = clean_data[row][col]

    # Find empty rows and columns
    empty_rows = find_empty_rows(arr)
    empty_cols = find_empty_cols(arr)
    # Insert extra rows
    arr = np.insert(arr, empty_rows, '.', axis=0)

    # Insert extra columns
    i_col = len(arr[0])
    for i, empty_col in enumerate(empty_cols):
        arr = np.insert(arr, empty_col + i, '.', axis=1)

    # find indexes of galaxies
    galaxy_indexes = list(zip(*np.where(arr == "#")))
    print(galaxy_indexes)
    sum = 0
    for i in range(0, len(galaxy_indexes)):
        for j in range(i, len(galaxy_indexes)):
            row_diff = galaxy_indexes[i][0] - galaxy_indexes[j][0]
            col_diff = galaxy_indexes[i][1] - galaxy_indexes[j][1]
            dist = abs(row_diff) + abs(col_diff)
            sum += dist

    return sum


def count(alist: List, first: int) -> int:
    return len(list(x for x in alist if x < first))


def day_11_part2(filename: str, larger) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()

    clean_data = []
    for line in data:
        line = line.strip()
        clean_data.append(line)

    i_row = len(clean_data)
    i_col = len(clean_data[0])
    # Create numpy  array
    arr = np.empty(shape=(i_row, i_col), dtype=str)
    for row in range(0, i_row):
        for col in range(0, i_col):
            arr[row][col] = clean_data[row][col]

    # Find empty rows and columns
    empty_rows = find_empty_rows(arr)
    empty_cols = find_empty_cols(arr)

    # Find galaxies
    galaxy_indexes = list(zip(*np.where(arr == "#")))
    sum = 0
    for i in range(0, len(galaxy_indexes)):
        for j in range(i, len(galaxy_indexes)):
            galaxy_i_row = galaxy_indexes[i][0]
            galaxy_i_col = galaxy_indexes[i][1]
            galaxy_j_row = galaxy_indexes[j][0]
            galaxy_j_col = galaxy_indexes[j][1]
            
            galaxy_i_row = galaxy_i_row + count(empty_rows, galaxy_i_row) * larger
            galaxy_i_col = galaxy_i_col + count(empty_cols, galaxy_i_col) * larger
            galaxy_j_row = galaxy_j_row + count(empty_rows, galaxy_j_row) * larger
            galaxy_j_col = galaxy_j_col + count(empty_cols, galaxy_j_col) * larger

            row_diff = galaxy_i_row - galaxy_j_row
            col_diff = galaxy_i_col - galaxy_j_col
            dist = abs(row_diff) + abs(col_diff)
            sum += dist

    return sum

print(day_11_part2('day_11_test.txt', 10))
