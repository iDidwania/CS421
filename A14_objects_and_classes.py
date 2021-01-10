class BackPack:

    def __init__(self, color, brand, size, use):
        self.color = color
        self.brand = brand
        self.size = size
        self.use = use

    def getDetails(self):
        print("Color: " + self.color)
        print("Brand: " + self.brand)
        print("Size: " + self.size)
        print("Use: " + self.use)
        print()

backpack_one = BackPack("Blue", "The North Face", "Large", "School")
backpack_one.getDetails()

backpack_two = BackPack("Pink", "Adidas", "Small", "Travel")
backpack_two.getDetails()

backpack_three = BackPack("Orange", "Eddie Bauer", "Medium", "Hiking")
backpack_three.getDetails()

backpack_four = BackPack("Grey", "The North Face", "Medium", "Work")
backpack_four.getDetails()


        
    
