from random import * 

class Card():
	
	def createCards(self):
		deck = []
		heart=chr(3)
		diamons =chr(4)
		club = chr(5)
		spade =chr(6)
		cards = [[heart,diamons,club,spade],['a',2,3,4,5,6,7,8,9,10,'j','q','k']]
		for simbol in cards[0]:
			for number in cards[1]:
				templateDict ={'number':number,'simbol':simbol,'status':'maindeck','value':int((cards[1].index(number)))+1,'img':None}
				deck.append(templateDict)
		return deck


	def __init__(self):
		return #self.createdeck()

