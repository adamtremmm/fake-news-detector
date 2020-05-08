#!/usr/bin/python3
"""
    RESTful API serving predictions on fake news tweets

    curl -i -H "Content-Type: application/json" -X POST -d '{"tweet":"President Trump officially resigned as President of the United States via tweet last night"}' http://localhost:5000/fakenews/api/v1.0/predict
"""
from flask import Flask, jsonify, request, make_response, render_template, abort
from flask_cors import CORS
from fake_news_detector import FakeNewsDetector

app = Flask(__name__)
CORS(app)

detector = FakeNewsDetector()

# @app.route('/<tweet>')
# def index(tweet):
# 	prediction = detector.make_prediction(tweet)
# 	return f'<h1>Tweet: {tweet}\nPrediction: {prediction}</h1>'

# @app.route('/fakenews/api/v1.0/predict/<tweet>', methods=['GET'])
# def get_prediction(tweet):
#     return jsonify({'tweet': tasks})

@app.route('/fakenews/api/v1.0/predict', methods=['POST'])
def create_prediction():
    if not request.json or not 'tweet' in request.json:
        abort(400)

    prediction = detector.make_prediction( request.json['tweet'] )
    p = prediction[0]
    return jsonify({'prediction': p}), 201


if __name__ == '__main__':
	app.run()