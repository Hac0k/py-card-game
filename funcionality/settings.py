from funcionality.deck import *
from funcionality.player import *

class Setting(object):
	global setting,players,msg

	msg={'number_incorrect':"The number is more big than 4 or 0 choice AUTOSELECT 4, do you reselection of players? Y or N",
		'howplayer':"how many player 2,3,4",
		'autoselect':'-AUTOSELECT 4',
		'troll':"u cant troll ",
		'numberFalse':"me give a number",
		'name_incorrect':"give me a  name "
		}

	setting={}
	players=[]

	def createPlayers(self):
		try:
			print("Your name ")	
			user = input()
			if user.isdigit():
				print (msg['troll'],msg['name_incorrect'])
				self.createPlayers()
			players.append(Player(user).players(True))
			self.createAiPlayers()				
		except ValueError:
			print(msg['troll'],msg['name_incorrect'])
			self.createPlayers()

	def createAiPlayers(self,number_players=None):
		try:
			print(msg['howplayer'])
			number_players = input()
			int(number_players)
			#validation of the range of the player available
			if int(number_players) >=5 or int(number_players) == 0:
    			# Message of the confirmation, of the what need doing the user
				print(msg['number_incorrect'])
				entry = input()
				if (entry == "yes" or entry == "y"):
					print(msg['howplayer'])
					try:
						number=input()
						int(number-1)
						number_players = number if number > 4 or number != 0 else 4
						return self.createAiPlayers(number_players)
						
					except ValueError:
						print(msg['troll'],msg['numberFalse'],msg['autoselect'])
						return self.createAiPlayers(number_players=4)
				else:
					return self.createAiPlayers(number_players=4)
			for i in range(int(number_players)-1):
				players.append(Player(None).players())
			setting['players'] = players

		except ValueError:
			print(msg['troll'])
			return self.createAiPlayers(number_players=4)

	def settings(self):
		self.createPlayers()
		setting['deck'] = Deck().shuffle()
		setting['noPlayers'] = len(players)
		setting['table'] = []
		return setting
