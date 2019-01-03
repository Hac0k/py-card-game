from funcionality.point import *
from funcionality.settings import *
from gui.console.table_console import *
import os
import sys
clear = lambda: os.system('cls')

class actionsTable():
	global mgs
	mgs={"selectCard" : "please for {} a card write the number of card",
	"pass" : "your a passed",
	"dontCard" : "do you havent this card"
	}
	def __init__(self, player, table):
		self.player = player
		self.table = table

	def actions(self,action):
		if action == 1:
			return self.take()
		elif action == 2:
			return self.passe()
		elif action == 3:
			return self.contructor()
		elif action == 4:
			return self.doubleContructor()
		elif action == 5:
			return self.moreConstructor()
		else:
			return self.passe()

	def take(self):
		print(mgs['selectCard'].format('take'))
		cardSelectd = int(input())
		for card in range(len(table)):
			if cardSelectd == table[card]['value']: 
				player['cardsHand'].append(table.pop(card))
				print('your a taked a {}'.format(cardSelectd))
				print("ok this shit is working")
				return
		print('check your selectCard')
		
	def passe(self):
		print('im call this funtion')
		cardSelectd = input()
		for card in range(len(players[0]['cardsHand'])):
			if cardSelectd == players[0]['cardsHand'][card]['number']:
				tempCard = players[0]['cardsHand'].pop([card][cardSelectd])
				return clear()
			else:
				print(msg['dontCard'])
		return self.passe()
	def contructor(self):
		pass

	def doubleContructor(self):
		pass
	def moreConstructor(self):
		pass
				

class main(object):
	global msg,settings,players,deck,table
	msg={
	'selectAction':'please write a number of action',
	'actions':'1-take, 2-passe, 3-contructor, 4-doubleContructor,5-moreConstructor',
	}
	print(game())
	settings = Setting().settings()
	clear()
	# [{'name':playerName,'status':'ai','cardsHand':[],'deckplayer':[],'statusShuffle':False,}]		
	players = settings['players']
	# templateDict ={'number':number,'simbol':simbol,'status':'maindeck','value':(cards[1].index(number))+1,'img':None}
	deck = settings['deck']
	# [{'number':number,'simbol':simbol,'status':'maindeck','value':(cards[1].index(number))+1,'img':None}]
	table = settings['table']
	
	def tables(self,n=0):
		self.shuffle()
		if (self.shuffle()):
			return 'close game'
		print(showTable(table,players[0]['cardsHand']))

		while len(players[0]['cardsHand']) > 0:
			for x in range(len(players)):
				print(msg['selectAction'])
				print(msg['actions'])
				action = input()
				if x > 0:
					action == 2
				actionsTable(players[x],table).actions(int(action))
				print(showTable(table,players[0]['cardsHand']))
				print(len(players[0]['cardsHand']))
			clear()	
		clear()













		
		return self.tables(self) 
	
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





		

