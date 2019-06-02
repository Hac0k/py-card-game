class Point(object):
	global points,players
	
	points = [];
	players = []

	def __init__(self,players):
		self.players = players
		
	def points(self):
		for x in range(len(self.players)):
			if len(self.players[x]['deckplayer']) >= 28:
				points.append([self.players[x]['name'],3])
			else:
				points.append([self.players[x]['name'],0])
		return self.spadesCounts()


	def spadesCounts(self):
		for x in range(len(self.players)):
			spadescounter = 0;

			#coounter of the cards 
			for cards in range(self.players[x]['deckplayer']):
				if cards['simbol'] == '♠':
					spadescounter+=1
			
			if spadesCounter >= 7:
				for x in range(len(points)):
					if self.players[x]['name'] == points[x][0]:
						points[x][1]+=1
					break	
			return
		return self.asesCounts()
	
	def asesCounts(self):
		for x in range(len(self.players)):
			asescounter = 0;	

			#coounter of the cards 
			for cards in range(self.players[x]['deckplayer']):
				if cards['number'] == 'a':
					asescounter+=1
			
			if asescounter >= 4:
				for x in range(len(points)):
					if self.players[x]['name'] == points[x][0]:
						points[x][1]+=1
					break	
			return
		return self.grancasinocount()

	def grancasinocount(self):
		for x in range(len(self.players)):
			grancasinocount = 0;	

			#coounter of the cards 
			for cards in range(self.players[x]['deckplayer']):
				if cards['number'] == '10':
					grancasinocount+=1
			
			if grancasinocount >= 4:
				for x in range(len(points)):
					if self.players[x]['name'] == points[x][0]:
						points[x][1]+=2
					break	
			return
		return

	def smallcasino(self):
		for x in range(len(self.players)):
			smallcasino = 0;	

			#coounter of the cards 
			for cards in range(self.players[x]['deckplayer']):
				if cards['number'] == '10':
					smallcasino+=1
			
			if smallcasino >= 4:
				for x in range(len(points)):
					if self.players[x]['name'] == points[x][0]:
						points[x][1]+=2
					break	
			return
		return print(points)


	def cards(self):
		lists_of_player =[]
		lists = []

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
				return points.append(players[x]);

		return;
	