#simple aaparoach
# a = 4 
# b = 2
# c = 1 
# print("avg",round((a+b+c)/3,2))

# useing function 
def avg(a,b,c):   #defining function
    dd = (a+b+c)/3.0  # code  to do something 
    print(dd)
    return dd # used to store the value with function and retures when we want to print the values 
     
     

d=avg(3,5,1)  # d stores the value returened in function
avg(1,2,3)  # calling the funtion
avg(2,2,2)
print(d)  #d prints the returned value