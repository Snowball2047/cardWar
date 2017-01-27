import random

def createDeck():
	suits = ['S','H','C','D']
	deck = []
	length = ''
	standard = input('Do you want to use a standard deck?\n')
	if standard.upper() == 'YES':
		numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	else:
		while length != '12' and length != '24' and length != '40':
			length = input('What size do you want the deck to be? (It has to be 12, 24, or 40)\n')
		if length == 3:
			numbers = ['A','2','3']
		elif length == 6:
			numbers = ['A','2','3','4','5','6']
		else:
			numbers = ['A','2','3','4','5','6','7','8','9','10']
	for i in range(0,4):
		tempSuit = suits[i]
		for i in range(0,len(numbers)):
			card = tempSuit +numbers[i]
			deck.append(card)
	return deck

class player():
	deck = createDeck()
	def __init__(player):
		deck = player.deck
		cardNum = random.randint(0,len(deck))
		player.card = deck[cardNum]

def deal():
	playerNum = int(input('How many players are there?\n'))
	players = []
	for i in range(0,playerNum):
		players.append(player())
	return players

players = deal()