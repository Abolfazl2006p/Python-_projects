def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "cannot divide by zero!"
    return a / b
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("choose (1-4): ")
a = float(input("First number: "))
b = float(input("Second number: "))
if choice == "1":
    print(add(a, b))
elif choice == "2":
    print(subtract(a, b))
elif choice == "3":
    print(multiply(a, b))
elif choice == "4":
    print(divide(a, b))
else:
    print("invalid choice!")
                        