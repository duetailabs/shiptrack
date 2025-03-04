from flask import Flask, jsonify
import requests

app = Flask(__name__)

# --- Discovery API Implementation ---
@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Returns metadata about the shipping service.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })


# --- Example Usage (Optional, for demonstration) ---
@app.route('/app-details', methods=['GET'])
def get_app_details():
    """Fetches app details from the /discovery endpoint."""
    try:
        response = requests.get('http://localhost:5000/discovery')  # Adjust URL if needed, 5000 is default flask port
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        return jsonify({"name": data.get('name', 'Unknown App'), "version": data.get('version', 'Unknown Version')})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching app details: {e}")
        return jsonify({"error":"Error fetching app details"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
#Generate error condition
@app.errorhandler(404)
def page_not_found(e):
    """
    Returns a custom 404 error message.
    """
    return jsonify({"error": "Page not found"}), 404
