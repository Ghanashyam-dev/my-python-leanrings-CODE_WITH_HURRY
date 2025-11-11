class employee:
    company = "hp"
    def __init__(self, salary , name , bond ):
        self.salary = salary # creat an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        


    def get_salary(self):
        return self.salary # self is the referance of object created from class ,

    def get_info(self):
        print(f"The name of emloyee is {self.name}, slary is {self.salary}.The bond is for {self.bond}")
        
    
e1 = employee("34000","jonh",4)
print(e1.salary)
print(e1.get_salary())
(e1.get_info())