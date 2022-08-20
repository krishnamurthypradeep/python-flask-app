from flask import Flask, jsonify, render_template
import os
from model import db

app = Flask(__name__)


@app.route("/api/v1/data")
def welcome():
    return jsonify(db)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


