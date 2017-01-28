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


def deal():
	deck = createDeck()
	playerNum = int(input('How many players are there?\n'))
	deal = True
	while deal == True:
		players = []
		for i in range(0,playerNum):
			cardNum = random.randint(0,len(deck)-1)
			players.append(deck[cardNum])
		temp = playerNum-1
		for i in range(0,temp):
			if players[i] == players[i-1]:
				deal == True
				print('Breaking')
				break
			else:
				deal = False
	return players
	
def suitValues(players):
	suitValues = []
	for i in range(0,len(players)):
		card = players[i]
		suit = players[1]
		if suit == 'D':
			suit = 1
		elif suit == 'C':
			suit = 2
		elif suit == 'H':
			suit = 3
		else:
			suit = 4
		suitValues.append(suit)
	return suitValues
		
def numberValues(players):
	numberValues = []
	for i in range(0,len(players)):
		number = players[2]
		numberValues.append(number)
	return numberValues
	
def checkValues(suitValues,numberValues):
	for i in range(0,len(suitValues)):
		wins = []
		for x in range(0,len(suitValues)):
			if i != x:
				if numberValues[i] > numberValues[x]:
					wins.append(True)
				elif numberValues[i] == numberValues[x]:
					if suitValues[i] > suitValues[x]:
						wins.append(True)
					else:
						wins.append(False)
				else:
					wins.append(False)
				
	
players = deal()
suitValues = suitValues(players)
numberValues = numberValues(players)
checkValues(suitValues,numberValues)
