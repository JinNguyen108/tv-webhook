import os
from flask import Flask, request, send_file, jsonify
import json

app = Flask(__name__)

# Nếu file chưa tồn tại, tạo file rỗng
if not os.path.exists("signals.json"):
    with open("signals.json", "w") as f:
        json.dump({"status": "no signal yet"}, f)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    data = request.json

    # Ghi dữ liệu nhận được vào file
    with open("signals.json", "w") as f:
        json.dump(data, f)

    return "Signal received", 200

@app.route('/signals.json', methods=['GET'])
def send_signals():
    try:
        return send_file("signals.json", mimetype='application/json')
    except Exception:
        return jsonify({"error": "File not found or cannot be sent"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
