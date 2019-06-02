from funcionality.point import *
from funcionality.settings import *
from funcionality.ia import *
from funcionality.actions import *
from gui.console.table_console import *
import os
import sys
clear = lambda: os.system('cls')

class main(object):
	global msg,settings,players,deck,table
	msg={
	'selectAction':'please write a number of action',
	'actions':'1-take, 2-passe, 3-contructor',
	}
	print(game())
	settings = Setting().settings()
	clear()
	# List of the dictionaries of the players
	players = settings['players']
	# dictionary of the deck 
	deck = settings['deck']
	# list of dictionaries to represent the table 
	table = settings['table']
	
	def tables(self):
		self.shuffle()
		if (self.shuffle()):
			return Point(players).points();

		print(showCompleteTable(table,players[0]))

		while len(players[0]['cardsHand']) > 0:
			action = None
			for x in range(len(players)):
				if players[x]['status'] == 'player':
					print(msg['selectAction'])
					print(msg['actions'])
					action = input()
					ActionsTable(players[x],table).actions(int(action))
				else:
					ia_actions(players[x],table)

				print(showCompleteTable(table,players[0]))
				print(len(players[0]['cardsHand']))

			clear()	
			print(showCompleteTable(table,players[0]))
			print(len(players[0]['cardsHand']))		
		return self.tables() 
	
	def shuffle(self):
		if(len(deck) == 0):
			return True
		
		if (len(deck) == 52):
			for z in range(4):
				card = deck.pop()
				table.append(card)
				card['status']='table'
		
		for i in players:				
			for x in range(2):
				card = deck.pop()
				i['cardsHand'].append(card)
				card['status']=i['name']

print(main().tables())
