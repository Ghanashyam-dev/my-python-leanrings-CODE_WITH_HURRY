# global keyword for chaning the gloabal variable value within the funtion
def sum(a,b):
    print(("hello"))
    c = a + b 
    global z # modifies the global z 
    z = 0 
    return c 
z = 3
print(z) 
print(sum(3,3))
print(z)