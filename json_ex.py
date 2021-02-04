import json

def check_char_count(mystr):
	if(len(mystr) == 2):
		return (f'{mystr} count passes')
	else:
		return (f'{mystr} count FAILS')


with open('states.json', 'r') as f:
	states = json.load(f)

for i in range(50):
	print(check_char_count(states['states'][i]['abbrevation']))
