# Recursion 
# best way to solve problems with formulas , must have base case value for avoiding infinity loops/recusion/calling function infinite time.

# fibinacci series 


'''
0 1 1 2 3 4 5 8 13 21
fib(0)= 0
fib(1)=1
fib(2)=fib(1)+fib(0)
fib(3)=fib(2)+fib(1)
.....
.....
fib(n)=fib(n-1)+fib(n-2)
'''

def fib(n):
    # base case 
    if (n==0 or n==1):
        return n
    else:

       return fib(n-2)+fib(n-1)



print(fib(5))
# workings :
# fib (5)
# fib(3)+fib(4)
# (fib(1)+fib(2))+(fib(2)+fib(3))
# (1+fib(0)+fib(1))+((fib(0)+fib(1))+fib(1)+fib(2))
# (1+0+1)+((0+1)+1+fib(0)+fib(1))
# (2)+(1+1+0+1)
# 5

print(fib(6))