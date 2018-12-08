from funcionality.point import *
from funcionality.settings import *
from gui.console.table_console import *

class actionsTable(object):
	def __init__(self, action, players):
		self.action = action
		self.player = players
	
	def actions(self):
	    try:
	        return {
	            'take': self.take(),
	            'passe': self.passe(),
	            'contructor':self.contructor(),
	            'doubleContructor':self.doubleContructor(),
	            'moreConstructor':self.moreConstructor(),
	        }[x]
	    except KeyError:
	        return self.passe()
	
	def take(self):
		pass
	def passe():
		pass
	def contructor():
		pass

	def doubleContructor():
		pass
	def moreConstructor():
		pass
				

class main(object):
	global mgs,settings,players,deck,table
	mgs={'selectCard':'please a selectCard'}
	settings = Setting().settings()
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
		print(showTable(table))

		












		
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
			for x in range(4):
				card = deck.pop()
				i['cardsHand'].append(card)
				card['status']=i['name']

		

print(main().tables())





		

