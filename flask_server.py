from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "WelCome to the Vulnerable server!"      

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'secret123':
        return "LOGIN SUCCESSFUL! you hacked the server."
    else:
        return "LOGIN FAILED! invalid credentials.", 401

if __name__ == '__main__':
    app.run(port=5000)
