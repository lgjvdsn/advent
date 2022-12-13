def get_lines(path: str):
	with open('../1.txt', 'r') as f:
		return [line.strip() for line in f.readlines()]

counter = 0
sums = []
for line in get_lines('../1.txt'):
	if not line:
		sums.append(counter)
		counter = 0
	else:
		counter += int(line)

top3 = sum(sorted(sums, reverse=True)[0:3]) 
print(f'max: {max(sums)}')
print(f'top: {sums[-1]}, 2nd: {sums[-2]}, 3rd: {sums[-3]}')
print(f'top3 sum: {top3}')

### naive version under

counter = 0;
sums = []
with open('../1.txt', 'r') as f:
	for line in f.readlines():
		if line == '\n':
			sums.append(counter)
			counter = 0
		else:
			counter += int(line.strip()) 

top3 = sum(sorted(sums, reverse=True)[0:3]) 
print(f'max: {max(sums)}')
print(f'top: {sums[-1]}, 2nd: {sums[-2]}, 3rd: {sums[-3]}')
print(f'top3 sum: {top3}')
