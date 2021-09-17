from evaluator import getEvaluation
from calcularCartas import calcularCartas
def evaluarPreFlop(hand,percentSpent,actions):
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
        

