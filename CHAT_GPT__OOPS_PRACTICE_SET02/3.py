class student:

    # here the constructor is a special method where initialize the attribute to the class and makes the initial state of object. 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name:{self.name}\nMarks:{self.marks}")

    def is_pass(self):
        if self.marks >= 40 :
            print("pass")
        else :
            print("fail")

s1 = student("ghana",39)
s2 = student("ghanashyam",40)

s1.display()
s1.is_pass()
s2.display()
s2.is_pass()