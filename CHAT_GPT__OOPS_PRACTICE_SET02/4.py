class circle:
    def __init__(self,radius ):
        self.radius = radius

    def area(self):
        print(f"area:{round(3.14*(self.radius**2),2)}")

    def parimeter(self):
        print(f"perimeter:{round((3.14*self.radius)*2,2)}")


c1 = circle(10)
c1.area()
c1.parimeter()


    
