def secure_login():
    print("--- SECURE LOGIN SYSTEM ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    print("\n--- secure Query Struction ---")
    print("SELECT * FROM users WHERE username=? AND password=?")
    print("Parameters:", (username, password))
    print("------------------------------\n")

    if username == "admin" and password == "password123":
        print("LOGIN SUCCESSFUL! (Valid credentials)")
    else:
        print("LOGIN FAILD! (Invalid credentials)")
secure_login()
           