a = 0
l = []
s = 0
for i in range (1,51):
    if i % 2 ==0:
        print(i)
        l.append(i)
        a = a + 1
        s = s + i


print(l,"\nTheir are",a,"number of even from 1 to 50","\nSUM is:",s)
    