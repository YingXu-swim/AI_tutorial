"""
Read the code in extgames.py and the example games given in the archive (bachstravinsky, meeting, prisonersdilemma). 
Complete the stripped-down version of Poker 
(see the training exercise material for details!) 
in the file template-poker.py, after copying it to poker.py. 
Hint: 
Player 0 will have 4 strategies, and Player 1 will have two strategies. 
Two of the strategies of Player 0 will be automatically eliminated by the application of strict dominance (already implemented in extgames.py), 
so in the final result there will be two strategies for each player. 
Use the names RLOW and RHIGH for the two chance moves, 
0BET and 0FOLD for the two actions of Player 0, and 1CALL and 1FOLD for the two actions of Player 1.

"""
from extgames import reduceToNormalFormGame, ChanceMove, Move, Terminal

# A simple Poker game with one card only

# POKER = Terminal([0,0]) # THIS MUST BE REPLACED WITH THE EXTENSIVE FORM GAME BY YOU!

POKER = ChanceMove([
    (
        0.5,"RLOW", Move(0,[("0FOLD",Terminal([-1,1])),("0BET",Move(1,[("1FOLD",Terminal([1,-1])),("1CALL",Terminal([2,-2]))]))])
    ), 
    
    
    (
        0.5,"RHIGH", Move(0,[("0FOLD",Terminal([-1,1])),("0BET",Move(1,[("1FOLD",Terminal([1,-1])),("1CALL",Terminal([-2,2]))]))])
    )
])


POKER_OBS_0 = ["RHIGH","RLOW"]
POKER_OBS_1 = ["0BET","0FOLD"]
POKER_OBS = dict()
POKER_OBS[0] = POKER_OBS_0
POKER_OBS[1] = POKER_OBS_1
reduceToNormalFormGame(POKER,POKER_OBS)
