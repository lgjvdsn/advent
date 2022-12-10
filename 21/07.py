# Pretty naive implementation but less lines
with open("07.txt") as entry:
    crabs = [int(x) for x in entry.readline().strip().split(',')]
    part1, part2 = [0] * (max(crabs) + 1), [0] * (max(crabs) + 1)
    for i in range(min(crabs), max(crabs) + 1):
        for crab in crabs:
            n = crab - i if crab > i else i - crab
            part1[i] += n
            part2[i] += int(n * (n + 1) / 2)
    print(f'part 1: {min(part1)}\npart 2: {min(part2)}')

# Not much difference between the two implementations, even though below uses less memory
""" with open("07.txt") as entry:
    crabs = [int(x) for x in entry.readline().strip().split(',')]
    min_1, min_2 = 9999999999999, 9999999999999
    for i in range(min(crabs), max(crabs) + 1):
        cur_1, cur_2 = 0, 0
        for crab in crabs:
            n = crab - i if crab > i else i - crab
            cur_1 += n
            cur_2 += int(n * (n + 1) / 2)
        min_1 = min(cur_1, min_1)
        min_2 = min(cur_2, min_2)
    print(f'part 1: {min_1}\npart 2: {min_2}') """