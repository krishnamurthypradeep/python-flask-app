from flask import Flask, jsonify, render_template

from model import db

app = Flask(__name__)


@app.route("/api/v1/data")
def welcome():
    return jsonify(db)


app.run("0.0.0.0", 5001)


