class grandfather():
    def age(self):
        print("old")
    
class father(grandfather):
    def age(self):
        print("young man")
        # super().age() #TAKES AND PRINTS THE CHARECTERTICS OF GRANDFATHER .AGE()

class son(father):
    def age(self):
        print("yound boy")
        # super().age()   #TAKES AND PRINTS THE CHARECTERTICS OF FATHER .AGE()

s1 = son()
s1.age()
father.age(s1)
grandfather.age(s1) 