from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

import redis
import hashlib
r = redis.Redis(
    host='localhost'
)
m = hashlib.sha256()
hash = hashlib.sha256()
m.update(b'+16048675309')

r.hset(m.hexdigest(), 'name', 'Jenny')

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/v1.0/numbers', methods=['GET'])
def get_numbers2():
    return jsonify({'numbers': numbers})

@app.route('/api/v1.0/numbers/<string:e164>', methods=['GET'])
def get_number2(e164):
    hget_number = hashlib.sha256()
    hget_number.update(bytes(e164, encoding='utf-8'))
    name = r.hget(hget_number.hexdigest(), 'name').decode('ascii')
#    if len(number) == 0:
#        abort(404)
#    return jsonify({'number': [number]})
    return jsonify({'Name': name})


@app.route('/api/v1.0/numbers', methods=['POST'])
def create_number2():
    hget_number = hashlib.sha256()
    hget_number.update(bytes(request.json['e164'], encoding='utf-8'))
    if r.exists(hget_number.hexdigest()):
        abort(400)
    if not request.json or not 'e164' in request.json:
        abort(400)

    r.hset(hget_number.hexdigest(), 'name', request.json['name'])
    return jsonify({'Name': r.hget(hget_number.hexdigest(), 'name').decode('ascii')}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)
