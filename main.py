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
