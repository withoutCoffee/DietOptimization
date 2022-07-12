
from src.Diet_Model import Diet_Model
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/nutrients")
def get_nutrients():
    # Dafault path
    diet = Diet_Model(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    return jsonify(diet._get_data()[0])

@app.route("/data")
def get_data():
    # Dafault path
    diet = Diet_Model(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    return jsonify(diet._get_data()[1])

@app.route("/opt")
def optimization():
    # Dafault path
    with open("data/forOpt.json") as openfile:
        req_data = json.load(openfile)
        diet = Diet_Model(nutrients= req_data["nutrients"], data = req_data["data"])
        diet._load_constraints()
        diet._fit()
        result, amount = diet._result()
        return jsonify({"Result":result,"amount":amount})
    return jsonify({"status":500})

@app.route("/opt/run",methods=['POST'])
def run():
    # handle json data and optimization.
    req_data = request.get_json()
    
    diet = Diet_Model(nutrients= req_data["nutrients"], data = req_data["data"])
    diet._load_constraints()
    diet._fit()
    result, amount = diet._result()
    return jsonify({"Result":result,"amount":amount})


@app.route("/")
def home():
    return "<h2>App de otimização de compras a partir de nutrientes diários necessários.<br/>Rota post json:/opt/run</h2>"
if __name__ == '__main__':
    app.run(debug=True)


    