from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, abort
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import linear_model
import joblib
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):
    def get(self):
        json_data = {"petal_length": 5.6}
        model = pickle.load(open("modelPickle","rb"))
        resultado = model.predict([[float(json_data['petal_length'])]])
        return resultado.tolist()


    def post(self):
        json_data = request.get_json(force=True)
        model = pickle.load(open("modelPickle","rb"))
        resultado = model.predict([[float(json_data['petal_length'])]])
        return resultado.tolist()


api.add_resource(HelloWorld,'/')

if __name__=='__main__':
    application.run(debug=False,host='0.0.0.0',port=5000)