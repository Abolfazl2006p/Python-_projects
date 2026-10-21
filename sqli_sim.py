def login():
    print("--- VULNERABLE LOGIN SYSTEM ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    print("\n--- Query sent to database ---")
    print(query)
    print("------------------------------\n")

    clean_query = query.upper().replace(" ","")

    if "OR1=1" in clean_query or "'--" in clean_query:
        print("LOGIN SUCCESSFUL! (SQL injection worked)")
    elif username == "admin" and password == "password123":
        print("LOGIN SUCCESSFUL! (VALID credentials)") 
    else:
        print("LOGIN FAILED! (invalid credentials)")
login()
                     