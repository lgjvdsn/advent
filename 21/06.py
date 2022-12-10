def get_fishes(days, fishes):
    for _ in range(days):
        tmp_fish = [0] * 9
        for i in range(9):
            if i == 0 and fishes[0]:
                tmp_fish[6] += fishes[0]; 
                tmp_fish[8] += fishes[0]
            elif fishes[i]:
                tmp_fish[i - 1] += fishes[i]
        fishes = tmp_fish
    return sum(fishes)

with open("06.txt") as entry:
    fishes = [0] * 9
    for num in [int(x) for x in entry.readline().strip().split(',')]:
        fishes[num] += 1
    print(f'Part 1: {get_fishes(80, fishes)}\nPart 2: {get_fishes(256, fishes)}')