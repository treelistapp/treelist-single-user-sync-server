import json
import shelve

from flask import Flask
from flask import request, Response

from secret import secret_path, port

app = Flask(__name__)
db = shelve.open('treelist.data')

def json_response(obj):
    return Response(json.dumps(obj), mimetype='application/json')

@app.route('/')
def index():
    return json_response({'status': 'ok'})

@app.route('/' + secret_path, methods=['POST'])
def write():
    data = request.json
    db['data'] = data
    print(data)
    return json_response({'data': data})

@app.route('/' + secret_path, methods=['GET'])
def read():
    data = db.get('data', {})
    return json_response(data)

app.run(port=port, debug=False)
db.close()