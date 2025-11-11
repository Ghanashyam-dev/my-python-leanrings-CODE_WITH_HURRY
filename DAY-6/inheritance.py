class  Animal: # Parent class (superclass)
       location = "Australia"
       def __init__(self, name):
         self.name = name



       def speak(self):
         print("Generic animal sound")

class Dog(Animal):  # Here the dog class get all the charecters preset in Animal class, which avoids rewriting the same attributs from animals useing inheritance.
    def speak(self):
        super().speak() # super is used to call parent attribute inside child class.
        print("Woof!")


a = Animal("dog")
a.speak()
a1 = Dog("lucky")
a1.speak()
print(a1.location)