try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("that's not a valid  number!")
except ZerodivisionError:
    print("you can't divide by zero!")
except Exception as e:
    print("Something went wrong:", e)
               