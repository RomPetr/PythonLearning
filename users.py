""" Набор классов для представления пользователей онлайн сервиса """
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