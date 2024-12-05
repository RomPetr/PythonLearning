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
