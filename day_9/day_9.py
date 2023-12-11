from typing import List
import numpy as np

def differences(sequence: List[int]) -> int:
    if set(sequence) == {0}:
        return 0
    if len(set(sequence)) == 1:
        return sequence[0]
    

def extrapolate(sequence: List[int]) -> List[int]:
    curr = np.array(sequence)
    if set(curr) == {0}:
        new_addition = 0
        np.append(curr, new_addition)
        return curr
    if len(set(curr)) == 1:
        new_addition = curr[0]
        np.append(curr, new_addition)
        return curr
    else:
        diffy = curr[1:] - curr[:-1]
        diffy_plus = extrapolate(diffy)
        new_elem = curr[-1] + diffy_plus[-1]
        curr = np.append(curr, new_elem)
        return curr

def extrapolate_backwards(sequence: List[int]) -> List[int]:
    curr = np.array(sequence)
    if set(curr) == {0}:
        new_addition = 0
        return np.insert(curr, 0, new_addition)
    if len(set(curr)) == 1:
        new_addition = curr[0]
        return np.insert(curr, 0, new_addition)
    else:
        diffy = curr[1:] - curr[:-1]
        diffy_plus = extrapolate_backwards(diffy)
        new_elem = curr[0] - diffy_plus[0]
        return np.insert(curr, 0, new_elem)


def day_9_part1(filename:str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    a = []
    for item in data:
        item = item.strip()
        temp_arr = np.fromstring(item, dtype=int, sep=' ')
        temp_arr = extrapolate(temp_arr)
        a.append(temp_arr[-1])
    return sum(a)
        
def day_9_part2(filename:str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    a = []
    for item in data:
        item = item.strip()
        temp_arr = np.fromstring(item, dtype=int, sep=' ')
        temp_arr = extrapolate_backwards(temp_arr)
        a.append(temp_arr[0])
    return sum(a)

print(day_9_part2('day_9_input.txt'))