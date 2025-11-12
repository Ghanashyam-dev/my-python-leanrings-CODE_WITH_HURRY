class student():

    def __init__(self,name,science,sst,math):
        self.name = name 
        self.marks_science = science
        self.marks_sst = sst 
        self.marks_math = math 

    def avg(self):
        self.avg_ = ((self.marks_sst + self.marks_science + self.marks_math)/3)
        print(f"avg marks of {self.name}:{self.avg_}")

    def grade(self):
        if self.avg_ <=20:
            print("(D)")
        elif self.avg_ < 30:
            print("(c)")
        elif self.avg_ >=30 and self.avg_<70:
            print("(B)")
        else :
           print("(A)")

s1 = student("ghana",40,40,40)
s2 = student("shyam",10,10,10)
s1.avg()
s1.grade()
s2.avg()
s2.grade()
