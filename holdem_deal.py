
'''
Hold Em Poker - Deal
2016-Jan-15
https://www.reddit.com/r/dailyprogrammer/comments/378h44/20150525_challenge_216_easy_texas_hold_em_1_of_3/
Python 2.7
Chris

Description:

For the first challenge we will simulate the dealing part of the game.

'''

import sys
import random

try:
    noPlayers = int(raw_input('How many players (2-8)? '))
except:
    sys.exit('Not an integer')

if 2 < noPlayers > 8:
    sys.exit('Number not in range')


cardSuits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
cardValues = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deckCards = [(value + ' of ' + suit) for suit in cardSuits for value in cardValues]
random.shuffle(deckCards)
board = []

dPlayers = {}
for x in range(noPlayers):
    dPlayers[x] = [deckCards.pop(), deckCards.pop()]
    print "Player %d's hand: %s, %s" % (x, dPlayers[x][0], dPlayers[x][1])

deckCards.pop() # burn card
for _ in range(3): # flop
    board.append(deckCards.pop())
print 'Flop is: %s, %s, %s' % (board[0], board[1], board[2])
deckCards.pop() # burn card
board.append(deckCards.pop()) # turn
print 'Turn is: %s' % (board[3])
deckCards.pop() # burn card
board.append(deckCards.pop()) # river
print 'River is: %s' % (board[4])
