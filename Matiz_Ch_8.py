"""
# Позиционные аргументы
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
"""
# -------------------------------------
"""
# Именованные аргументы
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
"""
# -------------------------------------
# HW 8.4
def make_shirt(size='L', text='I love Python'):
    print(f"My shirt is size {size}, on it next text '{text}'.")

make_shirt('M', 'I love C')
