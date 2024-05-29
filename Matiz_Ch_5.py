"""
# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# -------------------------------------
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('YES')
else:
    print('NO')

# -------------------------------------
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# -------------------------------------

# HW 5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs 2+3 == 5?")
print(2 + 3 == 5)
print("\nIs 5+6 > 7+7?")
print(5+6 > 7+7 )

#--------------------------------------
# HW 5.2
str_1 = 'abc'
str_2 = 'bca'
str_3 = 'AbC'
list_1 = ['a', 'b', 'c', 'd']
# print(str_1 == str_2)
# print(str_1 == str_3.lower())
# print(45 > 34)
# print(67>=76)
if 's' in list_1:
    print('Yes')
else:
    print('No')

#--------------------------------------

# amusement_park (парк развлечений)
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

#--------------------------------------
"""
# multiple lists (множественные списки)
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")