
class Point(object):
	"""docstring for point"""
	def __init__(self,players):
		self.players = players
		
	def points(self):
		return self.cards()

	def cards(self):
		lists_of_player =[]
		lists = []
		players = []

		for x in range(len(self.players)):
			player = self.players[x]['name']
			player_cards = self.players[x]['deckplayer']
			players.append(player)
			lists_of_player.append(len(player_cards))
			lists.append([player,len(player_cards)])

		return self.Greatesthan(players,lists_of_player,lists)

	def Greatesthan(self,players, lists_of_player, lists):
		sorted_list = sorted(lists_of_player,reverse = True)

		for x in range(len(lists_of_player)):
			if sorted_list[0] == lists[x][1]:
				return print("you won {}".format(players[x]))
				
		return print("you lose")
		