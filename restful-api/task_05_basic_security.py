from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, 
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# --- 1. Initialization and Configuration ---

app = Flask(__name__)

# Basic Auth Initialization
basic_auth = HTTPBasicAuth()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in production!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
jwt = JWTManager(app)

# User Data Store (In-memory)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- 2. Basic Authentication Implementation ---

@basic_auth.verify_password
def verify_password(username, password):
    """Callback function for Flask-HTTPAuth to verify credentials."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

# --- 3. JWT Authentication Implementation ---

@app.route('/login', methods=['POST'])
def login():
    """Route for users to log in and receive a JWT access token."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        # Returning 400 Bad Request for malformed login request
        return jsonify({"msg": "Missing username or password"}), 400

    username = data.get('username', None)
    password = data.get('password', None)

    if username not in users or not check_password_hash(users[username]["password"], password):
        # Returning 401 Unauthorized for invalid credentials
        return jsonify({"msg": "Bad username or password"}), 401

    # Create a token with the user's identity and their role in the extra payload
    additional_claims = {"role": users[username]["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    
    return jsonify(access_token=access_token)

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    # current_user = get_jwt_identity() # Not strictly needed, but useful for context
    return "JWT Auth: Access Granted"

# --- 4. Role-based Access Control (RBAC) ---

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Route accessible only to users with the 'admin' role."""
    
    # Get the entire JWT payload (claims)
    claims = get_jwt()
    
    # Check if the 'role' claim exists and is equal to 'admin'
    if claims.get('role') == 'admin':
        return "Admin Access: Granted"
    else:
        # Return 403 Forbidden if the role is not 'admin'
        return jsonify({"error": "Admin access required"}), 403

# --- 5. JWT Error Handlers (Mandatory 401 response) ---

@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
def handle_auth_error(err):
    """
    Catch-all handler for various JWT authentication errors.
    Crucial for consistently returning a 401 Unauthorized status code.
    """
    # The error message can be generic or based on the 'err' argument
    # We use a generic 401 message for compliance with security best practices/tests
    return jsonify({"error": "Missing or invalid authentication token"}), 401

# Optional: Basic Auth Unauthorized Handler
# Flask-HTTPAuth automatically handles 401, but a custom handler can be added if needed
@basic_auth.error_handler
def basic_auth_error(status):
    """Handles 401 errors for Basic Auth."""
    # Ensure a 401 Unauthorized response is returned
    return jsonify({"error": "Unauthorized Access"}), 401


if __name__ == '__main__':
    # Run the Flask development server
    app.run()
