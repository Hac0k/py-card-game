
class Point(object):
	"""docstring for point"""
	def __init__(self,players):
		self.players = players
		self.points()
		
	def points(self,players):
		pass

	def cards(self,players):
		listsOfPlayer =[]

		for x in players:
			listsOfPlayer.append({'player':players[x]['name'],'totalCard':len(players[x]['cardsHand'])})

		return listsOfPlayer