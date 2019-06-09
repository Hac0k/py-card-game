from random import *
from funcionality.actions import *

def ia_actions(player,table):
    	
	if len(table) > 0: 
		card = choice(table)
		card_selectd = card['value']
		
		if card['type'] == 'constrution':
    			helper_take_constution(table,player,card,card_selectd)	
		
		# Check if have a selectable card of the table 
		count=0
		for x in range(len(table)):
			if check_if_card_in_hand(player,table[x]):
				ActionsTable(player,table).actions(1, table[x]['value'], ia = True)	
				return

	card_player = choice(player['cardsHand'])
	value_card_player = card_player['value']

	ActionsTable(player,table).actions(2, value_card_player, ia = True)

def helper_take_constution(table,player,constrution,card_selectd):
	card_of_constrution = constrution['value']
	emptyList = []

	for card in range(len(table)):
		if card_selectd == card_of_constrution:
			for x in range(len(constrution['cards'])):
				player['deckplayer'].append(constrution['cards'].pop(0))
			eliminated_empty_dictonary(table)
			break;

		for user_card in range(len(player['cardsHand'])):
			if card_selectd == card_of_constrution:
				player['deckplayer'].append(player['cardsHand'].pop(user_card))
				break; # This break for stop the cycle but is no necessary return 
						
def eliminated_empty_dictonary(table):
	for empty_dictionary in range(len(table)):
		if dict.keys(table[empty_dictionary]).__contains__("cards"):
			del table[empty_dictionary]
			break

def check_if_card_in_hand(player,card_selectd):
		
	for card in range(len(player['cardsHand'])):	
		if player['cardsHand'][card]['value'] == card_selectd['value']:
			return True
	return False
