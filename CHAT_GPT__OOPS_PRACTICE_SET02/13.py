# E-commarce simulation 

class product_prices():
    def products(self):

        print("Available products:\n1. soap-10RS\n2. shampoo-40Rs\n3. magi-12RS\n4. rice-100RS\n5.butter-70RS\n.")

class cart(product_prices):
    def products(self):
        super().products()
    

    def add_products(self):
        print("Enter the quantities needed below\n")
        self.soap = int(input("Soap: "))
        self.shampoo = int(input("Shampoo: "))
        self.magi = int(input("magi: "))
        self.rice = int(input("rice: "))
        self.butter = int(input("butter: "))

    def remove_product(self):
        print("\nEnter the quantities items if u need to remove below, or else press 0 \n")

        self.soap1 = int(input("Soap: "))
        self.soap = self.soap - self.soap1
        self.shampoo1 = int(input("Shampoo: "))
        self.shampoo = self.shampoo - self.shampoo1
        self.magi1= int(input("magi: "))
        self.magi = self.magi - self.magi1
        self.rice1 = int(input("rice: "))
        self.rice = self.rice - self.rice1
        self.butter1 = int(input("butter: "))
        self.butter = self.butter - self.butter1

    def total_price(self):
        print("\nTOTAL BILL:- below\n")
        self.total = print(f"soap:{self.soap}\nshampoo:{self.shampoo}\nmagi:{self.magi}\nrice:{self.rice}\nbutter:{self.butter}\nTotAL:{ (10*self.soap) + (40*self.shampoo) +(12*self.magi) + (100*self.rice )+ (70*self.butter)}")



b = cart()
b.products()
b.add_products()
b.remove_product()
b.total_price()




    




        

