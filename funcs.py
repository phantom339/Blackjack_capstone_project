#importing required modules:
import random

def new_card():
    ''' This function give out a random card from the deck '''
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    val=random.choice(cards)
    return val


def card_sum(cards):
    total=0
    for i in cards:
        total+=i
    return total    

def card_compare(p_total, c_total):
    if p_total<=21 and c_total<=21:
        if p_total>c_total:
            winner="Player"
            return winner
        elif p_total<c_total:
            winner="Computer"
            return winner
        else:
            winner="Draw"
            return winner
    elif p_total>21 and c_total<=21:
        winner="Computer wins by Bursts"
        return winner
    elif p_total<=21 and c_total>21:
        winner="Player wins by bursts"
        return winner
    elif p_total>21 and c_total>21:
        if p_total>c_total:
            winner="Computer wins as its cards are closer to 21" 
            return winner
        elif p_total<c_total:
            winner="Player wins as its cards are closer to 21"
            return winner
        else:
            winner="draw"
            return winner