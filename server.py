from flask import Flask, request, jsonify, Response

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
        Phase is a string with either PRE-FOLD, FOLD, TURN, RIVER
        Action is a string with possible actions to take = [CHECK,BET,CALL,RAISE,FOLD]
        
        A card is a string with:
            "[2-9AJ-K][SHDC]"
               
        limite es true si se ha alcanzado el número de Raise y ya no es posible hacer Raise

        Response: {“action”: <ACTION>}

    """
    game_state = request.json
    print(game_state)
    try:
        return Response('{"action": "RAISE"}',mimetype="application/json")
    except:
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
        return Response('{"winner": 1}',mimetype="application/json")
    except:
        return Response("",status=500, mimetype="application/json")

