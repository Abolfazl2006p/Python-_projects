from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = "my_super_secret_key"

users = {
    1: {"id": 1, "username": "wiener", "email": "wiener@test.com", "api_key": "KEY_WIENER_123"},
    2: {"id": 2, "username": "carlos", "email": "carlos@test.com", "api_key": "KEY_CARLOS_456"},
    3: {"id": 3, "username": "admin", "email": "admin@test.com", "api_key": "KEY_ADMIN_789"},
}

@app.route("/login")
def login():
    session["user_id"] = 1
    return "Logged in as wiener"

@app.route("/my-account")
def my_account():
    user_id = session.get("user_id")
    
    if not user_id:
        return jsonify({"error": "Please login first"}), 401
        
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
    