from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Returns details about the service (shipping service in this case).
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
#Generate error conditions
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 Not Found errors.
    """
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 Internal Server errors.
    """
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(400)
def bad_request(error):
    """
    Handles 400 Bad Request errors.
    """
    return jsonify({'error': 'Bad request'}), 400
