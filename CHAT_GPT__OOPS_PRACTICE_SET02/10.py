class calculator:
    def __init__(self,*args):
        self.x = args
        
        

    def sum(self):
         
         print(sum(self.x))





s1 = calculator(2,3,1,1,14)
s1.sum()