from random import *

class Player(object):

	"""docstring for player"""
	player_name = None

	def __init__(self,name):
		self.player_name = name
		
	def players(self,boolean = False):
		names=['Michael Abrash','Scott Adams','Leonard Adleman','Alfred Aho','Andrei Alexandrescu','Paul Allen','Eric Allman','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson']
		player_name =  self.player_name if self.player_name else choice(names)
		ai = 'player'if boolean else 'ai'
		
		return {'name':player_name,'status':ai,'cardsHand':[],'deckplayer':[],'statusShuffle':False}		
