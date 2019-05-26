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

	def actions(self,action,cardSelectd=None,ia=False):
		if action == 1:
			return self.take(cardSelectd,ia)
		elif action == 2:
			return self.passe(cardSelectd,ia)
		elif action == 3:
			return self.contructor(cardSelectd,ia)
		else:
			return self.passe(cardSelectd,ia)

	def take(self,cardSelectd,ia):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('table','take'))
			cardSelectd = int(input())
			
		# this for is for check card in the table
		for card in range(len(self.table)):
			if cardSelectd == self.table[card]['value']:
				self.player['deckplayer'].append(self.table.pop(card))

				if ia == False:
					if not self.check_if_card_in_hand(cardSelectd):
						print("You no have this card ")
						return self.take(cardSelectd = None, ia = False)

				# This for is for take a move to card deck player 
				for userCard in range(len(self.player['cardsHand'])):
					if cardSelectd == self.player['cardsHand'][userCard]['value']:
						self.player['deckplayer'].append(self.player['cardsHand'].pop(userCard))
						break; # This break for stop the cycle but is no necessary return 
					
				print('your a taked a {}'.format(cardSelectd))
				return clear()

		print('check your selectCard taked')
		return self.take(cardSelectd = None,ia = False)
		
	def passe(self,cardSelectd,ia):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('your deck','throw'))
			cardSelectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if cardSelectd == self.player['cardsHand'][card]['value']:
				self.table.append(self.player['cardsHand'].pop(card))
				print('your a trow a {}'.format(cardSelectd))
				
				return clear()

		print('check your selectCard passed')
		return self.passe(cardSelectd = None)

	def contructor(self,cardSelectd,ia):
		
		if not cardSelectd:
			print(mgs['selectCard'].format('your deck','contructor'))
			cardSelectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if cardSelectd == self.player['cardsHand'][card]['value']:
				tempPlayerCard = self.player['cardsHand'].pop(card)
				tempTableCard = None

				print(mgs['selectCard'].format('table','contructor'))
				tableCard = int(input())

				if (cardSelectd + tableCard) >= 15:
					print('The constrution is more 14 please try a new contructions ')
					return self.contructor(cardSelectd=None) 

				for cardOfTable in range(len(self.table)):
					if tableCard == self.table[cardOfTable-1]['value']:
						tempTableCard = self.table.pop(card)
						continue;
				self.table.append([tempTableCard,tempPlayerCard])
				return 

		print('check your selectCard')
		return self.contructor(cardSelectd)

	def check_if_card_in_hand(self,cardSelectd):
		for card in range(len(self.player['cardsHand'])):
			if self.player['cardsHand'][card]['value'] == cardSelectd:
				return True
		return False
