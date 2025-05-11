from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    try:
        data = request.get_data(as_text=True)  # nhận text thuần
        with open("signals.txt", "w") as f:
            f.write(data.strip())  # Ghi vào file, bỏ khoảng trắng
        return "Signal received", 200
    except Exception as e:
        return str(e), 500

@app.route('/signals.txt', methods=['GET'])
def get_signal():
    return send_file("signals.txt", mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
