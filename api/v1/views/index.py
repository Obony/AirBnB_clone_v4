#!/usr/bin/python3
""" Api status """

from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods=['GET'])
def status():
    """ return api status """
    if methods:
        response = {"status": "OK"}
        return jsonify(response)
