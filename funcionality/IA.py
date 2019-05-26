from random import *
from funcionality.actions import *

def ia_actions(player,table):
	actions=[1,2]
	action = choice(actions)

	if action == 1:
		card = choice(table)
		cardSelect = card['value']
		ActionsTable(player,table).actions(action,cardSelect,ia=True)	
	else:
		card = choice(player['cardsHand'])
		cardSelect = card['value']
		ActionsTable(player,table).actions(action,cardSelect,ia = True)
