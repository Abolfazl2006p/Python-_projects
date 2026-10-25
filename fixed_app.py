from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = "my_super_secret_key"

users = {
    1: {"id": 1, "username": "wiener", "email": "wiener@test.com", "api_key": "KEY_WIENER_123"},
    2: {"id": 2, "username": "carlos", "email": "carlos@test.com", "api_key": "KEY_CARLOS_456"},
    3: {"id": 3, "username": "admin", "email": "admin@test.com", "api_key": "KEY_ADMIN_789"},
}

@app.route("/")
def index():
    return """
    <html>
        <body>
            <h1>Welcome to the Test App</h1>
            
            <h3>Search</h3>
            <form action="/search" method="GET">
                <input type="text" name="q">
                <input type="submit" value="Search">
            </form>

            <hr>
            
            <a href="/login">Go to Login</a><br>
            <a href="/my-account">Go to My Account</a>
            <form action="/login" method="POST">
                <input type="text" name="username">
                <input type="password" name="password">
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

@app.route("/login", methods=["GET", "POST"])
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

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if "'" in query:
        return "Error: sqlite3.OperationalError: syntax error", 500
    return f"No results for {query}"

if __name__ == "__main__":
    app.run(debug=True)