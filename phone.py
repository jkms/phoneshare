#!/usr/bin/env python3

from flask import Flask, jsonify, abort, make_response, request

import redis
import hashlib
import time
import datetime

import argparse

app = Flask(__name__)
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--redishost', help='Name or IP of Redis host', nargs='?', const='localhost', type=str,
                    default='localhost')
args = parser.parse_args()

r = redis.Redis(
    host=args.redishost,
    charset='utf-8'
)
m = hashlib.sha256()
m.update(b'+16048675309')

r.hset(m.hexdigest(), 'name', 'Jenny')


def decode(l):
    if isinstance(l, list):
        return [decode(x) for x in l]
    else:
        return l.decode('utf-8')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1.0/numbers/<string:e164>', methods=['GET'])
def get_number2(e164):
    hget_number = hashlib.sha256()
    hget_number.update(bytes(e164, encoding='utf-8'))
    name = decode(r.hget(hget_number.hexdigest(), 'name'))
    #    if len(number) == 0:
    #        abort(404)
    #    return jsonify({'number': [number]})
    return jsonify({'Name': name})


@app.route('/api/v1.0/calls/<string:e164>', methods=['GET'])
def get_calls(e164):
    he164 = hashlib.sha256()
    he164.update(bytes(e164, encoding='utf-8'))
    print('calls:' + he164.hexdigest())
    call_list = decode(r.hvals('calls:' + he164.hexdigest()))
    print(call_list)
    return jsonify({'Calls': call_list}), 201


@app.route('/api/v1.0/numbers', methods=['POST'])
def create_number2():
    hget_number = hashlib.sha256()
    hget_number.update(bytes(request.json['e164'], encoding='utf-8'))
    if r.exists(hget_number.hexdigest()):
        abort(400)
    if not request.json or 'e164' not in request.json:
        abort(400)

    r.hset(hget_number.hexdigest(), 'name', request.json['name'])
    return jsonify({'Name': decode(r.hget(hget_number.hexdigest(), 'name'))}), 201


@app.route('/api/v1.0/campaign/create', methods=['POST'])
def create_campaign():
    hcampaign = hashlib.sha256()
    hcampaign.update(bytes(request.json['name'], encoding='utf-8'))
    if r.exists('campaign:' + hcampaign.hexdigest()):
        abort(400)
    if not request.json or 'name' not in request.json:
        abort(400)
    r.hset('campaign:' + hcampaign.hexdigest(), 'name', request.json['name'])
    return jsonify({'Campaign Name': decode(r.hget('campaign:' + hcampaign.hexdigest(), 'name'))}), 201


@app.route('/api/v1.0/calls', methods=['POST'])
def create_call():
    he164 = hashlib.sha256()
    he164.update(bytes(request.json['e164'], encoding='utf-8'))
    if not r.exists(he164.hexdigest()):
        abort(400)
    if not request.json or 'e164' not in request.json:
        abort(400)
    calltime = time.time()
    r.hset('calls:' + he164.hexdigest(), int(calltime), datetime.datetime.fromtimestamp(calltime))
    return jsonify({'Time Stamp': decode(r.hget('calls:' + he164.hexdigest(), int(calltime)))}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
