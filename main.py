from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def discovery():
    """
    Returns a JSON response with metadata about the shipping service.
    """
    logger.info("Handling /discovery request")
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

def get_app_details():
    """
    Fetches app details from the /discovery endpoint of another service.
    """
    logger.info("Fetching app details from another service's /discovery endpoint")
    try:
        response = requests.get('http://localhost:8080/discovery')  # Using port 8080 to target the Go example service.
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        logger.info(f"Successfully fetched app details: {data}")
        return data.get('name', 'Unknown App'), data.get('version', 'Unknown Version')
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching app details: {e}")
        return "Unknown App", "Unknown Version"
    
@app.route('/discovery', methods=['GET'])
def discovery_route():
    """
    Flask route for the /discovery endpoint.
    """
    return discovery()

@app.route('/health', methods=['GET'])
def health_route():
    """
    Returns a JSON with status of ok
    """
    logger.info("Handling /health request")
    return jsonify({"status":"ok"})

@app.route('/details', methods=['GET'])
def get_app_details_route():
    name, version = get_app_details()
    return jsonify({"name": name, "version": version})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
# Generate standard liveness and readiness routes
from remote_context_snippets import liveness, readiness
@app.route('/live', methods=['GET'])
def live_route():
    """
    Flask route for the /live endpoint.
    """
    return liveness()

@app.route('/ready', methods=['GET'])
def ready_route():
    """
    Flask route for the /ready endpoint.
    """
    return readiness()
