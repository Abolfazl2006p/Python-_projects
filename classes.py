class person:
    def __init__(self, name, age):
        self .name = name
        self .age = age
    def greet(self):
        print("hello, my name is", self.name)
person1 = person("ali", 20)
person1.greet()
print(person1.age)

      