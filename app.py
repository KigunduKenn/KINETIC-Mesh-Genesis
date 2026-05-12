from flask import Flask, render_template_string, request, jsonify
import hashlib
import time
import threading

app = Flask(__name__)

# --- GENESIS DATA ---
ARCHITECT_ID = "00d2e0c1953a3b2c666c9523a9010c153149d22550ccba7d8aef5ba5de4e1b9d"
MINTED_STAKE = 100_000_000
logic_fragments = []

# HTML Dashboard Template
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>KINETIC Mesh | Genesis Node</title>
    <style>
        body { background: #0a0a0a; color: #00ff41; font-family: 'Courier New', monospace; padding: 20px; }
        .card { border: 1px solid #00ff41; padding: 15px; margin-bottom: 20px; box-shadow: 0 0 10px #00ff41; }
        .mulla { font-size: 2em; color: #fff; }
        .pulse { animation: blink 1s infinite; }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    </style>
</head>
<body>
    <h1>🌐 KINETIC MESH <span class="pulse">●</span></h1>
    <div class="card">
        <h3>ARCHITECT STAKE</h3>
        <p class="mulla">{{ stake }} KINE</p>
        <p>ID: {{ architect_id }}</p>
    </div>
    <div class="card">
        <h3>LATEST LOGIC FRAGMENTS</h3>
        <ul>
            {% for fragment in fragments %}
            <li>[{{ fragment.time }}] {{ fragment.data }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_HTML, stake=f"{MINTED_STAKE:,.0f}", architect_id=ARCHITECT_ID, fragments=logic_fragments[-5:])

@app.route('/mint', methods=['POST'])
def receive_data():
    data = request.json
    # Add data to our live feed
    logic_fragments.append({"time": time.strftime('%H:%M:%S'), "data": f"Phone Verified: {data.get('sensor', 'Unknown')}"})
    return jsonify({"status": "Success", "mulla_minted": 1000})

if __name__ == "__main__":
    # Start the Flask server on Port 7860
    app.run(host="0.0.0.0", port=7860)
