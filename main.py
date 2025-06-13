#Create the discovery, liveness, and readiness endpoints
from flask import Flask, jsonify
import time

app = Flask(__name__)

# Acme Corp standard backend routes
# Acme Corp discovery backend route
@app.route('/discovery', methods=['GET'])
def discovery():
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

# Acme Corp liveness backend route
@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

# Acme Corp readiness backend route
@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})
# End of Acme Corp standard backend routes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)