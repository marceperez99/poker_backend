import itertools
import sqlite3
memo = {}
def get_suit(card):
    return card[-1]
def get_numerical_value(card):
    # Una carta tiene la forma [NUMERO|LETRA](C|S|H|D)
    value = card[:-1]
    if value == "J":
        return 11
    if value == "Q":
        return 12
    if value ==  "K":
        return 13
    if value == "A":
        return 14
    else:
        return int(value)
def get_highest_card(hand):
    values = [get_numerical_value(card)  for card in hand]
    return max(values)

def is_highcard(hand):
    #2 to 14
    return get_numerical_value(hand[-1]),-1
def is_pair(hand):
    #43 to 55
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]):
        return 55 - (14-get_numerical_value(hand[1])),max(get_numerical_value(hand[2]),get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[1]) == get_numerical_value(hand[2]):
        return 55 - (14-get_numerical_value(hand[2])),max(get_numerical_value(hand[0]),get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[2]) == get_numerical_value(hand[3]):
        return 55 - (14-get_numerical_value(hand[3])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 55 - (14-get_numerical_value(hand[4])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]),get_numerical_value(hand[2]))
    return -1,-1

def is_two_pair(hand): 
    #56 to 67
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]) and  get_numerical_value(hand[2]) == get_numerical_value(hand[3]):
        return 67 - (14-get_numerical_value(hand[3])),get_numerical_value(hand[1])
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]) and  get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 67 - (14-get_numerical_value(hand[3])),get_numerical_value(hand[1])
    if get_numerical_value(hand[1]) == get_numerical_value(hand[2]) and  get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 67 - (14-get_numerical_value(hand[4])),get_numerical_value(hand[2])
    return -1,-1
def is_three_of_a_kind(hand):
    #68 to 80
    if get_numerical_value(hand[0]) == get_numerical_value(hand[2]):
        return 80 - (14-get_numerical_value(hand[0])),max(get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[1]) == get_numerical_value(hand[3]):
        return 80 - (14-get_numerical_value(hand[1])),max(get_numerical_value(hand[0]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[2]) == get_numerical_value(hand[4]):
        return 80 - (14-get_numerical_value(hand[4])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]))
    return -1,-1
def is_straight(hand):
    #81 to 90
   
    if get_numerical_value(hand[-1]) == 14:
        #special case "A"
        value = 2
        low = True
        for card in hand[:-1]:
            if get_numerical_value(card) != value:
                low = False
            value = value + 1           
        if low:     
            return 90 - (14 - 5),-1
    value = get_numerical_value(hand[0])
    for card in hand:
        if get_numerical_value(card) != value:
            return -1,-1  
        value = value + 1
    return 90 - (14-get_numerical_value(hand[-1])),-1
def is_flush(hand):
    #91 to 98
    suit = get_suit(hand[0])
    for card in hand:
        if get_suit(card) != suit:
            return -1,-1
    return 98 - (14 - get_numerical_value(hand[-1])),-1 
def is_full_house(hand):
    #99 to 111
    if get_numerical_value(hand[0]) == get_numerical_value(hand[2]) and get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 111 - (14 - get_numerical_value(hand[0])),get_numerical_value(hand[3])
    if get_numerical_value(hand[2]) == get_numerical_value(hand[4]) and get_numerical_value(hand[0]) == get_numerical_value(hand[1]):
        return 111 - (14 - get_numerical_value(hand[2])),get_numerical_value(hand[0])
    return -1,-1

def is_four_of_a_kind(hand):
    #112 to 124     
    if get_numerical_value(hand[0]) == get_numerical_value(hand[3]):
        return 124 - (14 - get_numerical_value(hand[1])),get_numerical_value(hand[4])
    if get_numerical_value(hand[1]) == get_numerical_value(hand[4]):
        return 124 - (14 - get_numerical_value(hand[1])),get_numerical_value(hand[0]) 
    return -1,-1

def is_straight_flush(hand):
    #125 to 134
    suit = get_suit(hand[0])
    if get_numerical_value(hand[-1]) == 14:
        #special case "A"
        value = 2
        low = True
        for card in hand[:-1]:
            if get_numerical_value(card) != value or suit != get_suit(card):
                low = False
            value = value + 1           
        if low:     
            return 134 - (14 - 5),-1
    
    value = get_numerical_value(hand[0])
    suit = get_suit(hand[0])
    
    for card in hand:
        if value != get_numerical_value(card) or get_suit(card) != suit:
            return -1,-1
        value = value + 1    
    return 134 - (14 - get_numerical_value(hand[-1])),-1
def is_royal_flush(hand):
    value = 10
    suit = get_suit(hand[0])
    for card in hand:
        if value != get_numerical_value(card) or get_suit(card) != suit:
            return -1,-1
        value = value + 1
    return 135,-1

def getEvaluation(hand):
    evaluators = [
        is_royal_flush,
        is_straight_flush,
        is_four_of_a_kind,
        is_full_house,
        is_flush,
        is_straight,
        is_three_of_a_kind,
        is_two_pair,
        is_pair,
        is_highcard
    ]
    hand.sort(key=get_numerical_value)

    for evaluator in evaluators:
        result,kicker = evaluator(hand)
        #La mano coincide con el evaluador
        if result >= 0:
            return result,kicker
    #Este codigo nunca se ejecuta hehe
    return -1,-1

def get_best_hand(cards,memo={}):
    best_hand = -1,-1
    for possible_hand in itertools.combinations(cards, 5):
        if possible_hand in memo:
            val,kicker = memo[possible_hand]
        else:
            val,kicker = getEvaluation(list(possible_hand))
            memo[possible_hand] = (val,kicker)
        if val > best_hand[0]:
            best_hand = val,kicker
        elif val == best_hand[0]:
            if kicker > best_hand[1]:
                best_hand = val,kicker
    return best_hand
def evaluate_winner(player_1,player_2):
    winner = 0
    if(player_1[0]>player_2[0]):
        winner = 1
    elif(player_1[0] == player_2[0]):
        if(player_1[1] > player_2[1]):
            winner = 1
        elif(player_1[1] < player_2[1]):
            winner = 2
    else:
        winner = 2
    return winner
def get_sql_evaluation(hand):
    hand.sort()
    hand =  "".join(hand)
    db = sqlite3.connect('hands.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT evaluation,kicker from hands where id='{hand}'")
    row = cursor.fetchall()
    return row[0]

