import os
import sys
clear = lambda: os.system('cls')

def cards(decks):

	templ,const,lists="""
	----------
	| {}  {}  |
	|        |
	|        |
	----------
""","""
	-----------------
	| {}  {}  |{} {}|
	|        |	    |
	|       {}|	    |
	---------|-------
""",[]

	for x in decks:
		if isinstance(x, dict) and x['type'] == 'constrution':
			lists.append(const.format(x['cards'][0]['value'],x['cards'][0]['simbol'],x['cards'][1]['value'],x['cards'][1]['simbol'],x['value']))
		else:
			lists.append(templ.format(x['value'],x['simbol']))
	lines = [lists[i].splitlines() for i in range(len(lists))]

	return lines
	
def game():
	game_definition ="""
Casino, often incorrectly spelled Cassino, probably dates to at least the seventeenth century. One of the first references in English is found in "The Hoyle Games", edited by Charles Jones, London, 1808. But several very similar games are described in the first manuals in French and German, such as Papillon and Callabra.

2.Number of players
In a game of Casino two, three or four players can intervene. It is better to play two or four in two pairs.

3. Type of Deck
A deck of 52 cards is used to play the Casino.

4. Value and Order of the Cards
The ace is worth 1 point; the other cards, from two to ten, have the value in points indicated by their indexes; the figures (King, Lady, Jack) have no numerical value.

5. Start
To start a game, the giver gives two cards to his opponent, then leaves two uncovered cards on the table and finally gives two for him, and deals another round of cards as in the first. This means that each player will have four cards in his hand and four will be discovered on the table. The giver leaves the deck to the right and the game begins. After playing these hands, the giver gives four cards to each player, two at a time, but does not put any on the table. Continued in this way, the same giver gives hands of four cards to each, six consecutive times, until the deck is finished, but puts cards on the table only in the beginning. When there are more than two players, each receives four cards in each round, but none is placed on the table before the first round. When giving the last cards of the deck, the giver must announce "Last round". The turn of giving alternates, or passes clockwise.

6.Development
Beginning with the hand (the player to the left of the giver), each player must play in his turn a card he has until the hand is finished. The played card must be used to: "discard", "take", "build", "duplicate" or "increase a construction".
Discard: if he can not or does not want to do any other game, the player leaves a card uncovered on the table.
Take: All the cards on the table can be captured, as long as the player has an appropriate card in his hand. A figure can be captured by another of the same class, for example, a Lady by a Lady. The cards thus captured are "taken": the player places them in a pile face down in front of him. The lowest cards can be taken in pairs and also by construction.
Build: two cards whose numerical total is ten or less, can be taken with a card equal to your total. For example, a six and a three can be taken with a nine; a five, a four and an ace with a ten. A player can leave a card in his hand on a card or cards on the table, making a "construction" of two or more cards that he will try to take in the next turn. For example, a four can be left on a three on the table, provided that the player has a seven in hand to be able to take them on the other turn. Also having a pair of the same index in the hand, with a third index card on the table, a player can build a pair, trying to take it with his other card later. For example, the player has two ten; he leaves one of them on a ten of the table, trying to take them later with the third ten. To make any construction in such a way that it is left to take it later, the player must declare the necessary index to take it, and this statement is mandatory. For example, a player leaves a five on a five and says: "building fives"; the opponent can not take the construction with a ten. Any construction left on the table can be taken by the opponent (or partner) of the constructor with the specified letter. A player can not be discarded in a turn in which he must build a construction made by him: he must take something or double the construction. The figures can not be used to build, they can only be taken in pairs. An alternative rule would be that they can be taken in pairs or triples.
Duplicate a construction: any construction can be doubled to the extent of available charts. For example, if the cards on the table are five, four, three and six, all can be taken with a nine. Or five, four and nine can be taken with a nine. Having played a six on a four to make ten, a player can in turn take his construction along with a seven and a three that were on the table, or can play a seven on a three and consolidate the two constructions, still keeping the Ten needed in the hand. But it is not required that a player at any time take the cards except to obey the rule of construction.
Increase a construction: a letter can be added to a construction by raising the index of the necessary letter to take it, provided that
the construction is unique, in no way duplicated;
the added letter comes from the hand, not from the table.
If these conditions are met, a player can increase their own or opponent's construction. For example: a six has been built; a player has an ace and a seven in his hand; he can add his ace to the construction, transforming it into seven. But: a six has been built; a player has an ace and a ten in his hand and there is a three on the table; he can not add the ace and three to the construction to increase it to ten.
After the deck is finished and the last hands are played, all the cards remaining on the table belong to the player who was the last to raise.

7.Puntaje
Each player (or pair) counts the points he has won for the cards he has raised. The points to consider are:

Cards (most of the 52 cards): 3 points
Spades (most of the 13 spades): 1 point
Grand Casino (the 10th): 2 points
Small Casino (the 2): 1 point
Aces (each worth 1 point): 4 points

If each player takes 26 cards, there is no score for "Cards".
For each player a cumulative total is saved, and the first to reach 21 points wins the game. The margin of victory is the difference of the totals; there are no prizes per game. If both reach 21 in the same hand, the points are counted in the order of precedence given above, "Cards" first, and the first to reach 21 wins. If the final result depends on the aces account, they are scored in order: A (first), A, A, A. An alternative rule would be that each card deal was a game.
Sweeps (optional): each time a player takes all the cards from the table, one point is scored per sweep. To indicate it, turn a card between your raised cards. For the score of the game, the value of the sweeps goes after that of the "Aces".
Leftovers (optional): for each raised card that exceeds thirty, one player (or pair) scores one point. For the score of the game, the value of the leftovers goes after that of the "Sweeps". The leftover leftovers are pikes taken in excess of eight; If the remaining spades are scored, a point is written for each one and its value goes after the surplus of cards.
Double and quad game (optional): if a player (or pair) reaches 21 points in two dealt cards, his score doubles (before the discount of the opponent's score); If you reach 21 points in a distribution of cards - only possible when scoring sweeps and / or leftovers - your score quadruples.

8. Irregularities
Wrong distribution of cards: in case a new distribution of cards is required, the non-giver can decide who will distribute next (in the game of four, either of the two opponents decides, in the game of three, an erroneous distribution loses the distribution). There must be a new distribution of cards if the mixing or cutting of cards were omitted, provided that the opponent requires it before making any game. There must be a new distribution of cards at any time that the deck is found to be incorrect.
Exposed cards: a card displayed in the cast or turned in the deck goes to the table and the giver plays with a "short hand"; except in the first round of deals, before the four cards have been left on the table, the exposed card remains as given on the table.
Wrong hand: if the giver gives the opponent too many cards, the opponent can turn a card on the table and the giver plays the next round with a short hand. If a hand has too many cards due to not playing in turn, it must be discarded in each subsequent turn during that round. If a hand has a few cards because more than one card was played in a turn, play with a short hand. If there are few cards to complete the cast, but the deck is correct, the giver plays the last round with a short hand.
Letters exposed illegally: only in the game in pairs, a card named or exposed outside the legal game in turn, must be left on the table as if the player had been discarded; he and his partner can not take it anymore. In the game of two and three players, a player must discard the card that has been exposed before time, or with which he tried to take cards that were not enabled.
Illegal gambling: an illegal game must be corrected when the claim is made before an opponent plays.
Inadequate construction: if a player makes a construction and can not take it when he must (because he announced a construction for which he does not have the right card or because he announced a construction that does not fit his ad), his opponent can add a point to his score and subtract one point from the offender's score.
In a two-player game, when each cast constitutes a game, any of the following irregularities causes the game to be lost: incorrect number of cards dealt by the giver in any round except the first; incorrect hand not due to an error of the giver; illegal taking of letters; inadequate construction; turn over previously taken cards; failure of the giver toannounce the last hand. In other games, the last two irregularities (turning the cards and failing to announce the last hand) are not usually penalized).

9. Tips to play the Casino
Good players retain the count of the cards and pikes that each player has taken. In general, they play to win as many cards as possible until the points are outlined.
Play a couple, lean to take with a pike, discard one that is not itchy.
The "cash points" (10, 2 and aces) should be remembered; likewise the highest available cards, tens, nine and eight. Most players do not make a great effort to remember all the other cards, but they try to know the last four cards of the opponent taking note of the unmatched cards due to the construction. For example, a four and a three are taken with a seven; indexes three, four and seven are without a partner. If later a four and a two are taken with a six, the previous four has a partner but now the letters without a pair are two, three, six and seven. When the final hand is dealt, all unmatched cards on the table or in your own hand will be in the opponent's hand.
The giver must take risks in building or discarding his low cards, hoping to take them; the non-giver (or hand) should keep such cards for his last or last games, unless he can build safely or take them, because he will play first in the next round and have the best chance of taking them.
When there are several cards on the table, it is often possible to calculate the opponent's hand for the games he does not play. This should be done systematically: "If he had a ten, he would have done this, if he had a nine he would have done that," and so on.
""" 
	print(welcomemsj())
	print(game_definition)
	print('write anything for exit')
	
	if input():
		return clear() 

def welcomemsj():
	print("""
		This is a game to casino 


		   please enjoy
		(^w^)  (^w^) (^w^) (^w^)


		write anything for exit
		""")

	if input():
		return clear()

def showCompleteTable(table,player):
	cards_players = player['cardsHand']
	name_player = player['name']

	print(showTable(table,'table'),showTable(cards_players,'cards_players',name_player))

def showTable(table, name, name_player=None):
	line =("\n"*2)
	spaces = (" "*10)
	print("{}{}{}{}{}".format(line,spaces,name,spaces,name_player,spaces,line))
	elementsTable = cards(table) 

	for l in zip(*elementsTable):
		print(*l, sep='')


def presentation_players(players):
	line =("\n"*2)
	spaces = (" "*2)

	for x in range(len(players)):
		print("{}{} {}{}".format(spaces,players[x]['name'],len(players[x]['cardsHand']),spaces))
