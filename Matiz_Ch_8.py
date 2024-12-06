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
"""
# HW 8.4
def make_shirt(size='L', text='I love Python'):
    print(f"My shirt is size {size}, on it next text '{text}'.")

make_shirt('M', 'I love C')
"""
# -------------------------------------
"""
# Возвращаемое значение
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
"""
# -------------------------------------
"""
# Возвращение словаря
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
"""
# -------------------------------------
"""
# Функция в цикле While
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease, tell me you name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
"""
# -------------------------------------
"""
# HW 8.7
def make_album(performer, album, tracks=None):
    get_album = {'performer': performer, 'album': album}
    if tracks:
        get_album['tracks'] = tracks
    return get_album

give_my_favorite_album = make_album('Drake', 'Take Care', 17)
print(give_my_favorite_album)
give_my_favorite_album = make_album('BTS', 'Map of the Soul')
print(give_my_favorite_album)
"""
# -------------------------------------
# Передача списка в функцию
"""
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
"""
# -------------------------------------
"""
# Изменение списка в функции
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
"""
# -------------------------------------
"""
# HW 8.9
def show_message(messages):
    for message in messages:
        print(message.capitalize())

msg = ['stop it', 'attention!', 'warning']
show_message(msg)
"""
# -------------------------------------
"""
# HW 8.10
def send_messages(messages, sent_messages):
    while messages:
        a = messages.pop()
        print(a.capitalize())
        sent_messages.append(a)


msg = ['stop it', 'attention!', 'warning']
sent_messages = []
send_messages(msg[:], sent_messages) # отправляем копию msg в функцию
print(msg)
print(sent_messages)
"""
# -------------------------------------
"""
# Передача произвольного набора аргументов
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
# -------------------------------------
"""
# Позиционные аргументы с произвольным набором аргументов
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')
"""
# -------------------------------------
# Использование произвольного набора именованных аргументов
def build_profile(first, last, **user_info):
    '''Строит словарь с информацией о пользователе'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princenton', field='physics')
print(user_profile)