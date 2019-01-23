from random import *
from funcionality.actions import *

def iaActions(player,table):
	actions=[1,2]
	action = choice(actions)
	if action == 1:
		card = choice(table)
		cardSelect = card['value']
		actionsTable(player,table).actions(action,cardSelect)	
	card = choice(player['cardsHand'])
	cardSelect = card['value']
	actionsTable(player,table).actions(action,cardSelect)
