# part 1
forward, depth1, aim, depth2 = 0, 0, 0, 0
with open("02.txt") as d1:
    for line in d1:
        if 'forward' in line:
            forward += int(line[-2])
            depth2 += aim * int(line[-2])
        if 'down' in line:
            depth1 += int(line[-2])
            aim += int(line[-2])
        if 'up' in line:
            depth1 -= int(line[-2])
            aim -= int(line[-2])
print(f'part 1 = {forward * depth1}')
print(f'part 2 = {forward * depth2}')