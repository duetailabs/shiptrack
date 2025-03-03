import requests
from flask import jsonify, Flask

app = Flask(__name__)


def discovery():
    """
    Returns a JSON response containing details about the shipping service.

    This function provides metadata about the "shipping" service, including its name,
    version, owners, team, and organization.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

def get_app_details():
    """
    Fetches app details from the /discovery endpoint.

    This function sends a GET request to the /discovery endpoint (assumed to be on
    localhost:8000) and extracts the 'name' and 'version' from the JSON response.
    It handles potential request errors and returns default values if something goes wrong.

    Returns:
        tuple: A tuple containing the app's name and version (both strings).
    """
    try:
        response = requests.get('http://localhost:8000/discovery')  # Adjust URL if needed
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return data.get('name', 'Unknown App'), data.get('version', 'Unknown Version')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching app details: {e}")
        return "Unknown App", "Unknown Version"
    
@app.route('/discovery', methods=['GET'])
def discovery_route():
    """
    Flask route for the /discovery endpoint.

    This function maps the /discovery URL to the discovery() function, making it accessible
    via HTTP GET requests.

    Returns:
      JSON response with service details
    """
    return discovery()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
#Generate error conditions
@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found errors.

    Returns:
        JSON response with an error message and a 404 status code.
    """
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Error handler for 500 Internal Server Error.

    Returns:
        JSON response with an error message and a 500 status code.
    """
    return jsonify({'error': 'Internal Server Error'}), 500

@app.errorhandler(400)
def bad_request(error):
    """
    Error handler for 400 Bad Request errors.

    Returns:
        JSON response with an error message and a 400 status code.
    """
    return jsonify({'error': 'Bad Request'}), 400
