class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, "makes a sound")
class dog(animal):
    def speak(self):
        print(self.name, "barks")
class cat(animal):
    def speak(self):
        print(self.name, "meows")
dog = dog("rex")
cat = cat("whiskers")
dog.speak()
cat.speak()
                            