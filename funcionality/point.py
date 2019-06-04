clear = lambda: os.system('cls')

class Point():

	def __init__(self,players):

		self.players = players

	def points(self):
		all_points = []

		for x in range(len(self.players)):
			if len(self.players[x]['deckplayer']) >= 28:
				all_points.append([self.players[x]['name'],3])
			else:
				all_points.append([self.players[x]['name'],0])
		
		#counter of the cards for spades
			spadescounter = 0;

			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['simbol'] == '♠':
					spadescounter+=1
			
			if spadescounter >= 7:
				for x in range(len(all_points)):
					if self.players[x]['name'] == all_points[x][0]:
						all_points[x][1]+=1
					break
		
		#counter of the cards for grand casino
			grancasinocount = 0;	

			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == '10':
					grancasinocount+=1
			
			if grancasinocount >= 4:
				for x in range(len(all_points)):
					if self.players[x]['name'] == all_points[x][0]:
						all_points[x][1]+=2
					break
		
		#counter of the cards for small casino
			smallcasino = 0;	

			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == '10':
					smallcasino+=1
			
			if smallcasino >= 4:
				for x in range(len(all_points)):
					if self.players[x]['name'] == all_points[x][0]:
						all_points[x][1]+=2
					break	

		#counter of the ases
			asescounter = 0

			for cards in range(len(self.players[x]['deckplayer'])):
				if self.players[x]['deckplayer'][cards]['number'] == 'a':
					asescounter+=1
			
			if asescounter >= 4:
				for x in range(len(all_points)):
					if self.players[x]['name'] == all_points[x][0]:
						all_points[x][1]+=1
					break
			
			all_points[x][1]+=asescounter

		clear()
		print("players points")
		for x in range(len(all_points)):
			print("{} {}".format(all_points[x][0],all_points[x][1]))
