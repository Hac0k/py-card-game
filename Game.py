from funcionality.deck import *
from funcionality.player import *

from gui import *

class setting(object):
	"""docstring for settingg"""
	global setting,players
	setting={}
	players=[]

	def createPlayers(self):
		print "Your name "
		user = raw_input()
		players.append(player(user).players())
		print "how many player 2,3,4"
		numberPlayers = raw_input()
		return self.createAiPlayers(numberPlayers)	

	def createAiPlayers(self,numberPlayers):
		
		if int(numberPlayers) >=5:
			print "The number is more big than 4 choice AUTOSELECT 4, do you reselection of players? Y or N"
			entry=raw_input()
			if (entry == "yes" or entry == "y"):
				print "how many player 2,3,4"
				number=raw_input()
				int(number)-1
				numberPlayers = number if number > 4 else 4
				print numberPlayers
				return self.createAiPlayers(numberPlayers)	
		for i in range(int(numberPlayers)-1):
			players.append(player(None).players())
		return players

class game(object):
	"""docstring for table"""
	"""{'name':playerName,'status':'ai','cards':[],"statusShuffle":False,}	"""
	players = setting().createPlayers()
	"""templateDict ={'number':number,'simbol':simbol,'status':'maindeck','value':(cards[1].index(number))+1,'img':None}"""
	deck = deck().shuffle()
	
	table=[]







		

