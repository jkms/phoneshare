from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.route('/')
def hello_world():
	return 'Hello World!'
numbers = [
    {
        'id': 1,
        'e164': u'+16048675309',
    },
    {
        'id': 2,
        'e165': u'+16045555555',
    }
]

@app.route('/api/v1.0/numbers', methods=['GET'])
def get_numbers():
    return jsonify({'numbers': numbers})

@app.route('/api/v1.0/numbers/<int:number_id>', methods=['GET'])
def get_number(number_id):
    number = [number for number in numbers if number['id'] == number_id]
    if len(number) == 0:
        abort(404)
    return jsonify({'number': number[0]})


@app.route('/api/v1.0/numbers', methods=['POST'])
def create_number():
    if not request.json or not 'e164' in request.json:
        abort(400)
    number = {
        'id': numbers[-1]['id'] + 1,
        'e164': request.json['e164']
    }
    numbers.append(number)
    return jsonify({'number': number}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)
