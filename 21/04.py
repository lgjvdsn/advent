print(  
    next([
        (winners.update(
            { card['name']: 
                sum(set().union(*card['rows'])) * number })
        if card['name'] not in winners else 0, winners)[1]
        for number in list(map(int, number_data.split(',')))
        for card in cards 
        if any(
            line.discard(number) or not line
            for axis in ('rows', 'cols')
            for line in card[axis]
        ) if len(winners) != len(cards)
    ]
    for winners in [{}]
    for number_data, *card_data in
        [__import__('sys').stdin.read().strip().split('\n\n')]
    for cards in [[
        dict(
            rows = list(map(set, rows)),
            cols = list(map(set, zip(*rows))),
            name = f'Board #{name}'
        )
        for name, card in enumerate(card_data, start=1)
        for rows in [[
            list(map(int, line.split())) 
            for line in card.splitlines()
        ]]
    ]])
    [1]
)

""" # I need to develop with classes instead of like a script
import copy

def checkBingo(boards):
    for board in boards:
        if board.checkBingo() > 0:
            return board.checkBingo()
        else:
            return False

class Card():
    def __init__(self, numbers):
        self.board = copy.deepcopy(numbers)
        self.last_val = -1
        self.card = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    def createCard(self, numbers):
        for i in range(5):
            for j in range(5):
                self.board = numbers[i][j]

    def printCard(self):
        print(self.card)
    
    def updateBoard(self, val):
        for i, row in enumerate(self.board):
            for j in range(5):
                if val == row[j]:
                    self.card[i][j] = val
                    self.last_val = val
        
    def checkBingo(self):
        for i, row in enumerate(self.card):
            if row == self.board[i]:
                return self.getUnmarked() * int(self.last_val)
        for i in range(5):
            col_b = [row[i] for row in self.board]
            col_c = [row[i] for row in self.card]
            if col_b == col_c:
                return self.getUnmarked() * int(self.last_val)
        return -1
                
    def getUnmarked(self):
        summito = 0
        for i in range(5):
            for j in range(5):
                if self.card[i][j] != self.board[i][j]:
                    summito += int(self.board[i][j])
        return summito


with open("04.txt") as d1:
    numbers = []
    cards = []
    tmp_card = []
    for i, line in enumerate(d1.readlines()):
        if i == 0:
            numbers = line.split(',')
        elif len(line.strip()):
            tmp_line = list(line.strip().replace('  ', ' ').split())
            tmp_card.append(tmp_line)
        else:
            cards.append(tmp_card.copy())
            tmp_card.clear()

cards = [x for x in cards if x != []]
boards = {}
for i, card in enumerate(cards):
    boards[i] = Card(card)

count = 0
for number in numbers:
    print(f'{len(boards)}')
    for i in range(len(boards)):
        try:
            boards[i].updateBoard(number)
            if boards[i].checkBingo() > 0:
                print(boards[i].checkBingo())
                boards.pop(i)
                break
        except:
            pass """