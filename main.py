#importing modules:
from art import logo 
import funcs

start=input("Would you like to play a Game of BlackJack 21: Y/N ").lower()
if start=="y":
    print(logo)
    p_cards=[]
    c_cards=[]
    next_turn=False
    key_p=2
    key_c=2
    should_continue=True
    p_jack=False
    c_jack=False
    #while loop to be introduced to use recursion
    while should_continue:
        if next_turn:
            key_p=1
            key_c=0
        for i in range(key_p):
            random_card=funcs.new_card()
            p_cards.append(random_card)
        for i in range(key_c):
            random_card=funcs.new_card()
            c_cards.append(random_card) 
        p_total=funcs.card_sum(p_cards) 
        c_total=funcs.card_sum(c_cards)
        if 11 in p_cards and 10 in p_cards and len(p_cards)==2:
            should_continue=False
            p_jack=True
            continue
        elif 11 in c_cards and 10 in c_cards and len(c_cards)==2:
            should_continue=False
            c_jack=True
            continue
        if 11 in p_cards and p_total>21:
            p_cards.remove(11)
            p_cards.append(1)
            p_total=funcs.card_sum(p_cards)
        print(f"Your cards: {p_cards} & sum of your cards is {p_total} ")
        print(f"Computer's 1st card: {c_cards[0]}")
        if p_total<21: 
            another_card=input("If you want another card press (Y)\nIf you want to pass press (N):\n").lower()
            if another_card=="y":
                next_turn=True
        else:    
            should_continue=False
        #ending the cycle:

    print(f"Your final hand : {p_cards}\n Your final score {p_total}")
    while c_total<=16:
        random_card=funcs.new_card()
        c_cards.append(random_card)
        c_total=funcs.card_sum(c_cards)
    winner=funcs.card_compare(p_total, c_total)
    print(f"Your cards :{p_cards} and your total :{p_total}")
    print(f"Computers cards:{c_cards} and computers total :{c_total}")
    print(f"Result of game: {winner}")
            
    if p_jack:
        print(f"Player's card are: {p_cards} and player wins by BlackJack")
    if c_jack:
        print(f"Coumputers card are : {c_cards} and computer wins by BlackJack")    

