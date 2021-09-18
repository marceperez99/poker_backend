import time
import itertools
from evaluator import evaluate_winner, get_best_hand, getEvaluation
from calcularCartas import calcularCartas
import random

from mazo import deck

def evaluarPreFlop(game_state):
    initialChips = game_state["initialChips"]
    remainingChips = game_state["remainingChips"]
    percentSpent = 1 - (remainingChips/initialChips)
    hand = game_state["player"]
    actions = game_state["actions"]
    if hand[0][:-1] == "10":
            hand[0] = "T" + hand[0][-1]
    if hand[1][:-1] == "10":
            hand[1] = "T" + hand[1][-1]
                
    val = calcularCartas(hand[0],hand[1])
    print(val)
    if val > 0.80:
        return "RAISE"
    elif val > 0.60 and val > percentSpent:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.50 and val > 0.80*percentSpent:
        if "CHECK" in actions:
            return "CHECK"
        elif "CALL" in actions:
            return "CALL"
    else:
        return "FOLD"
def evaluarFlop(game_state):
    actions = game_state["actions"]
    hand = game_state["player"]
    community = game_state["community"]
    initialChips = game_state["initialChips"]
    remainingChips = game_state["remainingChips"]
    percentSpent = 1 - (remainingChips/initialChips)
    success = 0
    count = 0
    best_hand_1 = -1,-1
    best_hand_2 = -1,-1
    my_deck = [card for card in deck if not(card in hand ) and not(card in community)]  
    random.shuffle(my_deck)
    my_cards = hand+community
    max_count = 20000
    inicio = time.time()
    for opponent_hand in itertools.combinations(my_deck,2):
        oponent = list(opponent_hand)+community
        if count > max_count:
            break
        for community_prediction in itertools.combinations(my_deck,2):
            if community_prediction[0] in opponent_hand or community_prediction[1] in opponent_hand:
                continue
            count = count + 1
            if count > max_count:
                break 
            best_hand_1 = get_best_hand(my_cards+list(community_prediction))
            best_hand_2 = get_best_hand(oponent+ list(community_prediction))
            
            if (evaluate_winner(best_hand_1,best_hand_2) == 1):
                   success = success + 1
    fin = time.time()
    print(fin-inicio)
    val = success/count
    if val > 0.80:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.60 and val > percentSpent:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.50 and val > 0.80*percentSpent:
        if "CHECK" in actions:
            return "CHECK"
        elif "CALL" in actions:
            return "CALL"
    else:
        return "FOLD"
def evaluarTurn(game_state):
    actions = game_state["actions"]
    hand = game_state["player"]
    community = game_state["community"]
    initialChips = game_state["initialChips"]
    remainingChips = game_state["remainingChips"]
    percentSpent = 1 - (remainingChips/initialChips)
    success = 0
    count = 0
    best_hand_1 = -1,-1
    best_hand_2 = -1,-1
    my_deck = [card for card in deck if not(card in hand ) and not(card in community)]
    random.shuffle(my_deck)
    my_cards = hand+community
    inicio = time.time()
    for opponent_hand in itertools.combinations(my_deck,2):
        opponent = list(opponent_hand)+community
     
        for community_prediction in my_deck:
            if community_prediction in opponent_hand:
                continue
            count = count + 1
              
            
            best_hand_1 = get_best_hand(my_cards + [community_prediction,])
            best_hand_2 = get_best_hand(opponent + [community_prediction,])
            
            if (evaluate_winner(best_hand_1,best_hand_2) == 1):
                   success = success + 1
    fin = time.time()
    print(fin-inicio)
    val = success/count
    if val > 0.80:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.60 and val > percentSpent:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.50 and val > 0.80*percentSpent:
        if "CHECK" in actions:
            return "CHECK"
        elif "CALL" in actions:
            return "CALL"
    else:
        return "FOLD"
def evaluarRiver(game_state):
    actions = game_state["actions"]
    hand = game_state["player"]
    community = game_state["community"]
    initialChips = game_state["initialChips"]
    remainingChips = game_state["remainingChips"]
    percentSpent = 1 - (remainingChips/initialChips)
    success = 0
    count = 0
    best_hand_1 = -1,-1
    best_hand_2 = -1,-1
    my_deck = [card for card in deck if not(card in hand ) and not(card in community)]  
    random.shuffle(my_deck)
    my_cards = hand+community
    inicio = time.time()
    for opponent_hand in itertools.combinations(my_deck,2):
        oponent = list(opponent_hand)+community
        count = count + 1
        best_hand_1 = get_best_hand(my_cards)
        best_hand_2 = get_best_hand(oponent)
        if (evaluate_winner(best_hand_1,best_hand_2) == 1):
            success = success + 1
    fin = time.time()
    print(fin-inicio)
    val = success/count
    if val > 0.80:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.60 and val > percentSpent:
        if "RAISE" in actions:
            return "RAISE"
        elif "BET" in actions:
            return "BET"
    elif val > 0.50 and val > 0.80*percentSpent:
        if "CHECK" in actions:
            return "CHECK"
        elif "CALL" in actions:
            return "CALL"
    else:
        return "FOLD"