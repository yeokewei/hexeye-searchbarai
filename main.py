from flask import Flask, request, jsonify
from flask_cors import CORS
from model import search

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hexeye Search:D!"

@app.route('/predict', methods=['GET'])
def predict():
    args = request.args
    print("arg")
    # data = request.get_json() 
    print(args.items())
    query = args['query']
    print(query)
    top_index= search(query)
    
    return top_index