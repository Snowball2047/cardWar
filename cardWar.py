import random

def createDeck():
    length = ''
    while length != '3' or length != '6' or length != '10':
        length = input('What size do you want the deck to be? (It has to be 3, 6, or 10')
    if length == 3:
        deck = ['1','2','3']
    elif length == 6:
        deck = ['1','2','3','4','5','6']
    else:
        deck = ['1','2','3','4','5','6','7','8','9','10']
    return deck


