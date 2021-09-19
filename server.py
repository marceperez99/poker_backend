from flask import Flask, request, jsonify, Response
from evaluator import get_best_hand, evaluate_winner
from evaluadorFase import evaluarPreFlop,evaluarFlop, evaluarRiver,evaluarTurn

app = Flask(__name__)

@app.route("/get_move",methods=['POST','OPTIONS'])
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
    if request.method == 'OPTIONS':
        return Response("",status=200, mimetype="application/json")
    game_state = request.json
    try:
        action = ""
        if game_state["strategy"] == "LIE":
            if "RAISE" in game_state["actions"]:
                action = "RAISE"
            else:
                action = "BET"
        else:
            #THINK     
            if game_state["phase"] == "PRE-FLOP":
                action = evaluarPreFlop(game_state)
            elif game_state["phase"] == "FLOP":
                action = evaluarFlop(game_state)
            elif game_state["phase"] == "TURN":
                action = evaluarTurn(game_state)
            elif game_state["phase"] == "RIVER":
                action = evaluarRiver(game_state)
            print(action)
            return jsonify(action=action)
                
            
    except Exception as err:
        print(err)
        raise err
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

    try:
        player_1 = game_state["player_1"]
        player_2 = game_state["player_2"]
        community = game_state["community"]
        best_hand_player_1 = get_best_hand(player_1 + community)
        best_hand_player_2 = get_best_hand(player_2+community)
        
        winner = evaluate_winner(best_hand_player_1,best_hand_player_2)    
        return Response('{"winner": ' + str(winner) + '}',mimetype="application/json")
    except Exception as err:
        print(err)
        return Response(str(err),status=500, mimetype="application/json")

@app.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    return response