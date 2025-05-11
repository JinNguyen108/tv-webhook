import os
from flask import Flask, request, send_file
import json

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    data = request.json
    print("[TradingView Alert]", data)

    with open("signals.json", "w") as f:
        json.dump(data, f)

    return "Signal received", 200

@app.route('/signals.json', methods=['GET'])
def send_signals():
    return send_file("signals.json", mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
