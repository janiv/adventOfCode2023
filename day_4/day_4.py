import re


DIGITS = r"[' '][2\d]+"

def day_4_part1(filename: str) -> int:
    total = 0
    file = open(filename, 'r')
    raw_lines = file.readlines()
    lines = []
    for r_line in raw_lines:
        line = r_line.strip('\n')
        lines.append(line)
    
    for line in lines:
        points = 0
        game_data = line.split(':') #left contains game num, right nums
        numbers = game_data[1].split('|')
        win_nums = re.findall(DIGITS, numbers[0])
        given_nums = re.findall(DIGITS, numbers[1])
        win_nums = [n.strip() for n in win_nums]
        given_nums = [m.strip() for m in given_nums]
        matches = len(set(win_nums) & set(given_nums))
        if matches > 0:
            points = pow(2, matches-1)
        print(game_data[0], " has ", matches, " that yields ", points)
        total += points
    return total

def day_4_part2(filename:str) -> int:
    scratch_cards = 0
    cards_dict = {}
    file = open(filename, 'r')
    raw_lines = file.readlines()
    lines = []
    for r_line in raw_lines:
        line = r_line.strip('\n')
        lines.append(line)
    c_keys = []
    for i in range(1, len(lines)+ 1):
        c_keys.append(i)
    for c in c_keys:
        cards_dict[c] = 1
    print(len(cards_dict))
    print(len(lines))
    for i, line in enumerate(lines, 1):
        game_data = line.split(':')
        numbers = game_data[1].split('|')
        win_nums = re.findall(DIGITS, numbers[0])
        given_nums = re.findall(DIGITS, numbers[1])
        win_nums = [n.strip() for n in win_nums]
        given_nums= [m.strip() for m in given_nums]
        matches = len(set(win_nums) & set(given_nums))
        curr_copies = cards_dict[i]
        for j in range(i+1, i+1+matches):
            if(j > len(cards_dict)):
                break;
            old_val = cards_dict[j]
            cards_dict[j] = old_val + curr_copies

    return(sum(cards_dict.values()))

print(day_4_part2('day_4_input.txt'))