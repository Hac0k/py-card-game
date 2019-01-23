class point(object):
	"""docstring for point"""
	def __init__(self,players):
		self.players = players
		self.points()
		
	def points(players):
		pass

	def cards(players):
		listsOfPlayer =[]

		for x in players:
			listsOfPlayer.append({'player':players[x]['name'],'totalCard':len(players[x]['cardsHand'])})

		return listsOfPlayer