import numpy as np
from typing import List

def create_arr(data: str, max_seed: int)->np.array:
    data_arr = data.split(':\n')
    data_nums = data_arr[1].split('\n')
    prev = np.linspace(0, max_seed, max_seed+1, dtype='>i4')
    res_arr = prev
    directions = []
    for item in data_nums:
        dir = item.split(' ')
        start = int(dir[1])
        map_val = int(dir[0])
        steps = int(dir[2])
        for i in range(start, start+steps):
            res_arr[i] = map_val + (i - start)
    return res_arr

def follow_directions(data: str, source: int) -> int:
    data_arr = data.split(':\n')
    data_nums = data_arr[1].split('\n')
    dest = source
    for item in data_nums:
        dirs = item.split(' ')
        start = int(dirs[1])
        end = start + int(dirs[2])
        if (start <= source < end):
            s = source - start + int(dirs[0])
            dest = s
            return dest
    return dest

def findLocVal(seedNum: int, soil_map: np.array, fert_map: np.array,
                        water_map: np.array, light_map: np.array, temp_map: np.array,
                        humid_map: np.array, location_map: np.array)-> int:
    seed_val = seedNum
    soil_val = soil_map[seed_val]
    fert_val = fert_map[soil_val]
    water_val =water_map[fert_val]
    light_val = light_map[water_val]
    temp_val = temp_map[light_val]
    humid_val = humid_map[temp_val]
    loc_val = location_map[humid_val]
    return loc_val


def day_5_part1(filename: str):
    file = open(filename, 'r')
    data_string = file.read()

    data = data_string.split('\n\n')
    seeds = data[0]
    seedsToSoil = data[1]
    soilToFert = data[2]
    fertToWater = data[3]
    waterToLight = data[4]
    lightToTemp = data[5]
    tempToHumid = data[6]
    humidToLoc = data[7]

    seeds = seeds.split(':')
    seed_nums = seeds[1].strip().split()
    seed_nums = [int(x) for x in seed_nums]
    loc_nums = []
    for seed in seed_nums:
        soil_num = follow_directions(seedsToSoil, seed)
        fert_num = follow_directions(soilToFert, soil_num)
        water_num = follow_directions(fertToWater, fert_num)
        light_num = follow_directions(waterToLight, water_num)
        temp_num = follow_directions(lightToTemp, light_num)
        hum_num = follow_directions(tempToHumid, temp_num)
        loc_num = follow_directions(humidToLoc, hum_num)
        loc_nums.append(loc_num)
    return min(loc_nums)

def day_5_part2(filename: str)-> int:
    file = open(filename, 'r')
    data_string = file.read()

    data = data_string.split('\n\n')
    seeds = data[0]
    seedsToSoil = data[1]
    soilToFert = data[2]
    fertToWater = data[3]
    waterToLight = data[4]
    lightToTemp = data[5]
    tempToHumid = data[6]
    humidToLoc = data[7]

    seeds = seeds.split(':')
    seed_nums = seeds[1].strip().split()
    seed_nums = [int(x) for x in seed_nums]

    seed_ranges = []

    while len(seed_nums) > 0:
        s_val = seed_nums.pop(0)
        r_val = seed_nums.pop(0)
        seed_ranges.append([s_val, r_val])

    print(seed_ranges)
    loc_min = seed_ranges[0][0]
    for vals in seed_ranges:
        start = vals[0]
        end = vals[0] + vals[1]
        for x in range(start, end):
            soil_num = follow_directions(seedsToSoil, x)
            fert_num = follow_directions(soilToFert, soil_num)
            water_num = follow_directions(fertToWater, fert_num)
            light_num = follow_directions(waterToLight, water_num)
            temp_num = follow_directions(lightToTemp, light_num)
            hum_num = follow_directions(tempToHumid, temp_num)
            loc_num = follow_directions(humidToLoc, hum_num)
            loc_min = min(loc_num, loc_min)
        print(start, vals[1], " Pair is done")
    return loc_min

print(day_5_part2("day_5_input.txt"))