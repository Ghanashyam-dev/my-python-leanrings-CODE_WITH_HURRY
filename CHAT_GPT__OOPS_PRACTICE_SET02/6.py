class animal:
    def speak(self):
        print("depends on what animal it is!")

class dog(animal):
    def bark(self):
        print("BARK!")

d = dog()
d.bark()
d.speak()
