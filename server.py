from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

latest = {
    "voltage": 0,
    "current": 0,
    "temperature": 0
}

# -------------------------
# Receive data from GSM
# -------------------------

@app.route("/data", methods=["POST"])
def receive():

    latest["voltage"] = request.form.get("voltage")
    latest["current"] = request.form.get("current")
    latest["temperature"] = request.form.get("temperature")

    print("DATA RECEIVED:", latest)

    return "OK"


# -------------------------
# Provide latest data
# -------------------------

@app.route("/latest")
def get_data():

    return jsonify(latest)


# -------------------------
# Dashboard UI
# -------------------------

@app.route("/")
def dashboard():

    return send_file("dashboard.html")


# -------------------------
# Run server
# -------------------------

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
