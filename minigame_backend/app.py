from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from apiHandler import apiHandler

app = Flask(__name__)
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/login")
def serve(path):
    return jsonify({'answer':[1,2,3,4,5,6,7,8,9]})

api.add_resource(apiHandler, '/answers')