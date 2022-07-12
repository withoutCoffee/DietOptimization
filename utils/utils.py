# Solution test for diet problem, with simples inside ortools
import json
from ortools.linear_solver import pywraplp
import pandas as pd
import numpy as np


def json_to_csv(data_path,write_path):
    data_cols = [
        "Food",
        "Unit",
        "Price(cents)",
        "Calories (kcal)",
        "Protein (g)",
        "Calcium (g)",
        "Iron (mg)",
        "Vitamin A (KIU)",
        "Thiamine (mg)",
        "Riboflavin (mg)",
        "Niacin (mg)",
        "Ascorbic Acid (mg)"]

    with open(data_path) as openfile:
        # Read file as a python list
        data = json.load(openfile)
        # Write excel file with pandas
        pd.DataFrame(data=data,columns = data_cols).to_excel(write_path)

def read_json(data_path):
    with open(data_path) as openfile:
        # Read file as a python list
        data = json.load(openfile)
        print(data)



if __name__ == "__main__":

    data_path = "data/data.json"
    write_path = "data/data.xlsx"
    #json_to_csv(data_path,write_path)
    #read_json(data_path)