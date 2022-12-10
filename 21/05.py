matrix = [[0] * 999 for _ in range(999)]
clean_lines, diagonals = [], []

with open("05.txt") as entry:
    for line in entry.readlines():
        clean_lines.append([[int(y) for y in x.split(',')] for x in line.strip().split(' -> ')])

    for line in clean_lines:
        if line[0][0] == line[1][0]:
            line_max, line_min = max(line[0][1], line[1][1]), min(line[0][1], line[1][1])
            for i in range(line_min, line_max + 1):
                matrix[line[0][0]][i] += 1
        elif line[0][1] == line[1][1]:
            line_max, line_min = max(line[0][0], line[1][0]), min(line[0][0], line[1][0])
            for i in range(line_min, line_max + 1):
                matrix[i][line[0][1]] += 1
        else:
            diagonals.append(line)

    print(len([num for row in matrix for num in row if num >= 2]))

    for line_d in diagonals:
        x_step = 1 if line_d[0][0] < line_d[1][0] else -1
        y_step = 1 if line_d[0][1] < line_d[1][1] else -1
        [x, y] = line_d[0]
        matrix[x][y] += 1
        while [x, y] != line_d[1]:
            x += x_step
            y += y_step
            matrix[x][y] += 1

    print(len([num for row in matrix for num in row if num >= 2]))

#print(f'{line}, {line_max}, {line_min}')

""" read_data = None
with open(r'05.txt') as f:
    read_data = f.readlines()

max_row, max_col = 0, 0
segments = []

for line in read_data:
    end_1, end_2 = line.strip().split(' -> ')
    segments.append((tuple(map(int, end_1.split(','))),
                    tuple(map(int, end_2.split(',')))))
    max_row = max(max_row, segments[-1][0][0], segments[-1][1][0])
    max_col = max(max_col, segments[-1][0][1], segments[-1][1][1])

diagram = [[0]*(max_col+1) for _ in range(max_row+1)]

diagonal_segments = []

for segment in segments:
    if segment[0][0] == segment[1][0]:
        min_col, max_col = min(segment[0][1], segment[1][1]), max(
            segment[0][1], segment[1][1])
        for col in range(min_col, max_col+1):
            diagram[segment[0][0]][col] += 1
    elif segment[0][1] == segment[1][1]:
        min_row, max_row = min(segment[0][0], segment[1][0]), max(
            segment[0][0], segment[1][0])
        for row in range(min_row, max_row+1):
            diagram[row][segment[0][1]] += 1
    else:
        diagonal_segments.append(segment)

print(len([val for row in diagram for val in row if val >= 2]))

for segment in diagonal_segments:
    X_incr = 1 if segment[0][0] < segment[1][0] else -1
    Y_incr = 1 if segment[0][1] < segment[1][1] else -1
    (X, Y) = segment[0]
    diagram[X][Y] += 1
    while True:
        X += X_incr
        Y += Y_incr
        diagram[X][Y] += 1
        if (X, Y) == segment[1]:
            break

print(len([val for row in diagram for val in row if val >= 2])) """


# count = [[0]*(999) for _ in range(999)]
# lines, diagonals = [], []
# with open("05.txt") as entry:
#     for line in entry.readlines():
#         lines.append([[int(y) for y in x.split(',')] for x in line.strip().split(' -> ')])
# for line in lines:
#     if line[0][0] == line[1][0]:
#         print(line)
#         # step = -1 if line[0][1] > line[1][1] else 1
#         # for num in range(line[0][1], line[1][1] + step, step):
#         #     pos = int(str(line[0][0]) + str(num))
#         #     #print(pos)
#         #     count[pos] += 1
#         min_col, max_col = min(line[0][1], line[1][1]), max(
#             line[0][1], line[1][1])
#         for col in range(min_col, max_col+1):
#             count[line[0][0]][col] += 1
#     elif line[0][1] == line[1][1]:
#         print(line)
#         # step = -1 if line[0][0] > line[1][0] else 1
#         # for num in range(int(line[0][0]), int(line[1][0]) + step, step):
#         #     pos = int(str(num) + str(line[0][1]))
#         #     #print(pos)
#         #     count[pos] += 1
#         min_row, max_row = min(line[0][0], line[1][0]), max(
#             line[0][0], line[1][0])
#         for row in range(min_row, max_row+1):
#             count[row][line[0][1]] += 1
#     else:
#         diagonals.append(line)
#                 #print(f'00: {clean[0][0]} 10: {clean[1][0]}')
# #print(len([val for row in lines for val in row if val >= 2]))
# twoplus = [val for row in lines for val in row if val >= 2]
# print(f'len(twoplus): {len(twoplus)}')
