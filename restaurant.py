class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of restaurant is '{self.restaurant_name}'")
        print(f"The cuisine of this restaurant is {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"I would like to inform you that the restaurant "
              f"'{self.restaurant_name}' is open for visiting from 14-00 to 02-00")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment
