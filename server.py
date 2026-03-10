from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest = {}

@app.route("/")
def home():
    return "Solar GSM Server Running"

@app.route("/data", methods=["POST"])
def receive():

    latest["voltage"] = request.form.get("voltage")
    latest["current"] = request.form.get("current")
    latest["temperature"] = request.form.get("temperature")

    print("DATA RECEIVED:", latest)

    return "OK"

@app.route("/latest")
def get_latest():

    return jsonify(latest)

app.run(host="0.0.0.0", port=10000)
