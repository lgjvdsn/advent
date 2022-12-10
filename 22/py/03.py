total = 0;
with open('../3.txt', 'r') as f:
	for line in f.readlines():
		half = int((len(line) - 1) / 2)
		repChar = ''.join(list(set(line[0:half]) & set(line[half:-1])))
		total += ord(repChar) -96 if repChar.islower() else ord(repChar) -38
	
print(f'Total part 1: {total} \n')

def findValue(group):
	repChar = ''.join(list(set(group[0]) & set(group[1]) & set(group[2])))
	return ord(repChar) -96 if repChar.islower() else ord(repChar) -38

group = [];
counter = 0;
total = 0
with open('../3.txt', 'r') as f:
	for line in f.readlines():
		group.append(line.strip())
		counter += 1;
		if counter == 3:
			total += findValue(group)
			counter = 0;
			group.clear()

print(f'Total part 2: {total}')
