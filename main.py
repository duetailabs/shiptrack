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
#genartae code for liveness
from remote_context_snippets import sample_harvest_API, sample_post_pod_status_API, sample_get_pod_status_API, sample_pallette_service_API
@app.route('/sample_harvest_API', methods=['GET'])
def sample_harvest_API_route():
    sample_harvest_API()
    return "sample_harvest_API executed"

@app.route('/sample_post_pod_status_API', methods=['POST'])
def sample_post_pod_status_API_route():
    sample_post_pod_status_API()
    return "sample_post_pod_status_API executed"

@app.route('/sample_get_pod_status_API', methods=['GET'])
def sample_get_pod_status_API_route():
    sample_get_pod_status_API()
    return "sample_get_pod_status_API executed"

@app.route('/sample_pallette_service_API', methods=['POST'])
def sample_pallette_service_API_route():
    sample_pallette_service_API()
    return "sample_pallette_service_API executed"
