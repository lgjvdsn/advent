# part 1
count = 0
with open("01.txt") as d1:
    prev = int(d1.readline())
    lines = [int(x) for x in d1.readlines()]
    for line in lines:
        count = count + 1 if line > prev else count
        prev = line

print(f'part 1 = {count}')

# part 2
count = 0
with open("01.txt") as d1:
    ld1 = [int(i) for i in d1]
    for i, elem in enumerate(ld1):
        if i + 3 < len(ld1):
            curr = ld1[i] + ld1[i + 1] + ld1[i + 2]
            next = ld1[i + 1] + ld1[i + 2] + ld1[i + 3]
            count = count + 1 if next > curr else count

print(f'part 2 = {count}')
