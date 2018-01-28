#!/bin/sh
set -e
source /phonebank/venv/bin/activate
/phonebank/phone.py --redishost $REDISHOST
