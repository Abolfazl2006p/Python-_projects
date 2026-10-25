from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"id": 1, "username": "wiener", "email": "wiener@test.com", "api_key": "KEY_WIENER_123"},
    2: {"id": 2, "username": "carlos", "email": "carlos@test.com", "api_key": "KEY_CARLOS_456"},
    3: {"id": 3, "username": "admin", "email": "admin@test.com", "api_key": "KEY_ADMIN_789"},
}

@app.route("/my-account")
def my_account():
    user_id = request.args.get("user_id", type=int)
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "user not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
    