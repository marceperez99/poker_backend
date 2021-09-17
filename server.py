from flask import Flask, request, jsonify, Response
import itertools
from evaluator import getEvaluation
from calcularCartas import calcularCartas
from evaluadorFase import evaluarPreFlop

app = Flask(__name__)


@app.route("/get_move",methods=['POST'])
def get_move():
    """
        The body of this method must be
        {
            player: cards[],
            community: cards[],
            strategy: string,
            phase: string,
            actions: action[],
            limite: boolean
        }

        Strategy is a string with either LIE or THINK
        Phase is a string with either PRE-FLOP, FLOP, TURN, RIVER
        Action is a string with possible actions to take = [CHECK,BET,CALL,RAISE,FOLD]
        
        A card is a string with:
            "[2-9AJ-K][SHDC]"
               
        limite es true si se ha alcanzado el número de Raise y ya no es posible hacer Raise

        Response: {“action”: <ACTION>}
    """
    game_state = request.json
    print(game_state)
    try:
        action = ""
        if game_state["strategy"] == "LYING":
            return Response('{"action": "RAISE"}',mimetype="application/json")
        else:     
            if game_state["phase"] == "PRE-FLOP":
                initialChips = game_state["initialChips"]
                remainingChips = game_state["remainingChips"]
                percentSpent = 1 - (remainingChips/initialChips)
                action = evaluarPreFlop(game_state["player"],percentSpent,game_state['actions'])
                return jsonify(action=action)
                
            return Response('{"action": "HEHE"}',mimetype="application/json")
    except Exception as err:
        print(err)
        return Response("",status=500, mimetype="application/json")

@app.route("/get_winner", methods=['POST'])
def get_winner():
    """
     The body of this method must be
        {
            player_1: cards[],
            community: cards[],
            player_2: cards[],
        }
    Response: 
        {"winner": 1} //Player 1
        {"winner": 2} //Player 2
        {"winner": 0} // A tie, divide the pot.
    """
    game_state = request.json

    print(game_state)
    try:
        player_1 = game_state["player_1"]
        player_2 = game_state["player_2"]
        community = game_state["community"]
        best_hand_player_1 = -1,-1
        best_hand_player_2 = -1,-1
        #player_1

        for possible_hand in itertools.combinations(player_1 + community, 5):
            val,kicker = getEvaluation(list(possible_hand))
            if val > best_hand_player_1[0]:
                best_hand_player_1 = val,kicker
            elif val == best_hand_player_1[0]:
                if kicker > best_hand_player_1[1]:
                    best_hand_player_1 = val,kicker
        for possible_hand in itertools.combinations(player_2 + community, 5):
            val,kicker = getEvaluation(list(possible_hand))
            if val > best_hand_player_2[0]:
                best_hand_player_2 = val,kicker
            elif val == best_hand_player_2[0]:
                if kicker > best_hand_player_2[1]:
                    best_hand_player_2 = val,kicker
        print(best_hand_player_1)
        print(best_hand_player_2)
        winner = 0
        if(best_hand_player_1[0]>best_hand_player_2[0]):
            winner  = 1
        elif(best_hand_player_1[0] == best_hand_player_2[0]):
            if(best_hand_player_1[1] > best_hand_player_2[1]):
                winner = 1
            elif(best_hand_player_1[1] < best_hand_player_2[1]):
                winner = 2
        else:
            winner = 2
        
        return Response('{"winner": ' + str(winner) + '}',mimetype="application/json")
    except Exception as err:
        print(err)
        return Response(str(err),status=500, mimetype="application/json")

