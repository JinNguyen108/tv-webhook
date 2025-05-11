from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    data = request.get_data(as_text=True)
    with open("signals.txt", "w") as f:
        f.write(data.strip())
    return "OK", 200

@app.route('/signals.txt', methods=['GET'])
def get_signals():
    return send_file("signals.txt", mimetype='text/plain')
