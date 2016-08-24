#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Development REST Server
# Written in Python 2
# Uses Flask
#     Debian package: python-flask
#     Pip: flask
# Author: Andreas Bader
# https://github.com/baderas/pyRESTDevServer

# Takes every POST Request and prints it out

# Usage:
# Start Server:
#    ./pyRESTDevServer.py
# Test with curl:
#    curl -i -H "Content-Type: application/json" -X POST -d @test.json http://localhost:5000/write

__author__ = 'Andreas Bader'
__version__ = "0.01"

import flask
import logging

conn = None

app = flask.Flask(__name__)

# Configure Logging
logLevel = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logLevel)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logLevel)
logger.addHandler(handler)

@app.route('/write', methods=['POST'])
def handle_write():
    logger.info("Got a POST request.")
    if flask.request.json:
        body = flask.request.get_json()
        logger.info("Got a json body with the following content:")
        logger.info(flask.json.dumps(body))
    return "",200 # 200 stands for "OK", use 201 for "CREATED"

@app.errorhandler(404)
def not_found(error):
    return  flask.make_response(flask.json.jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(debug=True) 

logger.info("End.")
