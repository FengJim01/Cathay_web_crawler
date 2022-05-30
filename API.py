import flask
from flask import jsonify, request
import os
import numpy as np
import json
import pandas as pd
from element_id import element2id
def csv2json(csv_path):
    csv = pd.read_csv(csv_path)
    n_row = csv.shape[0]
    json_list = []

    for i in range(n_row):
        if i == 0: continue # ignore the first row due to the introduction
        row_info = csv.loc[i,:]
        row_dict = {}
        for index,value in zip(row_info.index, row_info.values):
            if type(value) is np.int64: value = int(value)
            elif type(value) is np.float64: value = float(value)

            row_dict[index] = value 
        json_list.append(row_dict)
    return json_list

# Basic Flask Setting
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

# Load the csv file
A_json = csv2json(os.path.join("./data/","A_lvr_land_A.csv"))
B_json = csv2json(os.path.join("./data/","B_lvr_land_A.csv"))
E_json = csv2json(os.path.join("./data/","E_lvr_land_A.csv"))
F_json = csv2json(os.path.join("./data/","F_lvr_land_A.csv"))
H_json = csv2json(os.path.join("./data/","H_lvr_land_A.csv"))

@app.route('/Taipei/all',methods=['GET'])
def Taipei_all():
    return jsonify(A_json)

@app.route("/Taipei",methods=['GET'])
def Taipei_event():
    # Village
    if 'village' in request.args:
        village_id = request.args['village']
        ids = element2id('village')
        village = [value for index,value in ids if int(village_id) == index]
    else:
        village = 0
    # Floor number
    if "floor" in request.args:
        floor_id = request.args['floor']
        ids = element2id('floor')
        floor = [value for index,value in ids if int(floor_id) == index]
    else:
        floor = 0
    # Building Type
    if 'type' in request.args:
        b_type_id = request.args['type']
        ids = element2id('type')
        b_type = [value for index,value in ids if int(b_type_id) == index]
    else:
        b_type = 0
    
    results = []
    for element in A_json:
        if village == 0 or village[0] == element['鄉鎮市區']:
            if floor == 0 or floor[0] == element['總樓層數']:
                if b_type == 0 or b_typr[0] == element['建物型態']:
                    results.append(element)
    return jsonify(results)

@app.route('/Taichung/all',methods=['GET'])
def Taichung_all():
    return jsonify(B_json)

@app.route("/Taichung",methods=['GET'])
def Taichung_event():
    # Village
    if 'village' in request.args:
        village_id = request.args['village']
        ids = element2id('village')
        village = [value for index,value in ids if int(village_id) == index]
    else:
        village = 0
    # Floor number
    if "floor" in request.args:
        floor_id = request.args['floor']
        ids = element2id('floor')
        floor = [value for index,value in ids if int(floor_id) == index]
    else:
        floor = 0
    # Building Type
    if 'type' in request.args:
        b_type_id = request.args['type']
        ids = element2id('type')
        b_type = [value for index,value in ids if int(b_type_id) == index]
    else:
        b_type = 0
    
    results = []
    for element in B_json:
        if village == 0 or village[0] == element['鄉鎮市區']:
            if floor == 0 or floor[0] == element['總樓層數']:
                if b_type == 0 or b_typr[0] == element['建物型態']:
                    results.append(element)
    return jsonify(results)

@app.route('/Kaohsiung/all',methods=['GET'])
def Kaohsiung_all():
    return jsonify(E_json)

@app.route("/Kaohsiung",methods=['GET'])
def Kaohsiung_event():
    # Village
    if 'village' in request.args:
        village_id = request.args['village']
        ids = element2id('village')
        village = [value for index,value in ids if int(village_id) == index]
    else:
        village = 0
    # Floor number
    if "floor" in request.args:
        floor_id = request.args['floor']
        ids = element2id('floor')
        floor = [value for index,value in ids if int(floor_id) == index]
    else:
        floor = 0
    # Building Type
    if 'type' in request.args:
        b_type_id = request.args['type']
        ids = element2id('type')
        b_type = [value for index,value in ids if int(b_type_id) == index]
    else:
        b_type = 0
    
    results = []
    for element in E_json:
        if village == 0 or village[0] == element['鄉鎮市區']:
            if floor == 0 or floor[0] == element['總樓層數']:
                if b_type == 0 or b_typr[0] == element['建物型態']:
                    results.append(element)
    return jsonify(results)

@app.route('/NewTaipei/all',methods=['GET'])
def NewTaipei_all():
    return jsonify(F_json)

@app.route("/NewTaipei",methods=['GET'])
def NewTaipei_event():
    # Village
    if 'village' in request.args:
        village_id = request.args['village']
        ids = element2id('village')
        village = [value for index,value in ids if int(village_id) == index]
    else:
        village = 0
    # Floor number
    if "floor" in request.args:
        floor_id = request.args['floor']
        ids = element2id('floor')
        floor = [value for index,value in ids if int(floor_id) == index]
    else:
        floor = 0
    # Building Type
    if 'type' in request.args:
        b_type_id = request.args['type']
        ids = element2id('type')
        b_type = [value for index,value in ids if int(b_type_id) == index]
    else:
        b_type = 0
    
    results = []
    for element in F_json:
        if village == 0 or village[0] == element['鄉鎮市區']:
            if floor == 0 or floor[0] == element['總樓層數']:
                if b_type == 0 or b_typr[0] == element['建物型態']:
                    results.append(element)
    return jsonify(results)


@app.route('/Taoyuan/all',methods=['GET'])
def Taoyuan_all():
    return jsonify(H_json)

@app.route("/Taoyuan",methods=['GET'])
def Taoyuan_event():
    # Village
    if 'village' in request.args:
        village_id = request.args['village']
        ids = element2id('village')
        village = [value for index,value in ids if int(village_id) == index]
    else:
        village = 0
    # Floor number
    if "floor" in request.args:
        floor_id = request.args['floor']
        ids = element2id('floor')
        floor = [value for index,value in ids if int(floor_id) == index]
    else:
        floor = 0
    # Building Type
    if 'type' in request.args:
        b_type_id = request.args['type']
        ids = element2id('type')
        b_type = [value for index,value in ids if int(b_type_id) == index]
    else:
        b_type = 0
    
    results = []
    for element in H_json:
        if village == 0 or village[0] == element['鄉鎮市區']:
            if floor == 0 or floor[0] == element['總樓層數']:
                if b_type == 0 or b_typr[0] == element['建物型態']:
                    results.append(element)
    return jsonify(results)

app.run()





















