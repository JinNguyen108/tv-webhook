from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    data = request.json
    print("Alert received:", data)

    # Ghi vào file
    with open("signals.json", "w") as f:
        json.dump(data, f)

    return "Signal received", 200
    
@app.route('/signals.json', methods=['GET'])
def send_signals():
    print("[MT5 GET] signals.json was requested")
    return send_file("signals.json", mimetype='application/json')
