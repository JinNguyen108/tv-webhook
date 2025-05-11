from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/tv-alert', methods=['POST'])
def tv_alert():
    try:
        data = request.get_data(as_text=True).strip()

        # Đọc các dòng hiện có nếu có file
        lines = []
        if os.path.exists("signals.txt"):
            with open("signals.txt", "r") as f:
                lines = f.read().splitlines()

        # Thêm dòng mới vào đầu danh sách
        lines.insert(0, data)

        # Chỉ giữ lại 5 dòng gần nhất
        lines = lines[:5]

        # Ghi lại file
        with open("signals.txt", "w") as f:
            f.write('\n'.join(lines))

        return "Signal received", 200
    except Exception as e:
        return str(e), 500


@app.route('/signals.txt', methods=['GET'])
def get_signals():
    return send_file("signals.txt", mimetype='text/plain')
