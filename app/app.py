from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "FinTech Stock Trend Analysis",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/stock")
def stock():
    return jsonify({
        "symbol": "AAPL",
        "trend": "UP",
        "price": 225
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)