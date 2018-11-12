from random import *
class card():
	
	def createCards(self):
		heart=chr(3)
		diamons =chr(4)
		club = chr(5)
		spade =chr(6)
		cards = [[heart,diamons,club,spade],['a',2,3,4,5,6,7,8,9,10,'j','q','k']]
		return cards


class deck(object):
	cards = None
	def __init__(self):
		self.cards = card().createCards()

	"""docstring for deck"""
	def createDeck(self):
		cards = self.cards
		deck = []
		for simbol in cards[0]:
			for number in cards[1]:
				templateDict ={'number':number,'simbol':simbol,'status':'maindeck','value':(cards[1].index(number))+1,'img':None}
				deck.append(templateDict)
		return deck

	def shuffle(self):
		deck = self.createDeck()
		return sample(deck,len(deck))