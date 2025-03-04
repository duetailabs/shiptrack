from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

# Load package data from JSON file
try:
    with open('packages.json', 'r') as f:
        packages = json.load(f)
except FileNotFoundError:
    print("Error: packages.json not found.")
    exit(1)


@app.route('/packages/<packageId>', methods=['GET'])
def get_package(packageId):
    """
    Get information about a package.
    This endpoint retrieves package details based on the provided package ID.
    :param packageId: The ID of the package.
    :return: JSON response containing package information or 404 if not found.
    """
    for package_data in packages:
        if package_data['packageId'] == packageId:
            return jsonify({
                "height": package_data['height'],
                "width": package_data['width'],
                "depth": package_data['depth'],
                "weight": package_data['weight'],
                "special_handling_instructions": package_data['special_handling_instructions']
            })
    abort(404, description="Package not found")

# Live backend route
@app.route('/liveness', methods=['GET'])
def liveness():
    return jsonify({"status": "live", "code": 200, "timestamp": time.time()})

# Ready backend route
@app.route('/readiness', methods=['GET'])
def readiness():
    return jsonify({"status": "ready", "code": 200, "timestamp": time.time()})

if __name__ == '__main__':
    app.run(debug=True)
