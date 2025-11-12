class dog():
    def speak(slef):
        print("BARKS")

class cat(dog):
    def speak(slef):
        print("MEOW")

class cow(cat):
    def speak(slef):
        print("AMMAA")

a =cow()

cat.speak(a)
cow.speak(a)
dog.speak(a)
    