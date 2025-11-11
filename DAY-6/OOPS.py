# class - is a blueprint or a template . eg- form for an exam which containg student details like name, age,class,subjects ect...

# object - an instance derived from the class blue print , eg - form which contains the data like name , subjects , age , class ect... 



class employee:
    company = "hp"

    def get_salary(self): # self is the referance of object created from class ,
        return 40000
    

e = employee()  # here an object of class e of class employeee is created here 
print(e.get_salary())  # we call emplyee get salaray method 


e2 = employee()
print(e2.get_salary())
print(e2.company)
print(e.company)
