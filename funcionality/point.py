class Point():

	def __init__(self,players):
		self.all_points = []
		self.players = players

	def points(self):
		for x in range(len(self.players)):
			if len(self.players[x]['deckplayer']) >= 28:
				self.all_points.append([self.players[x]['name'],3])
			else:
				self.all_points.append([self.players[x]['name'],0])
		return self.spadesCounts()


	def spadesCounts(self):
		for x in range(len(self.players)):
			spadescounter = 0;

			#coounter of the cards 
			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['simbol'] == '♠':
					spadescounter+=1
			
			if spadescounter >= 7:
				for x in range(len(self.all_points)):
					if self.players[x]['name'] == self.all_points[x][0]:
						self.all_points[x][1]+=1
					break	
			return self.asesCounts()
		return self.asesCounts()

	def asesCounts(self):
		for x in range(len(self.players)):
			asescounter = 0;	

			#coounter of the cards 
			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == 'a':
					asescounter+=1
			
			if asescounter >= 4:
				for x in range(len(self.all_points)):
					if self.players[x]['name'] == self.all_points[x][0]:
						self.all_points[x][1]+=1
					break	
			return self.grancasinocount()
		return self.grancasinocount()

	def grancasinocount(self):
		for x in range(len(self.players)):
			grancasinocount = 0;	

			#coounter of the cards 
			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == '10':
					grancasinocount+=1
			
			if grancasinocount >= 4:
				for x in range(len(self.all_points)):
					if self.players[x]['name'] == self.all_points[x][0]:
						self.all_points[x][1]+=2
					break	
			return self.smallcasino()
		return self.smallcasino()

	def smallcasino(self):
		for x in range(len(self.players)):
			smallcasino = 0;	

			#coounter of the cards 
			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == '10':
					smallcasino+=1
			
			if smallcasino >= 4:
				for x in range(len(self.all_points)):
					if self.players[x]['name'] == self.all_points[x][0]:
						self.all_points[x][1]+=2
					break	
			return
		print(self.all_points)
		return 


	def cards(self):
		lists_of_player =[]
		lists = []

		for x in range(len(self.players)):
			player = self.players[x]['name']
			player_cards = self.players[x]['deckplayer']
			self.players.append(player)
			lists_of_player.append(len(player_cards))
			lists.append([player,len(player_cards)])

		return Greatesthan(self.players,lists_of_player,lists)

	def Greatesthan(self, lists_of_player, lists):
		sorted_list = sorted(lists_of_player,reverse = True)

		for x in range(len(lists_of_player)):
			if sorted_list[0] == lists[x][1]:
				return self.all_points.append(self.players[x]);

		return;
