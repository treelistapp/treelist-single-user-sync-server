import json
import shelve
import random

from flask import Flask
from flask import request, Response
from flask_cors import CORS

from secret import secret_path, port

app = Flask(__name__)
CORS(app)
db = shelve.open('treelist.data')

def json_response(obj):
    return Response(json.dumps(obj), mimetype='application/json')

@app.route('/')
def index():
    return json_response({'status': 'ok'})

@app.route(secret_path + '/hash')
def get_hash():
    hash_value = db.get('hash', 0)
    return json_response({'hash': hash_value})

@app.route(secret_path, methods=['POST'])
def write():
    data = request.json
    db['data'] = data
    hash_value = random.random() # good enough because no false negatives and <1% false positives in normal use
    db['hash'] = hash_value
    return json_response({
        'status': 'ok',
        'hash': hash_value
    })

@app.route(secret_path, methods=['GET'])
def read():
    data = db.get('data', {})
    data['hash'] = db.get('hash', 0)
    return json_response(data)

app.run(port=port, debug=False)
db.close()