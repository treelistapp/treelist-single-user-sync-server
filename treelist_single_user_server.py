import json
import shelve

from flask import Flask
from flask import request, Response

app = Flask(__name__)
db = shelve.open('treelist-data')

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
    
app.run(port=3000, debug=False)
db.close()