from flask import Flask, request

app = Flask(__name__)


@app.route("/generate_move", methods=['POST'])
def generate_move():
    print(request.json)
    return request.json
