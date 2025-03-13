import json
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Returns a JSON response containing information about the shipping service.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

# create liveness and readiness endpoints
@app.route('/live', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/ready', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
