sentance = "ghana"

def count(s):
    dic = {}
    
    for i in s :
        dic[f"{i}"] = s.count(i)
    print(dic)


        

count(sentance)
