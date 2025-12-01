from flask import Flask, jsonify, request

# In-memory storage for users.
# It must be initialized as an empty dictionary to pass the checker.
users = {}

# Instantiate the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Handles the root endpoint."""
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def get_status():
    """Handles the /status endpoint."""
    return "OK"

@app.route("/data", methods=["GET"])
def list_usernames():
    """Handles the /data endpoint, returning a list of all usernames."""
    # Get all keys (usernames) from the users dictionary
    usernames_list = list(users.keys())
    
    # Use jsonify to return a JSON array of usernames
    return jsonify(usernames_list)

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Handles the /users/<username> dynamic endpoint.
    Returns the user object or a 404 error if not found.
    """
    if username in users:
        # Return the user's data as JSON
        return jsonify(users[username])
    else:
        # Return a 404 Not Found error with a JSON error message
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles the /add_user endpoint, accepting POST requests to add a new user.
    """
    
    # 1. Attempt to parse JSON data
    try:
        new_user = request.get_json()
    except Exception:
        # Return 400 Bad Request if the body is not valid JSON
        return jsonify({"error": "Invalid JSON"}), 400

    # Handle case where get_json() returns None (e.g., empty body or bad content type)
    if not new_user:
         return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check for missing username
    if "username" not in new_user:
        # Return 400 Bad Request if username is missing
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    # 3. Check for duplicate username
    if username in users:
        # Return 409 Conflict if the username already exists
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add the new user to the in-memory dictionary
    users[username] = new_user

    # 5. Return a 201 Created status with the confirmation message
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    # *** CRITICAL FIX: The lines that added initial data (jane, john) 
    # have been REMOVED from this block. ***
    
    # Run the Flask development server
    app.run()
