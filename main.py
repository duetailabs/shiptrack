from flask import Flask, jsonify

app = Flask(__name__)

def discovery():
    """
    Returns a JSON response containing discovery information about the shipping service.
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
    Flask route for the /discovery endpoint.
    Calls the discovery function and returns its result.
    """
    return discovery()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
#Generate new error conditions
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400
