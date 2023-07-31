#!/usr/bin/python3
""" Flask app """

from flask import Flask
from models import storage
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
    app.run(host='0.0.0.0', port=5000,)
