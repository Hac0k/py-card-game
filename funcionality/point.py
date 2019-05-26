
class Point(object):
	"""docstring for point"""
	def __init__(self,players):
		self.players = players
		
	def points(self):
		return self.cards()

	def cards(self):
		listsOfPlayer =[]
		lists = []
		for x in range(len(self.players)):
			player = self.players[x]['name']
			playercards = self.players[x]['deckplayer']
			listsOfPlayer.append(len(playercards))
			lists.append([player,len(playercards)])

		return print("you won't")

	def Greatesthan(self, listsOfPlayer):
		sortedlist = sorted(listsOfPlayer)
		for x in range(listsOfPlayer):
			if sortedlist[0] == lists[x][0]:
				return print("you won't")
		return print("you lose ")
		