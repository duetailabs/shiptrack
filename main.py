from flask import Flask, jsonify, request, abort
import uuid
import time

app = Flask(__name__)

# In-memory storage for packages (replace with a database in a real application)
packages_db = {}


@app.route('/packages/<string:product_id>', methods=['GET'])
def get_package_by_product_id(product_id):
    """
    Retrieves package details associated with a specific product ID.
    """
    for package_id, package_data in packages_db.items():
      if package_data.get("product_id") == product_id:
        return jsonify({
            "height": package_data["height"],
            "width": package_data["width"],
            "depth": package_data["depth"],
            "weight": package_data["weight"],
            "special_handling_instructions": package_data.get("special_handling_instructions", "")
        })

    # Package not found
    return jsonify({
        "message": f"Package not found for product_id: {product_id}",
        "timestamp": time.time(),
        "app_name": "package-management-service",
        "version": "v1.0.0",
        "called_method": "getPackageByProductId",
        "product_id": product_id
    }), 404


@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package_by_id(package_id):
    """
    Deletes a package based on its unique ID.
    """
    if package_id in packages_db:
        del packages_db[package_id]
        return '', 204
    else:
        return jsonify({"description": f"The package_id: {package_id} was not found"}), 404


# Sample data for testing
def populate_sample_data():
    packages_db[1] = {
        "product_id": "product-123",
        "height": 10.5,
        "width": 5.2,
        "depth": 3.0,
        "weight": 2.5,
        "special_handling_instructions": "Fragile, handle with care"
    }
    packages_db[2] = {
        "product_id": "product-456",
        "height": 15.0,
        "width": 10.0,
        "depth": 8.0,
        "weight": 5.0
    }

populate_sample_data()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
