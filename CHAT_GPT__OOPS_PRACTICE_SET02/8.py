class shape():
    def area(self):
        print("Depends on what shap it is! ")
    
class rectangle(shape):
    def area(self):
        print("L x B")
        

class circle(shape):
    def area(self):
        print("PI x R²")

s = shape()
r = rectangle()
c = circle()

s.area()
r.area()
c.area()