
from src.Diet import Diet
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/nutrients")
def get_nutrients():
    # Dafault path
    diet = Diet(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    return jsonify(diet._get_data()[0])

@app.route("/data")
def get_data():
    # Dafault path
    diet = Diet(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    return jsonify(diet._get_data()[1])

@app.route("/opt")
def optimization():
    # Dafault path
    diet = Diet(nutrients_path = "data/nutrients.json", data_path = "data/data.json")
    diet._load_constraints()
    diet._fit()
    result, amount = diet._result()
    return jsonify({"Result":result,"amount":amount})

@app.route("/")
def home():
    return "<h2>App de otimização de compras a partir de nutrientes diários necessários.</h2>"
if __name__ == '__main__':
    app.run(debug=True)


    