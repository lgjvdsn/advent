def get_lines(path: str) -> list:
	with open(path, 'r') as f:
		return [line.strip() for line in f.readlines()]

def get_pairs(line: list) -> list:
	pairs: list = [int(pair) for pair in line.replace('-', ',').split(',')]
	pair1: list = [x for x in range(pairs[0], pairs[1] + 1)]
	pair2: list = [x for x in range(pairs[2], pairs[3] + 1)]
	return pair1, pair2

def intersects(pairs: list) -> bool:
	intersect_1 = [x for x in pairs[0] if x in pairs[1]]
	intersect_2 = [x for x in pairs[1] if x in pairs[0]]
	return len(intersect_1) > 0 or len(intersect_2) > 0
	
def contained(pairs: list) -> bool:
	one_contained_in_two = set(pairs[0]).issubset(set(pairs[1]))
	two_contained_in_one = set(pairs[1]).issubset(set(pairs[0]))
	return one_contained_in_two or two_contained_in_one

lines: list = get_lines('../4.txt')
pairs: list = [get_pairs(line) for line in lines]

total_1: int = len([1 for pair in pairs if intersects(pair)])
total_2: int = sum(1 for i in pairs if contained(i))

print(f'Part 1: number of lists contained in another list: {total_1}')
print(f'Part 2: number of intersections: {total_2}')

