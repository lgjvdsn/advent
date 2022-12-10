# part 1
total, forward, depth = 0, 0, 0
with open("03.txt") as d1:
    sums = [0,1,0,1,0,0,0,1,0,1,1,1]
    for line in d1:
        li = line.strip()
        for i, char in enumerate(li):
            #print(int(char))
            sums[i] += int(char)
    fin_sum = [0,0,0,0,0,0,0,0,0,0,0,0]
    print(sums)
    for i, count in enumerate(sums):
        if count < 500:
            fin_sum[i] = '0'
        else:
            fin_sum[i] = '1'

    print(fin_sum)
    opp = ''.join(fin_sum)
    opp = opp.replace('1', '2').replace('0', '1').replace('2', '0')
    binum = int('0b' + ''.join(fin_sum), 2)
    #print(binum)
    opp = int('0b' + opp, 2)
    #print(opp)
    #print(opp * binum)

binum = ''.join(fin_sum)
binopp = binum.replace('1', '2').replace('0', '1').replace('2', '0')
print(binum)
print(binopp)

""" list_nums = []
with open("03.txt") as d1:
    for line in d1:
        li = line.strip()
        if li[0] == binum[0] and li[1] == binum[1] and li[2] == binum[2]:
            if li[3] == binum[3] and li[4] == binum[4] and li[5] == binum[5]:
                if li[6] == binum[6] and li[7] == binum[7] and li[8] == binum[8]:
                    if li[9] == binum[9]:
                        list_nums.append(line)
        
    print(f'binum: {"".join(list_nums).strip()}')

list_opp = []
with open("03.txt") as d1:
    for line in d1:
        li = line.strip()
        if li[0] == binopp[0] and li[1] == binopp[1] and li[2] == binopp[2]:
            if li[3] == binopp[3] and li[4] == binopp[4] and li[5] == binopp[5]:
                if li[6] == binopp[6] and li[7] == binopp[7]:
                    list_opp.append(line)
                    #if li[9] == binopp[9]:
            #if li[1] == opp[1]:
    print(len(list_opp))

    print(f'binopp = {list_opp}') """

# Part 2
with open("03.txt") as f:
        lines = f.readlines()

currentLinesOxygen, currentLinesCO2 = lines, lines
scrubber_rating,oxygen_rating = 0, 0

for i in range(len(lines[0].strip())):
    lines_with_one_co,lines_with_one_ox = [],[]
    for line in currentLinesOxygen:
        if line[i] == '1':
            lines_with_one_ox.append(line)
    for line in currentLinesCO2:
        if line[i] == '1':
            lines_with_one_co.append(line)

    if len(lines_with_one_ox) >= len(currentLinesOxygen)/2:
        currentLinesOxygen = lines_with_one_ox
    else:
        currentLinesOxygen = [entry for entry in currentLinesOxygen if entry not in lines_with_one_ox]

    if len(lines_with_one_co) < len(currentLinesCO2)/2:
        currentLinesCO2 = lines_with_one_co
    else: currentLinesCO2 = \
        [entry for entry in currentLinesCO2 if entry not in lines_with_one_co]

    if len(currentLinesCO2) == 1: scrubber_rating = int(currentLinesCO2[0].strip(),2)
    if len(currentLinesOxygen) == 1: oxygen_rating = int(currentLinesOxygen[0].strip(),2)

    print("Solution part 2: %d" %(oxygen_rating * scrubber_rating))