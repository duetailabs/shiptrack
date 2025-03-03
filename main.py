from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Returns a JSON response containing details about the shipping service.

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
# Generate error conditions
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


