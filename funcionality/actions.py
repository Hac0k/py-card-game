import os
import sys
clear = lambda: os.system('cls')

class ActionsTable():
	global mgs

	mgs={"selectCard" : "please selectCard of {} for {} a card write the number of card",
		"pass" : "your a passed",
		"dontCard" : "do you havent this card",
		'selectAction':'please write a number of action',
		'actions':'1-take, 2-passe, 3-contructor',
	}

	def __init__(self, player, table):
		self.player = player
		self.table = table

	def actions(self,action=None,card_selectd=None,ia=False):
		if not action:
			print(mgs['selectAction'])
			print(mgs['actions'])
			action = int(input())

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
			
		if not card_selectd and ia == False:
			print(mgs['selectCard'].format('table','take'))
			try:
				card_selectd = int(input())
			except ValueError:
				self.take(card_selectd = None,ia = False)
			

		# this for is for check card in the table
		for card in range(len(self.table)):

			if card_selectd == self.table[card]['value']:
				self.player['deckplayer'].append(self.table.pop(card))

				if ia == False and not self.check_if_card_in_hand(card_selectd):
					if self.table[card]['type'] == 'constrution': 
						self.helper_take_constution(self.table[card],card_selectd)
					else:	
						print("You no have this card ")
						self.take(card_selectd = None, ia = False)

				# This for is take a move to card deck player 
				for user_card in range(len(self.player['cardsHand'])):
					if card_selectd == self.player['cardsHand'][user_card]['value']:
						self.player['deckplayer'].append(self.player['cardsHand'].pop(user_card))
						break; # This break for stop the cycle but is no necessary return 
					
				print('your a taked a {}'.format(card_selectd))
				return clear()

		print('check your selectCard taked')
		return self.take(card_selectd = None,ia = False)
	
	def helper_take_constution(self,constrution,card_selectd):
		cards_of_constrution = constrution['value']
		
		for card in range(len(self.table)):
			if card_selectd == cards_of_constrution:
				for x in range(len(constrution)):
					self.player['deckplayer'].append(constrution['cards'].pop([x]))

			for user_card in range(len(self.player['cardsHand'])):
				if card_selectd == cards_of_constrution:
					self.player['deckplayer'].append(self.player['cardsHand'].pop(user_card))
					break; # This break for stop the cycle but is no necessary return 

		return;			
		

	def passe(self,card_selectd,ia):
		
		if not card_selectd:
			print(mgs['selectCard'].format('your deck','throw'))
			try:
				card_selectd = int(input())
			except ValueError:
				print('check your selectCard passed')
				return self.passe(card_selectd = None, ia = False)

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
			return self.passe(card_selectd = None)
			
		if not card_selectd:
			print(mgs['selectCard'].format('your deck','contructor'))
			card_selectd = int(input())

		for card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][card]['value']:
				temp_player_card = self.player['cardsHand'].pop(card)
				temp_table_card = None

				print(mgs['selectCard'].format('table','contructor'))
				try:
					table_card = int(input())
				except ValueError:
					break;

				if (card_selectd + table_card) >= 15:
					print('The constrution is more 14 please try a new contructions ')
					return self.contructor(card_selectd=None) 

				if(self.check_if_card_in_table(table_card)):
    					
					for cardOfTable in range(len(self.table)):
						if table_card == self.table[cardOfTable]['value']:
							temp_table_card = self.table.pop(cardOfTable)
							break;
					self.table.append({'type':'constrution','value':temp_table_card['value']+temp_player_card['value'],'cards':[temp_table_card,temp_player_card]})
					return;
		print('check your selectCard')
		return self.contructor(card_selectd=None)

	def check_if_card_in_hand(self,card_selectd):
    		
		for card in range(len(self.player['cardsHand'])):
			if self.player['cardsHand'][card]['value'] == card_selectd:
				return True
		return False
		
	def check_if_card_in_table(self,card_selectd):
    		
		for card in range(len(self.table)):
			if self.table[card]['value'] == card_selectd:
				return True
		return False

