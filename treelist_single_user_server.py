import json
import shelve

from flask import Flask
from flask import request, Response

from secret import secret_path

app = Flask(__name__)
db = shelve.open('treelist.data')

if 'visit-count' not in db:
    db['visit-count'] = 0

def json_response(obj):
    return Response(json.dumps(obj), mimetype='application/json')

@app.route('/')
def index():
    #resp = request.headers.environ['HTTP_X_REAL_IP']
    db['visit-count'] += 1

    resp = {'status': 'ok', 'visit-count': db['visit-count']}

    return json_response(resp)

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

app.run(port=3000, debug=False)
db.close()