import re
import numpy


def day_6_part1(filename: str) -> int:
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    times = data[0].split(':')
    times = re.findall(r"[\d]+", times[1])
    distances = data[1].split(':')
    distances = re.findall(r"[\d]+", distances[1])
    counts = []
    for i, time in enumerate(times):
        dist_tresh = int(distances[i])
        time = int(time)
        count = 0
        for t in range(1, time):
            speed = t
            trav_dis = (time - t) * speed
            if trav_dis > dist_tresh:
                count +=1
        counts.append(count)
    return numpy.prod(counts)


print(day_6_part1("day_6_input.txt"))
