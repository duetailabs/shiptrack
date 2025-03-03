from flask import jsonify

def discovery():
    """
    Implements the /discovery backend route.

    Returns:
        JSON response containing the service's name, version, owners, team, and organization.
    """
    return jsonify({
        "name": "shipping",
        "version": "1.0",
        "owners": ["ameerabb", "lonestar"],
        "team": "genAIs",
        "organization": "acme"
    })
# Generate error conditions
def not_found_error(error):
    """
    Handles 404 Not Found errors.

    Args:
        error: The error object.

    Returns:
        JSON response with a 404 status code.
    """
    return jsonify({'error': 'Not found'}), 404

def bad_request_error(error):
    """
    Handles 400 Bad Request errors.

    Args:
        error: The error object.

    Returns:
        JSON response with a 400 status code.
    """
    return jsonify({'error': 'Bad request'}), 400

def internal_server_error(error):
    """
    Handles 500 Internal Server errors.

    Args:
        error: The error object.

    Returns:
        JSON response with a 500 status code.
    """
    return jsonify({'error': 'Internal server error'}), 500


