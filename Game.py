from funcionality.deck import *
from funcionality.player import *

from gui import *

class Setting(object):
	"""docstring for settingg"""
	global setting,players,msg
	msg={'numberIncorrect':"The number is more big than 4 or 0 choice AUTOSELECT 4, do you reselection of players? Y or N",
	'howplayer':"how many player 2,3,4",'autoselect':'-AUTOSELECT 4','troll':"u cant troll me give a number"}
	setting={}
	players=[]

	def createPlayers(self):
		print "Your name "
		user = raw_input()
		players.append(player(user).players())
		return self.createAiPlayers()	

	def createAiPlayers(self,numberPlayers=None):
		try:
			print msg['howplayer']
			numberPlayers=raw_input()
			int(numberPlayers)
			if int(numberPlayers) >=5 or int(numberPlayers) == 0:
				print msg['numberIncorrect']
				entry=raw_input()
				if (entry == "yes" or entry == "y"):
					print msg['howplayer']
					try:
						number=raw_input()
						int(number-1)
						numberPlayers = number if number > 4 or number != 0 else 4
						return self.createAiPlayers(numberPlayers)
					except ValueError:
						print msg['troll'],msg['autoselect']
						return self.createAiPlayers(numberPlayers=4)
				else:
					return self.createAiPlayers(numberPlayers=4)
			for i in range(int(numberPlayers)-1):
				players.append(player(None).players())
			setting['players'] = players
		except ValueError:
			print msg['troll']
			return self.createAiPlayers(numberPlayers=4)

	

 	def settings(self):
 		self.createPlayers()
		return setting

class game():
	players = Setting().settings()
	deck = deck().shuffle()

	

	# print deck
	







		

