from random import *

class Player(object):

	"""docstring for player"""
	playername = None

	def __init__(self,name):
		self.playername = name
		
	def players(self,boolean = False):
		names=['Michael Abrash','Scott Adams','Leonard Adleman','Alfred Aho','Andrei Alexandrescu','Paul Allen','Eric Allman','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson']
		playerName =  self.playername if self.playername else choice(names)
		ai = 'player'if boolean else 'ai'
		return {'name':playerName,'status':ai,'cardsHand':[],'deckplayer':[],'statusShuffle':False}		
