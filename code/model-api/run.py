# -*- coding: UTF-8 -*-
import model
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello!!'

@app.route('/predict', methods=['POST'])
def postInput():
    msg = request.get_json()
    input = msg['text']

    result = model.predict(input)

    return jsonify({'return': str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)