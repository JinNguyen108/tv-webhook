import os
from flask import Flask, request, send_file, jsonify
import json

app = Flask(__name__)

# Nếu file chưa có thì tạo file rỗng khi server khởi động
if not os.path.exists("signals.json"):
    with open("signals.json", "w") as f:
        json.dump({"status": "no signal yet"}, f)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    data = request.json
    print("[TradingView Alert]", data)

    with open("signals.json", "w") as f:
        json.dump(data, f)

    return "Signal received", 200

@app.route('/signals.json', methods=['GET'])
def send_signals():
    try:
        return send_file("signals.json", mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
