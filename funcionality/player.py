from random import *
class player(object):

	"""docstring for player"""
	playername = None

	def __init__(self,name):
		self.playername = name
		
	def players(self):
		names=['Michael Abrash','Scott Adams','Leonard Adleman','Alfred Aho','Andrei Alexandrescu','Paul Allen','Eric Allman','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson','Marc Andreessen','Jeremy Ashkenas','Bill Atkinson']
		playerName =  self.playername if self.playername else choice(names)
		return {'name':playerName,'status':'ai','cardsHand':[],'deckplayer':[],'statusShuffle':False,}		


		