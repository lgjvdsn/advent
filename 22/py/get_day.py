# Get today's input
import requests
import argparse 

parser = argparse.ArgumentParser(description="Getting a day from Advent of Code", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-d", "--day", help="Please input the day as a number")
parser.add_argument("-s", "--session", help="Please copy your session and pass it here")

args = parser.parse_args()
if not args.day or not args.session:
    print("Please input -d for the day and -s for your session token")
    exit()

url = f'https://adventofcode.com/2022/day/{args.day}/input'
headers = {'cookie': f'session={args.session}'}
response = requests.get(url , headers=headers)

if response.status_code == 200:
	print(f'downloaded day {args.day} in ../{args.day}.txt')
	f = open(f'../{args.day}.txt', "w")
	f.write(response.text)
	f.close()
else:
	print(response)
