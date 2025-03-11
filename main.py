import uuid
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

class User:
    """Represents a user in the system."""

    def __init__(self, username, email, password, user_id=None):
        self.user_id = user_id or str(uuid.uuid4())  # Generate unique ID if not provided
        self.username = username
        self.email = email
        self.password = password  # In real app, hash this!

    def to_dict(self):
        """Converts user data to a dictionary."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password,  # In real app, don't store plain password
        }

    @staticmethod
    def from_dict(data):
        """Creates a User object from a dictionary."""
        return User(
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )


class UserManager:
    """Manages user data (CRUD operations)."""

    def __init__(self, data_file="users.json"):
        self.data_file = data_file
        self.users = self._load_users()

    def _load_users(self):
        """Loads user data from the JSON file."""
        if not os.path.exists(self.data_file):
          with open(self.data_file, 'w') as f:
            json.dump([], f)

        try:
            with open(self.data_file, "r") as f:
                user_data = json.load(f)
                return {
                    user["user_id"]: User.from_dict(user) for user in user_data
                }
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print(f"Error: Corrupted users data file at {self.data_file}.  Starting with empty database")
            return {}
        

    def _save_users(self):
        """Saves user data to the JSON file."""
        user_data = [user.to_dict() for user in self.users.values()]
        with open(self.data_file, "w") as f:
            json.dump(user_data, f, indent=4)

    def create_user(self, username, email, password):
        """Creates a new user."""
        if any(user.username == username for user in self.users.values()):
            raise ValueError(f"Username '{username}' already exists.")
        if any(user.email == email for user in self.users.values()):
            raise ValueError(f"Email '{email}' already exists.")

        user = User(username, email, password)
        self.users[user.user_id] = user
        self._save_users()
        return user

    def get_user(self, user_id):
        """Retrieves a user by ID."""
        user = self.users.get(user_id)
        if user is None:
          raise ValueError(f"User with ID: {user_id} not found")
        return user
    
    def get_user_by_username(self, username):
      """Retrieves a user by username"""
      for user in self.users.values():
        if user.username == username:
          return user
      raise ValueError(f"User with username: {username} not found")

    def get_all_users(self):
        """Retrieves all users."""
        return list(self.users.values())

    def update_user(self, user_id, username=None, email=None, password=None):
        """Updates an existing user."""
        user = self.get_user(user_id)
        if username:
          if any(u.username == username for u in self.users.values() if u.user_id != user_id):
              raise ValueError(f"Username '{username}' already exists.")
          user.username = username
        if email:
          if any(u.email == email for u in self.users.values() if u.user_id != user_id):
              raise ValueError(f"Email '{email}' already exists.")
          user.email = email
        if password:
            user.password = password  # In real app, hash this!
        self._save_users()
        return user

    def delete_user(self, user_id):
        """Deletes a user."""
        user = self.get_user(user_id)
        del self.users[user_id]
        self._save_users()

#create user manager instance
manager = UserManager()

# discovery route function
@app.route('/discovery', methods=['GET'])
def discovery():
    """
    Provides information about available services.
    """
    services = {
        "users": {
            "description": "Manage user accounts",
            "endpoints": [
                {
                    "method": "POST",
                    "url": "/users",
                    "description": "Create a new user"
                },
                {
                    "method": "GET",
                    "url": "/users/<user_id>",
                    "description": "Get a user by ID"
                },
                {
                    "method": "GET",
                    "url": "/users",
                    "description": "Get all users"
                },
                {
                    "method": "PUT",
                    "url": "/users/<user_id>",
                    "description": "Update an existing user"
                },
                 {
                    "method": "GET",
                    "url": "/users/username/<username>",
                    "description": "Get a user by username"
                },
                {
                    "method": "DELETE",
                    "url": "/users/<user_id>",
                    "description": "Delete a user"
                }
            ]
        }
        # Add more services here
    }
    return jsonify(services)

if __name__ == "__main__":
  app.run(debug=True)
#Generate error conditioins
@app.errorhandler(ValueError)
def handle_value_error(error):
    """Handles ValueError exceptions."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(Exception)
def handle_generic_error(error):
    """Handles generic exceptions."""
    return jsonify({"error": "An unexpected error occurred."}), 500
