#PART 1

# Loss = 0
# Draw = 3
# Win = 6 
# Rock = A or X = 1
# Paper = B or Y = 2
# Scissor = C or Z = 3
# X wins against C
# Y wins against A
# Z wins against B 
# X loses against B
# Y loses against C
# Z loses against A

total = 0;
scores = {'AX':4, 'AY':8, 'AZ':3, 'BX':1, 'BY':5, 'BZ':9, 'CX':7, 'CY':2, 'CZ':6 };
with open('../2.txt', 'r') as f:
	for line in f.readlines():
		key = line.replace(' ', '').strip()
		total += scores[key]
print(f'Total part 1: {total}\n')

# PART 2
# X = must lose
# Y = must draw
# Z = must win

actions = {
	'X' : {
		'A':3, 'B':1, 'C':2
	},
	'Y': {
		'A':4, 'B':5, 'C':6
	},
	'Z': {
		'A':8, 'B':9, 'C':7
	}
}
total = 0
with open('../2.txt', 'r') as f:
	for line in f.readlines():
		play, action = line.rstrip().split(' ')
		total += actions[action][play]

print(f'Total part 2: {total}')	
