from random import *

class Card():
	
	def createCards(self):
		cards = [['♠', '♦', '♥', '♣'],['a',2,3,4,5,6,7,8,9,10,'j','q','k']]
		return cards

class Deck(object):
	cards = None
	def __init__(self):
		self.cards = Card().createCards()
		
	def createDeck(self):
		cards = self.cards
		deck = []

		for simbol in cards[0]:
			for number in cards[1]:
				template_dict ={'number':number,'simbol':simbol,'status':'maindeck','value':(cards[1].index(number))+1,'img':None,'type':'card'}
				deck.append(template_dict)

		return deck

	def shuffle(self):
		deck = self.createDeck()
		return sample(deck,len(deck))
		