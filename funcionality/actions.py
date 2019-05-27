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

	def actions(self,action,card_selectd=None,ia=False):
		if action == 1:
			return self.take(card_selectd,ia)
		elif action == 2:
			return self.passe(card_selectd,ia)
		elif action == 3:
			return self.contructor(card_selectd,ia)
		else:
			return self.passe(card_selectd,ia)

	def take(self,card_selectd,ia):
		
		if len(self.table) <= 0:
			print("the table is empty u cant only pass")
			return self.passe(card_selectd = None,ia = False)
			
		if not card_selectd:
			print(mgs['selectCard'].format('table','take'))
			card_selectd = int(input())
		
		# this for is for check card in the table
		for card in range(len(self.table)):
			if card_selectd == self.table[card]['value']:
				self.player['deckplayer'].append(self.table.pop(card))

				if ia == False:
					if not self.check_if_card_in_hand(card_selectd):
						print("You no have this card ")
						return self.take(card_selectd = None, ia = False)

				# This for is for take a move to card deck player 
				for user_card in range(len(self.player['cardsHand'])):
					if card_selectd == self.player['cardsHand'][user_card]['value']:
						self.player['deckplayer'].append(self.player['cardsHand'].pop(user_card))
						break; # This break for stop the cycle but is no necessary return 
					
				print('your a taked a {}'.format(card_selectd))
				return clear()

		print('check your selectCard taked')
		return self.take(card_selectd = None,ia = False)
		
	def passe(self,card_selectd,ia):
		
		if not card_selectd:
			print(mgs['selectCard'].format('your deck','throw'))
			card_selectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][card]['value']:
				self.table.append(self.player['cardsHand'].pop(card))
				print('your a trow a {}'.format(card_selectd))
				
				return clear()

		print('check your selectCard passed')
		return self.passe(card_selectd = None, ia = False)

	def contructor(self,card_selectd,ia):
		
		if len(self.table) <= 0:
			print("the table is empty u cant only pass")
			return self.passe(card_selectd = None,ia = False)
			
		if not card_selectd:
			print(mgs['selectCard'].format('your deck','contructor'))
			card_selectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][card]['value']:
				temp_player_card = self.player['cardsHand'].pop(card)
				temp_table_card = None

				print(mgs['selectCard'].format('table','contructor'))
				table_card = int(input())

				if (card_selectd + table_card) >= 15:
					print('The constrution is more 14 please try a new contructions ')
					return self.contructor(card_selectd=None) 

				for cardOfTable in range(len(self.table)):
					if table_card == self.table[cardOfTable-1]['value']:
						temp_table_card = self.table.pop(card)
						continue;
				self.table.append([temp_table_card,temp_player_card])
				return 

		print('check your selectCard')
		return self.contructor(card_selectd)

	def check_if_card_in_hand(self,card_selectd):
    		
		for card in range(len(self.player['cardsHand'])):
			if self.player['cardsHand'][card]['value'] == card_selectd:
				return True
		return False
