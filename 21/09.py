class Location():
    def __init__(self):
        self.neighbors = []
        self.self_num = -1

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def add_self(self, num):
        self.self_num = num

    def print_neighbors(self):
        print(self.neighbors)
        
# create a location list with neighbors?


with open("09.txt") as entry:
    lines = [x.strip() for x in entry.readlines()]
    locations = [[Location() for i in range(100)] for j in range(100)]
    # for i in range(99):
    #     for j in range(99):
    #         print(f'i {i} j {j}')
    #         locations[i][j] = Location()
    # row = [Location() for _ in range(100)]
    # locations = [Location() for list(row) _ in range(100)]
    previous = lines.pop(0)

    for i, char in enumerate(previous):
        if i == 0:
            locations[0][0].add_neighbor(previous[1])
            locations[0][0].add_neighbor(lines[0][0])
        elif i == len(previous) - 1:
            #print(char)
            locations[0][i].add_neighbor(previous[i - 1])
            locations[0][i].add_neighbor(lines[0][-1])
        else:
            locations[0][i].add_neighbor(previous[i - 1])
            locations[0][i].add_neighbor(previous[i + 1])
            locations[0][i].add_neighbor(lines[0][i])
    for i, line in enumerate(lines):
        #print(i)
        for j, char in enumerate(line):
            #print(locations[i][j].print_neighbors())
            #print(char)
            print(f'i {i} j {j}')
            # TODO: Fix the last line location assignment
            if j == 0 and i < len(lines) -1:
                if i == 0:
                    print(f'add {previous[j]}, {line[j + 1]}, {lines[i + 1][j]}')
                locations[i][j].add_neighbor(previous[j])
                locations[i][j].add_neighbor(line[j + 1])
                locations[i][j].add_neighbor(lines[i + 1][j])
        previous = line
    print('0 0')
    locations[0][0].print_neighbors()
    print('0 2')
    locations[0][2].print_neighbors()
    print('1 0')
    locations[1][0].print_neighbors()
    print('2 0')
    locations[2][0].print_neighbors()