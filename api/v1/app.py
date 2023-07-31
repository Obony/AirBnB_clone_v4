#!/usr/bin/python3
""" Flask app """

from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views

# app variable, instance of Flask
app = Flask(__name__)

#register the blueprint app_views to Flask instance app
app.register_blueprint(app_views)

#tear down
@app.teardown_appcontext
def tear_down(self):
    """ remove instance of SQLAlchemy """
    storage.close()

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
