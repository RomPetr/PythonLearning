"""
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
"""
# -------------------------------------

# HW 9.7
class User():

    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def describe_user(self):
        print(f"User info:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupatin}")

    def greet_user(self):
        print(f"Welcome {self.first_name} on our portal 'BoostIT'!\n")

    def greet_admin(self):
        print(f"Hello again, {self.first_name} {self.last_name}, my dear administrator!")

"""
class Admin(User):

    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        # self.occupation = None
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять сообщения',
            'разрешено удалять пользователей',
            'разрешено добавлять пользователей',
            'разрешено банить пользователей',]

    def show_privileges(self):
        print(f"This is a next privileges for {self.occupation}:")
        for privilege in self.privileges:
            print({privilege})

admin = Admin('Joe', 'Spencer', '45', 'male', 'Administrator')
admin.greet_admin()
admin.show_privileges()
"""
# -------------------------------------
# HW 9.8
class Privileges():
    def __init__(self):
        self.occupation = 'admin'
        self.privileges = [
            'разрешено добавлять сообщения',
            'разрешено удалять сообщения',
            'разрешено удалять пользователей',
            'разрешено добавлять пользователей',
            'разрешено банить пользователей', ]

    def show_privileges(self):
        print(f"This is a next privileges for {self.occupation}:")
        for privilege in self.privileges:
            print({privilege})


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privileges = Privileges()

admin = Admin('Joe', 'Spencer', '45', 'male', 'Administrator')
admin.greet_admin()
admin.privileges.show_privileges()
