import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def environ():
    return jsonify({k:v for k, v in os.environ.items()})
    