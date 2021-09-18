import sqlite3
from evaluator import get_numerical_value,getEvaluation
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

cursor.execute("CREATE TABLE IF NOT EXISTS hands(id text PRIMARY KEY, evaluation integer, kicker integer,rank text);")
INSERT_SQL = "INSERT INTO hands(id, evaluation, kicker,rank) VALUES(?, ?, ?,?);"
one = 26000
for i, hand in enumerate(itertools.combinations(deck,5)):
    val,kicker = getEvaluation(list(hand))
    rank = get_rank(val)
    cursor.execute(INSERT_SQL,(stringifyCard(list(hand)),val,kicker,rank))
    if(i % one == 0):
        print(f"{i/one}%")
db.commit()
db.close()