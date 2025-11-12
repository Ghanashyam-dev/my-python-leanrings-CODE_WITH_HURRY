class bankaccount:


    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.balance = amount

    def check_balance(self):
        print(f"Balance:{self.balance}")

    def deposite(self):
        d = int(input("Deposite ammount: "))
        self.balance=self.balance+d
        print(f"success,Balance = {self.balance}")

    def withdraw(self):
        
        w = int(input("withdraw ammount: "))
        if self.balance >= w:
            self.balance=self.balance-w
            print(f"success,Balance = {self.balance}")
        else :
            print("LOW BALANCE")

    
p1 = bankaccount("ghana",1500)
print(p1.name)
print(p1.amount)
p1.check_balance()
p1.deposite()
p1.withdraw()
p1.check_balance()

p2 = bankaccount("shyam",500)
print(p2.name)
print(p2.amount)
p2.check_balance()
p2.deposite()
p2.withdraw()
p2.check_balance()




    

    

    
    
        

    
        


