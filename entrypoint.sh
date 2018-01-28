#!/bin/sh
set -e
#nohup redis-server &
cd /phonebank
source venv/bin/activate
#exec "$@"
python3 /phonebank/phone.py --redishost $REDISHOST
