def  sum(a,b):


    c = a + b  # c value can only be accesed inside function . these are called local variable.


    return c # once the c value is returned it pints the vlaue whenever it is called and then after the vlaues of a , b , c are wiped out inside the function.


d = 9 # this is global veriable. 


print(sum(1,1))