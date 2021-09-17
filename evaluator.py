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
    #45 to 57
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]):
        return 57 - (14-get_numerical_value(hand[1])),max(get_numerical_value(hand[2]),get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[1]) == get_numerical_value(hand[2]):
        return 57 - (14-get_numerical_value(hand[2])),max(get_numerical_value(hand[0]),get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[2]) == get_numerical_value(hand[3]):
        return 57 - (14-get_numerical_value(hand[3])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 57 - (14-get_numerical_value(hand[4])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]),get_numerical_value(hand[2]))
    return -1,-1

def is_two_pair(hand): 
    #58 to 69
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]) and  get_numerical_value(hand[2]) == get_numerical_value(hand[3]):
        return 69 - (14-get_numerical_value(hand[3])),-1
    if get_numerical_value(hand[0]) == get_numerical_value(hand[1]) and  get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 69 - (14-get_numerical_value(hand[3])),-1
    if get_numerical_value(hand[1]) == get_numerical_value(hand[2]) and  get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 69 - (14-get_numerical_value(hand[4])),-1
    return -1,-1
def is_three_of_a_kind(hand):
    #70 to 82
    if get_numerical_value(hand[0]) == get_numerical_value(hand[2]):
        return 82 - (14-get_numerical_value(hand[0])),max(get_numerical_value(hand[3]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[1]) == get_numerical_value(hand[3]):
        return 82 - (14-get_numerical_value(hand[1])),max(get_numerical_value(hand[0]),get_numerical_value(hand[4]))
    if get_numerical_value(hand[2]) == get_numerical_value(hand[4]):
        return 82 - (14-get_numerical_value(hand[4])),max(get_numerical_value(hand[0]),get_numerical_value(hand[1]))
    return -1,-1
def is_straight(hand):
    #83 to 91
    value = get_numerical_value(hand[0])
    for card in hand:
        if get_numerical_value(card) != value:
            return -1,-1  
        value = value + 1
    return 91 - (14-get_numerical_value(hand[-1])),-1
def is_flush(hand):
    #92 to 99
    suit = get_suit(hand[0])
    for card in hand:
        if get_suit(card) != suit:
            return -1,-1
    return 99 - (14 - get_numerical_value(hand[-1])),-1 
def is_full_house(hand):
    #100 to 112
    if get_numerical_value(hand[0]) == get_numerical_value(hand[2]) and get_numerical_value(hand[3]) == get_numerical_value(hand[4]):
        return 112 - (14 - get_numerical_value(hand[0])),get_numerical_value(hand[3])
    if get_numerical_value(hand[2]) == get_numerical_value(hand[4]) and get_numerical_value(hand[0]) == get_numerical_value(hand[1]):
        return 112 - (14 - get_numerical_value(hand[2])),get_numerical_value(hand[0])
    return -1,-1

def is_four_of_a_kind(hand):
    #113 to 125     
    if get_numerical_value(hand[0]) == get_numerical_value(hand[3]):
        return 125 - (14 - get_numerical_value[1]),get_numerical_value(hand[4])
    if get_numerical_value(hand[1]) == get_numerical_value(hand[4]):
        return 125 - (14 - get_numerical_value[1]),get_numerical_value(hand[0]) 
    return -1,-1

def is_straight_flush(hand):
    #126 to 134
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

    for evaluator in evaluators:
        hand.sort(key=get_numerical_value)
        result,kicker = evaluator(hand)
        #La mano coincide con el evaluador
        if result >= 0:
            return result,kicker
    #Este codigo nunca se ejecuta hehe
    return -1,-1
