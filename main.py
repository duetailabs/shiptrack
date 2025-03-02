from flask import Flask, jsonify

app = Flask(__name__)

# --- Backend Handlers (similar to backend_handlers.py) ---

def discovery():
    """
    Returns metadata about the service.
    """
    return jsonify({
        "name": "shipping",  # Or another suitable name for your application
        "version": "1.0",  # Or the current version
        "owners": ["ameerabb", "lonestar"], # Or the contact people of the app.
        "team": "genAIs", # Or the name of your team.
        "organization": "acme" # Or your organization name.
    })

# --- Routes ---

@app.route('/discovery', methods=['GET'])
def discovery_route():
    """
    Exposes the discovery metadata as a GET endpoint.
    """
    return discovery()


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Run on port 8000 (or your preferred port)
# Generate standard liveness and readiness routes
import time

@app.route('/live', methods=['GET'])
def liveness():
    """
    Returns a liveness probe response.
    """
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

@app.route('/ready', methods=['GET'])
def readiness():
    """
    Returns a readiness probe response.
    """
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})
