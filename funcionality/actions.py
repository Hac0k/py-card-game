import os
import sys
clear = lambda: os.system('cls')

class ActionsTable():
	global mgs

	mgs={"select_card" : "Please select card of {} for {} a card write the number of card",
		"pass" : "Your a passed",
		"dontCard" : "Do you haven't this card",
		"invalid_actions": "Invalid input action canceled, please retry action",
		'select_actions':'Please write a number of action',
		'actions':'1-take, 2-passe, 3-contructor',
	}

	def __init__(self, player, table):
		self.player = player
		self.table = table

	def actions(self,action=None,card_selectd=None,ia=False):
		if not action:
			print(mgs['select_actions'])
			print(mgs['actions'])
			try:
				action = int(input())
			except ValueError:
				print(mgs["invalid_actions"])
				self.actions()

		if action == 1:
			return self.take(card_selectd,ia)
		elif action == 2:
			return self.passe(card_selectd,ia)
		elif action == 3:
			return self.contructor(card_selectd)
		else:
			return self.actions()

	def take(self,card_selectd,ia):
		
		if len(self.table) <= 0:
			print("The table is empty u cant only pass")
			return self.passe(card_selectd = None,ia = False)
			
		if not card_selectd and ia == False:
			print(mgs['select_card'].format('table','take'))
			try:
				card_selectd = int(input())
			except ValueError:
				print(mgs["invalid_actions"])
				self.actions()
			
		# this for is for check card in the table
		for card in range(len(self.table)):
			is_correct_card = card_selectd == self.table[card]['value']
			is_a_constrution = self.table[card]['type'] == 'constrution'

			if is_correct_card and not is_a_constrution:
				self.player['deckplayer'].append(self.table.pop(card))
				self.take_card_the_user_hands(card_selectd)
				
				print('your a taked a {}'.format(card_selectd))
				return clear()
			
			if ia == False and not self.check_if_card_in_hand(card_selectd):
				if is_a_constrution: 
					self.helper_take_constution(self.table[card],card_selectd)
					self.take_card_the_user_hands(card_selectd)
				else:	
					print("You no have this card ")
					self.take(card_selectd = None, ia = False)

				print('your a taked a {}'.format(card_selectd))
				return clear()

		print('Check your select_card taked')
		return self.take(card_selectd = None,ia = False)

	def take_card_the_user_hands(self,card_selectd):
		# This for is take a move to card deck player 
		for user_card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][user_card]['value']:
				self.player['deckplayer'].append(self.player['cardsHand'].pop(user_card))
				break; # This break for stop the cycle but is no necessary return 
	
	def helper_take_constution(self,constrution,card_selectd):
		cards_of_constrution = constrution['value']
		emptyList = []

		for card in range(len(self.table)):
			if card_selectd == cards_of_constrution:
				for x in range(len(constrution)):
					self.player['deckplayer'].append(constrution['cards'].pop(0))
				eliminated_empty_dictonary(self)
				break;

			for user_card in range(len(self.player['cardsHand'])):
				if card_selectd == cards_of_constrution:
					self.player['deckplayer'].append(self.player['cardsHand'].pop(user_card))
					break; # This break for stop the cycle but is no necessary return 

		return;	

	def eliminated_empty_dictonary(self):
		for empty_dictionary in range(len(self.table)):
			if dict.keys(self.table[empty_dictionary]).__contains__("cards"):
				del self.table[empty_dictionary]
				break
    		
	#throw a Card	
	def passe(self,card_selectd,ia):
		
		if not card_selectd:
			print(mgs['select_card'].format('your deck','throw')) 
			try:
				card_selectd = int(input())
			except ValueError:
				print(mgs["invalid_actions"])
				self.actions()

		for card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][card]['value']:
				self.table.append(self.player['cardsHand'].pop(card))
				print('Your a trow a {}'.format(card_selectd))
				
				return clear()

		print('Check your select_card passed')
		return self.passe(card_selectd = None, ia = False)

	#make a constrution
	def contructor(self,card_selectd):
		
		if len(self.table) <= 0:
			print("The table is empty u cant only pass")
			return self.passe(card_selectd = None)
			
		if not card_selectd:
			print(mgs['select_card'].format('your deck','contructor'))
			try:
				card_selectd = int(input())
			except ValueError:
				print(mgs["invalid_actions"])
				self.actions()
			
		for card in range(len(self.player['cardsHand'])):
			if card_selectd == self.player['cardsHand'][card]['value']:
				temp_player_card = self.player['cardsHand'].pop(card)
				temp_table_card = None

				print(mgs['select_card'].format('table','contructor'))
				try:
					table_card = int(input())
				except ValueError:
					print(mgs["invalid_actions"])
					self.actions()
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
		print('Check your select_card')
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
