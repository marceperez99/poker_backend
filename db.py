import sqlite3
from evaluator import get_numerical_value,getEvaluation,get_best_hand,evaluate_winner
from mazo import deck
import itertools
def stringifyCard(hand):
    hand.sort()
    return "".join(hand)
def get_rank(val):
    if val <= 14:
        return "HIGHCARD"
    if val <= 57:
        return "PAIR"
    if val <= 69:
        return "TWO_PAIR"
    if val <= 82:
        return "THREE_OF_A_KIND"
    if val <= 91:
        return "STRAIGHT"
    if val <= 99:
        return "FLUSH"
    if val <= 112:
        return "FULL_HOUSE"
    if val <= 125:
        return "FOUR_OF_A_KIND"
    if val <= 134:
        return "STRAIGHT_FLUSH"
    return "ROYAL_FLUSH"

db = sqlite3.connect('hands.db')
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS flop(id text PRIMARY KEY, community text, success_rate numeric);")
INSERT_SQL = "INSERT INTO flop(id, success_rate) VALUES(?, ?);"
one = 260000
i = 0
success = 0
for hand in itertools.combinations(deck,2):
    for community in itertools.combinations(deck,3):     
        if hand[0] in community or hand[1] in community:
            continue
        myHand = hand + community
        for opponent_hand in itertools.combinations(deck,2):
            if opponent_hand[0] in community or opponent_hand[1] in community:
                continue
            if opponent_hand[0] in hand or opponent_hand[1] in hand:
                continue
            opponentHand = opponent_hand + community
            for community_prediction in itertools.combinations(my_deck,2):
                if community_prediction[0] in opponent_hand or community_prediction[1] in opponent_hand:
                    continue
                if community_prediction[0] in community or community_prediction[1] in community:
                    continue
                if community_prediction[0] in hand or community_prediction[1] in hand:
                    continue
                i = i + 1
                best_hand_1 = get_best_hand(list(myHand + community_prediction))
                best_hand_2 = get_best_hand(list(opponentHand+community_prediction))
                
                if (evaluate_winner(best_hand_1,best_hand_2) == 1):
                    success = success + 1
        
        cursor.execute(INSERT_SQL,(stringifyCard(list(hand)),stringifyCard(list(community),success/)))
    if(i % one == 0):
        print(f"{i/one}%")
print(i)
db.commit()
db.close()