def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")
choice = input("choose (1-2): ")
temp = float(input("Enter temperature: "))
if choice == "1":
    print("Result:", celsius_to_fahrenheit(temp))
elif choice == "2":
    print("Result:", fahrenheit_to_celsius(temp))
else:
    print("invalid choice !")
            