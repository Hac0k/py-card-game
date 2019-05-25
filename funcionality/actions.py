import os
import sys
clear = lambda: os.system('cls')

class ActionsTable():
	global mgs

	mgs={"selectCard" : "please selectCard of {} for {} a card write the number of card",
	"pass" : "your a passed",
	"dontCard" : "do you havent this card"
	}

	def __init__(self, player, table):
		self.player = player
		self.table = table

	def actions(self,action,cardSelectd=None):
		if action == 1:
			return self.take(cardSelectd)
		elif action == 2:
			return self.passe(cardSelectd)
		elif action == 3:
			return self.contructor(cardSelectd)
		else:
			return self.passe(cardSelectd)

	def take(self,cardSelectd):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('table','take'))
			cardSelectd = int(input())

		for card in range(len(self.table)):
			if cardSelectd == self.table[card]['value']:
				self.player['cardsHand'].append(self.table.pop(card))
				print('your a taked a {}'.format(cardSelectd))
				print("ok this take is working")
				
				return clear()

		print('check your selectCard taked')
		return self.take(self,cardSelectd=None)
		
	def passe(self,cardSelectd):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('your deck','throw'))
			cardSelectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if cardSelectd == self.player['cardsHand'][card]['value']:
				self.table.append(self.player['cardsHand'].pop(card))
				print('your a trow a {}'.format(cardSelectd))
				print("ok this trow shit is working")

				return clear()
				
		print('check your selectCard passed')
		return self.passe(self,cardSelectd=None)

	def contructor(self,cardSelectd):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('your deck','contructor'))
			cardSelectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if cardSelectd == self.player['cardsHand'][card]['value']:
				tempPlayerCard = self.player['cardsHand'].pop(card)

				print(mgs['selectCard'].format('table','contructor'))
				tableCard = int(input())

				if (cardSelectd + tableCard) >= 15:
					print('The constrution is more 14 please try a new contructions ')
					return self.contructor(self) 

				for cardOfTable in range(len(self.table)):
					print('ese el index',cardOfTable,self.table[cardOfTable]['value']==tableCard)
					if tableCard == self.table[cardOfTable]['value']:
						tempTableCard = self.table.pop(card)
						return
				self.table.append([tempTableCard,tempPlayerCard])
				return 

		print('check your selectCard')
		return self.contructor(self,cardSelectd=None)
