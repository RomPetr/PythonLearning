"""
class Dog():
    '''Простая модель собаки.'''

    def __init__(self, name, age):
        '''Инициализирует атрибуты name и age'''
        self.name = name.title()
        self.age = age

    def sit(self):
        '''Собака садится по команде'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Собака перекатывается по команде'''
        print(f"{self.name} rolled ower!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
"""
# -------------------------------------
"""
# HW 9.1
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


my_restaurant = Restaurant('WilliWonka', 'American')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
"""
# -------------------------------------
"""
# HW 9.2
first_restaurant = Restaurant('Oglu', 'Buratian')
second_restaurant = Restaurant('ChiShu', 'Chinese')
third_restaurant = Restaurant('Pablo', 'Mexican')

first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
"""
# -------------------------------------
# HW 9.3
class User():

    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupatin = occupation

    def describe_user(self):
        print(f"User info:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupatin}")

    def greet_user(self):
        print(f"Welcome {self.first_name} on our portal 'BoostIT'!\n")

first_user = User('Marie', 'Dubua', 19, 'Female', 'Artist')
second_user = User('Poll', 'Achkins', 30, 'Male', 'Engineer')
first_user.describe_user()
first_user.greet_user()
second_user.describe_user()
second_user.greet_user()

