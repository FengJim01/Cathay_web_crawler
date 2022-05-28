import flask
from flask import jsonify, request
import os
import numpy as np
import json
import pandas as pd

def csv2json(csv_path):
    csv = pd.read_csv(csv_path)
    n_row = csv.shape[0]
    json_list = []

    for i in range(n_row):
        

# Basic Flask Setting
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

# Load the csv file
csv_list = os.listdir("./data/")
for i in csv_list:
    
