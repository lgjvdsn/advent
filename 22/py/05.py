def get_lines(path: str) -> list:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_stacks(line: str) -> list:
    pos = [i for i, ltr in enumerate(line) if ltr == '[']
    return pos

def get_stacks(lines: str) -> list:
    stacks: dict = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    for line in lines[0:8]:
        pos = [i for i in find_stacks(line)]
        [stacks[i // 4 + 1].append(line[i + 1]) for i in pos]
    for k, v in stacks.items():
        v.reverse()
    return stacks

def get_commands(lines: str) -> list:
    commands: list = []
    for line in lines[10:]:
        line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
        commands.append([int(x) for x in line])
    return commands

def move_one(commands: list, stacks: list) -> None:
    for c in commands:
        for i in range(0, c[0]):
            if len(stacks[c[1]]) > 0:
                m = stacks[c[1]].pop()
                stacks[c[2]].append(m)

def move_multiple(commands: list, stacks: list) -> None:
    for c in commands:
        if len(stacks[c[1]]) > 0:
            m = [stacks[c[1]].pop() for i in range(0, c[0])]
            m.reverse()
            [stacks[c[2]].append(i) for i in m]

def part1() -> None:
    lines: list = get_lines('../5.txt')
    stacks: list = get_stacks(lines)
    commands:list = get_commands(lines)
    move_one(commands, stacks)
    print(f'Part 1 result: {"".join([v[-1] for k, v in stacks.items() if v])}')
  
def part2() -> None:
    lines: list = get_lines('../5.txt')
    stacks: list = get_stacks(lines)
    commands:list = get_commands(lines)
    move_multiple(commands, stacks)
    print(f'Part 2 result: {"".join([v[-1] for k, v in stacks.items() if v])}')

part1()
part2()
