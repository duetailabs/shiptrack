from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Returns metadata about the service.

    This endpoint provides information such as the service name,
    version, owners, team, and organization.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
# Generate standard liveness and readiness routes
from remote_context_snippets import liveness, readiness

@app.route('/live', methods=['GET'])
def live():
    return liveness()

@app.route('/ready', methods=['GET'])
def ready():
    return readiness()
#generate  code with error conditions
import time

def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})
#generate code with errors
from flask import abort, request
from data_model import Package
from connect_connector import SessionMaker

# function that returns the name and version of the app
import requests

def get_app_details():
    """Fetches app details from the /discovery endpoint."""
    try:
        response = requests.get('http://localhost:8000/discovery')  # Adjust URL if needed
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get('name', 'Unknown App'), data.get('version', 'Unknown Version')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching app details: {e}")
        return "Unknown App", "Unknown Version"

# get a package from CloudSQL database
# Endpoint that retrieves package details based on the provided product ID
@app.route('/packages/<int:product_id>', methods=['GET'])
def retrieve_package_by_product_id(product_id):
    """
    Get information about a package.
    This endpoint retrieves package details based on the provided product ID.
    :param product_id: The ID of the product.
    :return: JSON response containing package information or 404 if not found.
    """
    session = SessionMaker()
    package = session.query(Package).filter(Package.product_id == int(product_id)).first()
    session.close()

    if package:
        return jsonify({
            "height": package.height,
            "width": package.width,
            "depth": package.depth,
            "weight": package.weight,
            "special_handling_instructions": package.special_handling_instructions
        })
    else:
        app_name, app_version = get_app_details()
        abort(404, description={
            "message": "The product_id was not found",
            "timestamp": time.time(),
            "app_name": app_name,
            "version": app_version,
            "called_method": "get_package",
            "product_id": product_id
        })

# create a new package in the CloudSQL database
# Endpoint that creates a