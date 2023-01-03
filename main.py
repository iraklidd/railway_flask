from flask import Flask, jsonify
from dotenv import load_dotenv
# load_dotenv()
import os


# PWD = os.getenv("parolie")

app = Flask(__name__)
# app.config['DEBUG'] = True


@app.route('/')
def index():
    # return jsonify({"Jariskacis parolia: ": PWD })
    return jsonify({"Jariskacis parolia: ": "PWD" })


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
