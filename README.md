# Python Projects

My Python learning projects.

## Projects
- Calculator
- To-Do List
- Weather App
- Games
- File Manager
- Password Generator
- Currency Converter
- Grade Manager
- Decorators Practice
- Generators Practice

## Tools
- Python 3.14
- Git & GitHub
# Flask IDOR Vulnerability Lab

This repository demonstrates an Insecure Direct Object Reference (IDOR) vulnerability and how to fix it in a Flask application.

## 🚨 Vulnerable Version (vulnerable_app.py)
This version blindly trusts the user_id parameter in the URL (/my-account?user_id=1). An attacker can change the ID to access other users' sensitive data.

## 🛡️ Secure Version (fixed_app.py)
This version uses Flask session to verify the authenticated user's identity on the server side, ignoring any malicious user_id provided in the URL.

## 🛠️ How to Run
1. Install Flask: pip install flask
2. Run the vulnerable app: python vulnerable_app.py
3. Run the secure app: python fixed_app.py