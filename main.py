from flask import Flask, jsonify

app = Flask(__name__)

def discovery():
    """
    Implements the Discovery API endpoint.

    Returns:
        JSON response containing service metadata.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })

@app.route('/discovery', methods=['GET'])
def discovery_route():
    """
    Flask route handler for the /discovery endpoint.

    Returns:
        JSON response from the discovery() function.
    """
    return discovery()

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
#generate error condition based code
@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found errors.

    Args:
        error: The error object.

    Returns:
        JSON response with error details and 404 status code.
    """
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Error handler for 500 Internal Server Error.

    Args:
        error: The error object.

    Returns:
        JSON response with error details and 500 status code.
    """
    return jsonify({'error': 'Internal Server Error'}), 500
