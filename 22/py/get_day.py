# Get today's input
import requests
import sys

day = sys.argv[1]
session = sys.argv[2]
print(f'session: {session}')
url = f'https://adventofcode.com/2022/day/{day}/input'
headers = {'cookie': f'session={session}'}
response = requests.get(url , headers=headers)

if response.status_code == 200:
	print(f'downloaded day {day} in ../{day}.txt')
	f = open(f'../{day}.txt', "w")
	f.write(response.text)
	f.close()
else:
	print(response)
