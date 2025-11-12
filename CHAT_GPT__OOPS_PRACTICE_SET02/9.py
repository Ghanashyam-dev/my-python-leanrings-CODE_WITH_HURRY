class vehical:
    def start(self):
        print("Vehical is starting")

class bike(vehical):
    def start(self):
        super().start()
        print("bike is starting")


c = bike()
c.start()