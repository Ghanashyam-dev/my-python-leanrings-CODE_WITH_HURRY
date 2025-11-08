'''
factorial of number 
1 = 1 
2 = 2 x 1 
3 = 3 x 2 x 1 
4 = 4 x 3 x 2 x 1 
5 = 5 x 4 x 3 x 2 x 1 
....

n =  
'''


def fact(n):
    if n ==  1 or n ==0 :
        return n

    return n * fact(n-1)


print(fact(5))
print(fact(4))
print(fact(3))
print(fact(2))
print(fact(1))  
print(fact(0))  