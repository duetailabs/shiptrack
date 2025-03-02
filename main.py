from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Provides discovery information for the shipping service.

    Returns:
        JSON: A dictionary containing the service's name, version, owners, team, and organization.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)
#Genertae code for error conditions
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 Not Found errors.

    Args:
        error: The error object.

    Returns:
        JSON: A dictionary containing an error message and status code.
    """
    return jsonify({'error': 'Not found', 'status_code': 404}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 Internal Server errors.

    Args:
        error: The error object.

    Returns:
        JSON: A dictionary containing an error message and status code.
    """
    return jsonify({'error': 'Internal Server Error', 'status_code': 500}), 500

