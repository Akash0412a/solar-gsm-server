from flask import Flask, request, jsonify

app = Flask(__name__)

latest = {}

@app.route("/data", methods=["POST"])
def receive():

    latest["voltage"] = request.form.get("voltage")
    latest["current"] = request.form.get("current")
    latest["temperature"] = request.form.get("temperature")

    print("DATA RECEIVED:", latest)

    return "OK"


@app.route("/latest")
def latest():

    return jsonify(latest)


app.run(host="0.0.0.0", port=10000)