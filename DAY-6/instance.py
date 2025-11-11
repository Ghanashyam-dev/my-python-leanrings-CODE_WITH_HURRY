class employee:
    company = "hp" # This is class attribute
    def __init__(self, salary , name , bond, company ):
        self.salary = salary # creat an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
        


    def get_salary(self):
        return self.salary # self is the referance of object created from class ,

    def get_info(self):
        print(f"The name of emloyee is {self.name}, slary is {self.salary}.The bond is for {self.bond}")
        

e1 = employee(40000,"john",4,"tesla")
print(e1.company) # it always print the instance attribute if present over class attribute.
print(employee.company) # this always print class attribute

# object introspection

# print(dir(e1))