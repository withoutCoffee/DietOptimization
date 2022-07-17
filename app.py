
from src.repository.Diet_Model import Diet_Model
from src.repository.HandleSheet import HandleSheet
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from src.configurations import DevelopmentConfig, ProductionConfig


app = Flask(__name__)
app.config.from_object(ProductionConfig)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def run(nutrients,foods):
    diet = Diet_Model(nutrients= nutrients, data = foods)
    diet._load_constraints()
    diet._fit()
    result, amount = diet._result()
    return result, amount
    
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
def exec():
    # handle json data and optimization.
    try:
        req_data = request.get_json()
        result, amount = run(req_data["nutrients"],req_data["data"])
        return jsonify({"Result":result,"amount":amount})
    except Exception as e:
        return jsonify(e)

@app.route("/opt/sheets",methods=['POST'])
def run_sheet():
    req_data = request.get_json()
    try:
        hs = HandleSheet(sheet_url = req_data["sheet_url"])
        nutrients, foods = hs.read_sheet().data_to_json().get_data()
        result, amount = run(nutrients, foods)
        return jsonify({"result":result,"amount":amount})
    except Exception as e:
        
        return jsonify("Dataset has a limited. 200 foods!")
    
@app.route("/")
def home():
    return "<h2><a href='https://github.com/withoutCoffee/DietOptimization'>>Info<</h2>"

if __name__ == '__main__':
    app.run()


    