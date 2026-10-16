with open("test.txt", "w") as f:
    f.write("Hello, this is a test file. \n")
    f.write("This is the second line. \n")
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
