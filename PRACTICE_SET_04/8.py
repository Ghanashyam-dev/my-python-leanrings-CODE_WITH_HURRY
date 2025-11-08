# sum of digits 

# def sum_of_digits(a):
#     b = str(a)
#     s = 0 
#     for i in b :
#         s += int(i)
#     return s 
        


# a = 7532
# print(sum_of_digits(a))



def sum(n):
    if n==0:
        return n 


    return (n%10) + sum(n//10)

print(sum(7532))