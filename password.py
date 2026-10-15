import secrets
import string
def generate_password(lengh):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password 
length = int(input("password length: "))
print("Your password:", generate_password(length))
      