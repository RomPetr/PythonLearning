# HW 9.6
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of restaurant is '{self.restaurant_name}'")
        print(f"The cuisine of this restaurant is {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"I would like to inform you that the restaurant "
              f"'{self.restaurant_name}' is open for visiting from 14-00 to 02-00")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors_types(self):
        print(f"This restaurant have the next flavors: {self.flavors}")


ice_cream = IceCreamStand('MyCream', 'ice creams', 'vanilla',
                          'chocolate', 'strawberry', 'mint')
ice_cream.describe_restaurant()
ice_cream.get_flavors_types()