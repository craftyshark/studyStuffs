# Define a class 'car' with attributes 'brand', 'model', 'year', and 'color'. Also, within
# this class, define a method 'car_info' that returns a string describing these attributes

class Car :
    def __init__ (self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def car_info (self):
        